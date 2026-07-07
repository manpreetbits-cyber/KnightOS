"""
KnightOS Games Page - Beautiful Game Cards
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt

from app.theme import *
from app.ui.icons import (
    CHESS_ICON, CALENDAR_ICON, CLOCK_ICON,
    WIN_ICON, LOSS_ICON, DRAW_ICON,
    USER_ICON, MORE_ICON
)


class GameCard(QWidget):
    """Beautiful modern game card"""
    
    def __init__(self, event, round_num, opponent, result, opening, date, parent=None):
        super().__init__(parent)
        
        result_icons = {
            "Win": WIN_ICON,
            "Loss": LOSS_ICON,
            "Draw": DRAW_ICON
        }
        
        result_colors = {
            "Win": SUCCESS,
            "Loss": ERROR,
            "Draw": INFO
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
        
        # Event and Round
        event_label = QLabel(f"{event} • Round {round_num}")
        event_label.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {BODY_SIZE + 1}px;
            font-weight: 600;
        """)
        
        # Date
        date_label = QLabel(date)
        date_label.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {SMALL_SIZE}px;
        """)
        
        header_layout.addWidget(event_label)
        header_layout.addStretch()
        header_layout.addWidget(date_label)
        header.setLayout(header_layout)
        
        # Middle Row
        middle_row = QWidget()
        middle_layout = QHBoxLayout()
        middle_layout.setContentsMargins(0, 0, 0, 0)
        middle_layout.setSpacing(SMALL_PADDING)
        middle_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        # Opponent
        opponent_label = QLabel(f"vs {opponent}")
        opponent_label.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {BODY_SIZE}px;
        """)
        
        # Result
        result_container = QWidget()
        result_layout = QHBoxLayout()
        result_layout.setContentsMargins(0, 0, 0, 0)
        result_layout.setSpacing(4)
        result_layout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        
        result_icon = QLabel()
        result_color = result_colors.get(result, SECONDARY_TEXT)
        result_icon.setPixmap(self._create_icon(result_icons.get(result, ""), 20, 20, result_color))
        result_icon.setFixedSize(20, 20)
        
        result_label = QLabel(result)
        result_label.setStyleSheet(f"""
            color: {result_color};
            font-size: {BODY_SIZE}px;
            font-weight: 600;
        """)
        
        result_layout.addWidget(result_icon)
        result_layout.addWidget(result_label)
        result_container.setLayout(result_layout)
        
        middle_layout.addWidget(opponent_label)
        middle_layout.addStretch()
        middle_layout.addWidget(result_container)
        middle_row.setLayout(middle_layout)
        
        # Bottom Row
        bottom_row = QWidget()
        bottom_layout = QHBoxLayout()
        bottom_layout.setContentsMargins(0, 0, 0, 0)
        bottom_layout.setSpacing(SMALL_PADDING)
        bottom_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        # Opening
        opening_label = QLabel(opening)
        opening_label.setStyleSheet(f"""
            color: {ACCENT};
            font-size: {SMALL_SIZE}px;
        """)
        
        # Review Button
        review_btn = QPushButton("Review")
        review_btn.setFixedHeight(32)
        review_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {SIDEBAR};
                border-radius: {BUTTON_RADIUS - 4}px;
                color: {PRIMARY_TEXT};
                font-size: {SMALL_SIZE}px;
                padding: 0 {SMALL_PADDING}px;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }}
            QPushButton:hover {{
                background-color: {CARD_HOVER};
                border-color: {ACCENT};
            }}
            QPushButton:pressed {{
                background-color: {CARD};
            }}
        """)
        
        bottom_layout.addWidget(opening_label)
        bottom_layout.addStretch()
        bottom_layout.addWidget(review_btn)
        bottom_row.setLayout(bottom_layout)
        
        layout.addWidget(header)
        layout.addSpacing(4)
        layout.addWidget(middle_row)
        layout.addSpacing(4)
        layout.addWidget(bottom_row)
        
        self.setLayout(layout)
    
    def _create_icon(self, svg_content, width, height, color):
        """Create an icon from SVG content"""
        from PySide6.QtSvg import QSvgRenderer
        from PySide6.QtGui import QPixmap, QPainter
        
        if not svg_content:
            return QPixmap(width, height)
        
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


class GameFiltersCard(QWidget):
    """Game filters and statistics"""
    
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
        title = QLabel("Filters & Stats")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Filter Buttons
        filters = ["All", "Recent", "Wins", "Losses", "Draws"]
        
        filter_layout = QHBoxLayout()
        filter_layout.setContentsMargins(0, 0, 0, 0)
        filter_layout.setSpacing(SMALL_PADDING)
        
        for filter_text in filters:
            filter_btn = QPushButton(filter_text)
            filter_btn.setFixedHeight(36)
            is_active = filter_text == "All"
            filter_btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {CARD if not is_active else ACCENT};
                    border-radius: {BUTTON_RADIUS - 4}px;
                    color: {PRIMARY_TEXT if not is_active else BACKGROUND};
                    font-size: {SMALL_SIZE}px;
                    padding: 0 {SMALL_PADDING}px;
                    border: 1px solid {ACCENT if is_active else 'rgba(255, 255, 255, 0.1)'};
                }}
                QPushButton:hover {{
                    background-color: {CARD_HOVER};
                }}
            """)
            filter_layout.addWidget(filter_btn)
        
        filter_layout.addStretch()
        
        # Stats
        stats = [
            ("Total Games", "247", ACCENT),
            ("Wins", "124", SUCCESS),
            ("Losses", "89", ERROR),
            ("Draws", "34", INFO),
            ("Win Rate", "50.2%", SUCCESS)
        ]
        
        for stat_name, stat_value, color in stats:
            stat_row = QWidget()
            stat_row.setFixedHeight(40)
            
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
        layout.addWidget(QWidget())  # Spacer for filter layout
        filter_container = QWidget()
        filter_container.setLayout(filter_layout)
        layout.addWidget(filter_container)
        
        for stat_name, stat_value, color in stats:
            stat_row = QWidget()
            stat_row.setFixedHeight(40)
            
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


