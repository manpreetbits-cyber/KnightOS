"""
KnightOS Openings Page - Visual Repertoire Management
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter

from app.theme import *
from app.ui.icons import (
    CHESS_ICON, PAWN_ICON, ROOK_ICON, KNIGHT_ICON, 
    BISHOP_ICON, QUEEN_ICON, KING_ICON,
    CHART_LINE_ICON, ADD_ICON, CHECK_ICON
)


class OpeningCard(QWidget):
    """Visual opening repertoire card"""
    
    def __init__(self, name, moves, progress, last_reviewed, confidence, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: {CARD};
            border-radius: {CARD_RADIUS}px;
            padding: {CARD_PADDING}px;
            
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(SMALL_PADDING)
        
        # Header
        header = QWidget()
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(SMALL_PADDING)
        header_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        # Piece Icon (based on opening type)
        piece_icon = self._get_piece_icon(name)
        icon_label = QLabel()
        icon_label.setPixmap(self._create_icon(piece_icon, 28, 28, ACCENT))
        icon_label.setFixedSize(28, 28)
        
        # Name
        name_label = QLabel(name)
        name_label.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE}px;
            font-weight: 600;
        """)
        
        header_layout.addWidget(icon_label)
        header_layout.addWidget(name_label)
        header_layout.addStretch()
        
        # Confidence Badge
        confidence_badge = QLabel(f"{confidence}%")
        confidence_color = SUCCESS if confidence >= 80 else WARNING if confidence >= 50 else ERROR
        confidence_badge.setStyleSheet(f"""
            background-color: {confidence_color};
            color: {BACKGROUND};
            font-size: {CAPTION_SIZE}px;
            font-weight: 600;
            padding: 4px 8px;
            border-radius: {BUTTON_RADIUS - 4}px;
        """)
        
        header_layout.addWidget(confidence_badge)
        header.setLayout(header_layout)
        
        # Moves
        moves_label = QLabel(moves)
        moves_label.setStyleSheet(f"""
            color: {ACCENT};
            font-size: {BODY_SIZE - 1}px;
            font-family: monospace;
        """)
        
        # Progress Bar
        progress_container = QWidget()
        progress_container.setFixedHeight(6)
        progress_container.setStyleSheet(f"""
            background-color: {SIDEBAR};
            border-radius: 3px;
        """)
        
        progress_fill = QWidget()
        progress_fill.setFixedHeight(6)
        progress_fill.setFixedWidth(int(progress * 2.5))
        progress_fill.setStyleSheet(f"""
            background: linear-gradient(90deg, {ACCENT} 0%, {ACCENT_HOVER} 100%);
            border-radius: 3px;
        """)
        
        progress_layout = QHBoxLayout()
        progress_layout.setContentsMargins(0, 0, 0, 0)
        progress_layout.setSpacing(0)
        progress_layout.addWidget(progress_fill)
        progress_container.setLayout(progress_layout)
        
        # Stats Row
        stats_row = QWidget()
        stats_layout = QHBoxLayout()
        stats_layout.setContentsMargins(0, 0, 0, 0)
        stats_layout.setSpacing(SMALL_PADDING)
        
        last_reviewed_label = QLabel(f"Last: {last_reviewed}")
        last_reviewed_label.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {CAPTION_SIZE}px;
        """)
        
        progress_text = QLabel(f"{progress}% Complete")
        progress_text.setStyleSheet(f"""
            color: {ACCENT};
            font-size: {CAPTION_SIZE}px;
            font-weight: 500;
        """)
        
        stats_layout.addWidget(last_reviewed_label)
        stats_layout.addStretch()
        stats_layout.addWidget(progress_text)
        stats_row.setLayout(stats_layout)
        
        layout.addWidget(header)
        layout.addSpacing(4)
        layout.addWidget(moves_label)
        layout.addSpacing(SMALL_PADDING)
        layout.addWidget(progress_container)
        layout.addSpacing(4)
        layout.addWidget(stats_row)
        
        self.setLayout(layout)
    
    def _get_piece_icon(self, name):
        """Get piece icon based on opening name"""
        name_lower = name.lower()
        if any(x in name_lower for x in ['pawn', 'gambit', 'defense']):
            return PAWN_ICON
        elif any(x in name_lower for x in ['rook', 'castle']):
            return ROOK_ICON
        elif any(x in name_lower for x in ['knight', 'horse']):
            return KNIGHT_ICON
        elif any(x in name_lower for x in ['bishop', 'fianchetto']):
            return BISHOP_ICON
        elif any(x in name_lower for x in ['queen', 'ladies']):
            return QUEEN_ICON
        else:
            return KING_ICON
    
    def _create_icon(self, svg_content, width, height, color=ACCENT):
        """Create an icon from SVG content"""
        from PySide6.QtSvg import QSvgRenderer
        
        renderer = QSvgRenderer()
        svg_with_color = svg_content.replace('stroke="currentColor"', f'stroke="{color}"')
        svg_with_color = svg_with_color.replace('fill="currentColor"', f'fill="{color}"')
        renderer.load(svg_with_color.encode())
        
        pixmap = QPixmap(width, height)
        pixmap.fill(Qt.GlobalColor.transparent)
        
        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()
        
        return pixmap


class OpeningStatsCard(QWidget):
    """Opening statistics overview"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: {CARD};
            border-radius: {CARD_RADIUS}px;
            padding: {CARD_PADDING}px;
            
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(CARD_PADDING)
        
        # Title
        title = QLabel("Repertoire Overview")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Stats
        stats = [
            ("Total Openings", "24", ACCENT),
            ("Mastered", "8", SUCCESS),
            ("In Progress", "12", WARNING),
            ("Need Review", "4", ERROR)
        ]
        
        for stat_name, stat_value, color in stats:
            stat_row = QWidget()
            stat_row.setFixedHeight(48)
            
            stat_layout = QHBoxLayout()
            stat_layout.setContentsMargins(0, 0, 0, 0)
            stat_layout.setSpacing(SMALL_PADDING)
            stat_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            
            name_label = QLabel(stat_name)
            name_label.setStyleSheet(f"""
                color: {SECONDARY_TEXT};
                font-size: {BODY_SIZE - 1}px;
            """)
            
            value_label = QLabel(stat_value)
            value_label.setStyleSheet(f"""
                color: {color};
                font-size: {BODY_SIZE + 1}px;
                font-weight: 600;
            """)
            
            stat_layout.addWidget(name_label)
            stat_layout.addStretch()
            stat_layout.addWidget(value_label)
            
            stat_row.setLayout(stat_layout)
            layout.addWidget(stat_row)
        
        layout.addWidget(title)
        for stat_name, stat_value, color in stats:
            stat_row = QWidget()
            stat_row.setFixedHeight(48)
            
            stat_layout = QHBoxLayout()
            stat_layout.setContentsMargins(0, 0, 0, 0)
            stat_layout.setSpacing(SMALL_PADDING)
            stat_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            
            name_label = QLabel(stat_name)
            name_label.setStyleSheet(f"""
                color: {SECONDARY_TEXT};
                font-size: {BODY_SIZE - 1}px;
            """)
            
            value_label = QLabel(stat_value)
            value_label.setStyleSheet(f"""
                color: {color};
                font-size: {BODY_SIZE + 1}px;
                font-weight: 600;
            """)
            
            stat_layout.addWidget(name_label)
            stat_layout.addStretch()
            stat_layout.addWidget(value_label)
            
            stat_row.setLayout(stat_layout)
            layout.addWidget(stat_row)
        
        self.setLayout(layout)


