"""
KnightOS Endgames Page
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtCore import Qt

from app.theme import *
from app.ui.icons import CHESS_ICON, CHART_LINE_ICON


class EndgameCategoryCard(QWidget):
    """Endgame category card"""
    
    def __init__(self, title, description, progress, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: {CARD};
            border-radius: {CARD_RADIUS}px;
            padding: {CARD_PADDING}px;
            
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(SMALL_PADDING)
        
        # Title
        title_label = QLabel(title)
        title_label.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE}px;
            font-weight: 600;
        """)
        
        # Description
        desc_label = QLabel(description)
        desc_label.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {BODY_SIZE - 1}px;
            line-height: 1.5;
        """)
        desc_label.setWordWrap(True)
        
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
        
        # Progress Text
        progress_text = QLabel(f"{int(progress)}% Mastery")
        progress_text.setStyleSheet(f"""
            color: {ACCENT};
            font-size: {CAPTION_SIZE}px;
            font-weight: 500;
        """)
        
        layout.addWidget(title_label)
        layout.addSpacing(4)
        layout.addWidget(desc_label)
        layout.addSpacing(SMALL_PADDING)
        layout.addWidget(progress_container)
        layout.addSpacing(4)
        layout.addWidget(progress_text)
        
        self.setLayout(layout)


class EndgamePositionCard(QWidget):
    """Endgame position card"""
    
    def __init__(self, title, fen, difficulty, parent=None):
        super().__init__(parent)
        
        difficulty_colors = {
            "Basic": SUCCESS,
            "Intermediate": WARNING,
            "Advanced": ERROR,
            "Master": ACCENT
        }
        
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
        
        title_label = QLabel(title)
        title_label.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {BODY_SIZE + 1}px;
            font-weight: 500;
        """)
        
        difficulty_badge = QLabel(difficulty)
        difficulty_color = difficulty_colors.get(difficulty, SECONDARY_TEXT)
        difficulty_badge.setStyleSheet(f"""
            background-color: {difficulty_color};
            color: {BACKGROUND};
            font-size: {CAPTION_SIZE}px;
            font-weight: 600;
            padding: 4px 8px;
            border-radius: {BUTTON_RADIUS - 4}px;
        """)
        
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        header_layout.addWidget(difficulty_badge)
        header.setLayout(header_layout)
        
        # FEN
        fen_label = QLabel(fen)
        fen_label.setStyleSheet(f"""
            color: {TERTIARY_TEXT};
            font-size: {CAPTION_SIZE}px;
            font-family: monospace;
        """)
        
        # Board placeholder
        board_placeholder = QLabel("Chess Board Visualization")
        board_placeholder.setFixedHeight(120)
        board_placeholder.setStyleSheet(f"""
            background-color: {SIDEBAR};
            border-radius: {BUTTON_RADIUS}px;
            color: {TERTIARY_TEXT};
            font-size: {SMALL_SIZE}px;
        """)
        board_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(header)
        layout.addSpacing(8)
        layout.addWidget(board_placeholder)
        layout.addSpacing(8)
        layout.addWidget(fen_label)
        layout.addStretch()
        
        self.setLayout(layout)


class EndgameStatsCard(QWidget):
    """Endgame statistics"""
    
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
        title = QLabel("Endgame Mastery")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Stats
        stats = [
            ("Basic Endgames", "95%", SUCCESS),
            ("Pawn Endgames", "88%", SUCCESS),
            ("Minor Piece", "75%", WARNING),
            ("Rook Endgames", "65%", WARNING),
            ("Queen Endgames", "55%", ERROR)
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


class Endgames(QWidget):
    """Endgames Page"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: {BACKGROUND};
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(PADDING, PADDING, PADDING, PADDING)
        layout.setSpacing(CARD_PADDING)
        
        # Title
        title = QLabel("Endgame Training")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {TITLE_SIZE}px;
            font-weight: 600;
        """)
        
        # Categories Grid
        categories_layout = QHBoxLayout()
        categories_layout.setContentsMargins(0, 0, 0, 0)
        categories_layout.setSpacing(CARD_PADDING)
        
        category1 = EndgameCategoryCard(
            "Basic Endgames",
            "King and pawn endgames, basic checkmates",
            95
        )
        category1.setMinimumWidth(280)
        
        category2 = EndgameCategoryCard(
            "Pawn Endgames",
            "Opposition, key squares, and pawn races",
            85
        )
        category2.setMinimumWidth(280)
        
        category3 = EndgameCategoryCard(
            "Minor Piece Endgames",
            "Bishop vs Knight, same-colored bishops",
            70
        )
        category3.setMinimumWidth(280)
        
        categories_layout.addWidget(category1)
        categories_layout.addWidget(category2)
        categories_layout.addWidget(category3)
        categories_layout.addStretch()
        
        # Positions Grid
        positions_layout = QHBoxLayout()
        positions_layout.setContentsMargins(0, 0, 0, 0)
        positions_layout.setSpacing(CARD_PADDING)
        
        position1 = EndgamePositionCard(
            "King and Pawn",
            "8/8/8/8/8/6k1/5p2/7K w - - 0 1",
            "Basic"
        )
        position1.setMinimumWidth(280)
        
        position2 = EndgamePositionCard(
            "Lucena Position",
            "8/8/8/8/8/5k2/5p2/7K w - - 0 1",
            "Intermediate"
        )
        position2.setMinimumWidth(280)
        
        position3 = EndgamePositionCard(
            "Philidor Position",
            "8/8/8/8/8/4k3/4p3/7K w - - 0 1",
            "Advanced"
        )
        position3.setMinimumWidth(280)
        
        positions_layout.addWidget(position1)
        positions_layout.addWidget(position2)
        positions_layout.addWidget(position3)
        positions_layout.addStretch()
        
        # Stats Card
        stats_card = EndgameStatsCard()
        stats_card.setMinimumWidth(350)
        
        # Combine all
        layout.addWidget(title)
        layout.addSpacing(8)
        layout.addLayout(categories_layout)
        layout.addSpacing(CARD_PADDING)
        layout.addLayout(positions_layout)
        layout.addSpacing(CARD_PADDING)
        layout.addWidget(stats_card)
        layout.addStretch()
        
        self.setLayout(layout)