class Games(QWidget):
    """Games Page - Beautiful game cards"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: {BACKGROUND};
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(PADDING, PADDING, PADDING, PADDING)
        layout.setSpacing(CARD_PADDING)
        
        # Title
        title = QLabel("My Games")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {TITLE_SIZE}px;
            font-weight: 600;
        """)
        
        # Main Content
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(CARD_PADDING)
        
        # Filters Card
        filters_card = GameFiltersCard()
        filters_card.setMinimumWidth(280)
        
        # Games Grid
        games_container = QWidget()
        games_layout = QVBoxLayout()
        games_layout.setContentsMargins(0, 0, 0, 0)
        games_layout.setSpacing(CARD_PADDING)
        
        # Row 1
        row1 = QHBoxLayout()
        row1.setContentsMargins(0, 0, 0, 0)
        row1.setSpacing(CARD_PADDING)
        
        game1 = GameCard(
            "National Open 2024",
            3,
            "Alex Johnson",
            "Win",
            "Sicilian Defense: Najdorf",
            "2024-01-15"
        )
        game1.setMinimumWidth(320)
        
        game2 = GameCard(
            "Club Tournament",
            5,
            "Maria Garcia",
            "Draw",
            "Ruy Lopez: Morphy Defense",
            "2024-01-10"
        )
        game2.setMinimumWidth(320)
        
        game3 = GameCard(
            "Online Rapid",
            1,
            "ChessBot 3000",
            "Loss",
            "French Defense: Winawer",
            "2024-01-08"
        )
        game3.setMinimumWidth(320)
        
        row1.addWidget(game1)
        row1.addWidget(game2)
        row1.addWidget(game3)
        row1.addStretch()
        
        # Row 2
        row2 = QHBoxLayout()
        row2.setContentsMargins(0, 0, 0, 0)
        row2.setSpacing(CARD_PADDING)
        
        game4 = GameCard(
            "Friendly Match",
            1,
            "David Wilson",
            "Win",
            "Italian Game: Evans Gambit",
            "2024-01-05"
        )
        game4.setMinimumWidth(320)
        
        game5 = GameCard(
            "Training Game",
            2,
            "Coach AI",
            "Win",
            "Queen's Gambit: Declined",
            "2024-01-03"
        )
        game5.setMinimumWidth(320)
        
        game6 = GameCard(
            "Blitz Tournament",
            4,
            "Sarah Chen",
            "Draw",
            "Caro-Kann: Classical",
            "2024-01-01"
        )
        game6.setMinimumWidth(320)
        
        row2.addWidget(game4)
        row2.addWidget(game5)
        row2.addWidget(game6)
        row2.addStretch()
        
        games_layout.addLayout(row1)
        games_layout.addLayout(row2)
        games_container.setLayout(games_layout)
        
        main_layout.addWidget(filters_card)
        main_layout.addWidget(games_container)
        main_layout.addStretch()
        
        # Combine all
        layout.addWidget(title)
        layout.addSpacing(8)
        layout.addLayout(main_layout)
        layout.addStretch()
        
        self.setLayout(layout)