class OpeningTreeCard(QWidget):
    """Opening tree visualization"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: {CARD};
            border-radius: {CARD_RADIUS}px;
            padding: {CARD_PADDING}px;
            
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(CARD_PADDING)
        
        # Title
        title = QLabel("Opening Tree")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Tree visualization (simplified)
        tree_container = QWidget()
        tree_layout = QVBoxLayout()
        tree_layout.setContentsMargins(0, 0, 0, 0)
        tree_layout.setSpacing(4)
        
        # Main line
        main_line = QLabel("1. e4 e5 2. Nf3 Nc6 3. Bb5 a6")
        main_line.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {BODY_SIZE}px;
            font-family: monospace;
            background-color: {SIDEBAR};
            padding: {TINY_PADDING}px;
            border-radius: {BUTTON_RADIUS - 4}px;
        """)
        
        # Variations
        variations = [
            "4. Ba4 Nf6 5. O-O Be7",
            "4. Ba4 b5 5. Bb3 Nf6",
            "4. Ba4 Bb7 5. O-O Nf6"
        ]
        
        for variation in variations:
            var_label = QLabel(variation)
            var_label.setStyleSheet(f"""
                color: {SECONDARY_TEXT};
                font-size: {BODY_SIZE - 1}px;
                font-family: monospace;
                padding: {TINY_PADDING}px;
                margin-left: 20px;
            """)
            tree_layout.addWidget(var_label)
        
        tree_layout.addWidget(main_line)
        for variation in variations:
            var_label = QLabel(variation)
            var_label.setStyleSheet(f"""
                color: {SECONDARY_TEXT};
                font-size: {BODY_SIZE - 1}px;
                font-family: monospace;
                padding: {TINY_PADDING}px;
                margin-left: 20px;
            """)
            tree_layout.addWidget(var_label)
        
        tree_container.setLayout(tree_layout)
        
        layout.addWidget(title)
        layout.addWidget(tree_container)
        layout.addStretch()
        
        self.setLayout(layout)


class Openings(QWidget):
    """Openings Page - Visual repertoire management"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: {BACKGROUND};
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(PADDING, PADDING, PADDING, PADDING)
        layout.setSpacing(CARD_PADDING)
        
        # Title
        title = QLabel("Opening Repertoire")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {TITLE_SIZE}px;
            font-weight: 600;
        """)
        
        # Opening Cards Grid
        openings_layout = QHBoxLayout()
        openings_layout.setContentsMargins(0, 0, 0, 0)
        openings_layout.setSpacing(CARD_PADDING)
        
        # Row 1
        opening1 = OpeningCard(
            "Sicilian Defense",
            "1. e4 c5",
            90,
            "2 days ago",
            92
        )
        opening1.setMinimumWidth(280)
        
        opening2 = OpeningCard(
            "Ruy Lopez",
            "1. e4 e5 2. Nf3 Nc6 3. Bb5",
            75,
            "5 days ago",
            78
        )
        opening2.setMinimumWidth(280)
        
        opening3 = OpeningCard(
            "French Defense",
            "1. e4 e6",
            60,
            "1 week ago",
            65
        )
        opening3.setMinimumWidth(280)
        
        # Row 2
        opening4 = OpeningCard(
            "Caro-Kann",
            "1. e4 c6",
            80,
            "3 days ago",
            85
        )
        opening4.setMinimumWidth(280)
        
        opening5 = OpeningCard(
            "Italian Game",
            "1. e4 e5 2. Nf3 Nc6 3. Bc4",
            50,
            "2 weeks ago",
            55
        )
        opening5.setMinimumWidth(280)
        
        opening6 = OpeningCard(
            "Queen's Gambit",
            "1. d4 d5 2. c4",
            40,
            "1 month ago",
            45
        )
        opening6.setMinimumWidth(280)
        
        # Add to layout
        row1 = QHBoxLayout()
        row1.setContentsMargins(0, 0, 0, 0)
        row1.setSpacing(CARD_PADDING)
        row1.addWidget(opening1)
        row1.addWidget(opening2)
        row1.addWidget(opening3)
        row1.addStretch()
        
        row2 = QHBoxLayout()
        row2.setContentsMargins(0, 0, 0, 0)
        row2.setSpacing(CARD_PADDING)
        row2.addWidget(opening4)
        row2.addWidget(opening5)
        row2.addWidget(opening6)
        row2.addStretch()
        
        # Main Content
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(CARD_PADDING)
        
        # Stats Card
        stats_card = OpeningStatsCard()
        stats_card.setMinimumWidth(300)
        
        # Tree Card
        tree_card = OpeningTreeCard()
        tree_card.setMinimumWidth(350)
        
        main_layout.addWidget(stats_card)
        main_layout.addWidget(tree_card)
        main_layout.addStretch()
        
        # Combine all
        layout.addWidget(title)
        layout.addSpacing(8)
        layout.addLayout(row1)
        layout.addSpacing(CARD_PADDING)
        layout.addLayout(row2)
        layout.addSpacing(CARD_PADDING)
        layout.addLayout(main_layout)
        layout.addStretch()
        
        self.setLayout(layout)
