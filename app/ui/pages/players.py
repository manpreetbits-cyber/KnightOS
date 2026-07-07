"""
KnightOS Players Page
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt

from app.theme import *
from app.ui.icons import (
    USER_ICON, RATING_UP_ICON, RATING_DOWN_ICON,
    CHART_LINE_ICON, SEARCH_ICON
)


class PlayerCard(QWidget):
    """Player information card"""
    
    def __init__(self, name, rating, games_played, win_rate, trend="up", parent=None):
        super().__init__(parent)
        
        trend_colors = {
            "up": SUCCESS,
            "down": ERROR,
            "stable": SECONDARY_TEXT
        }
        
        trend_icons = {
            "up": RATING_UP_ICON,
            "down": RATING_DOWN_ICON,
            "stable": "-"
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
        
        # Avatar
        avatar_label = QLabel()
        avatar_label.setFixedSize(AVATAR_SIZE, AVATAR_SIZE)
        avatar_label.setStyleSheet(f"""
            background-color: {ACCENT};
            border-radius: {AVATAR_RADIUS}px;
            color: {BACKGROUND};
            font-weight: bold;
        """)
        avatar_label.setText(name[0] if name else "?")
        avatar_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Name and Rating
        info_container = QWidget()
        info_layout = QVBoxLayout()
        info_layout.setContentsMargins(0, 0, 0, 0)
        info_layout.setSpacing(2)
        
        name_label = QLabel(name)
        name_label.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {BODY_SIZE + 1}px;
            font-weight: 600;
        """)
        
        rating_label = QLabel(f"Rating: {rating}")
        rating_label.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {SMALL_SIZE}px;
        """)
        
        info_layout.addWidget(name_label)
        info_layout.addWidget(rating_label)
        info_container.setLayout(info_layout)
        
        header_layout.addWidget(avatar_label)
        header_layout.addWidget(info_container)
        header_layout.addStretch()
        
        # Trend
        trend_color = trend_colors.get(trend, SECONDARY_TEXT)
        trend_icon = trend_icons.get(trend, "")
        
        if trend_icon != "-":
            trend_label = QLabel()
            trend_label.setPixmap(self._create_icon(trend_icon, 20, 20, trend_color))
            trend_label.setFixedSize(20, 20)
            header_layout.addWidget(trend_label)
        
        header.setLayout(header_layout)
        
        # Stats Row
        stats_row = QWidget()
        stats_layout = QHBoxLayout()
        stats_layout.setContentsMargins(0, 0, 0, 0)
        stats_layout.setSpacing(SMALL_PADDING)
        
        games_label = QLabel(f"{games_played} games")
        games_label.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {CAPTION_SIZE}px;
        """)
        
        win_rate_label = QLabel(f"{win_rate}% win rate")
        win_rate_color = SUCCESS if win_rate >= 50 else WARNING if win_rate >= 40 else ERROR
        win_rate_label.setStyleSheet(f"""
            color: {win_rate_color};
            font-size: {CAPTION_SIZE}px;
            font-weight: 500;
        """)
        
        stats_layout.addWidget(games_label)
        stats_layout.addStretch()
        stats_layout.addWidget(win_rate_label)
        stats_row.setLayout(stats_layout)
        
        layout.addWidget(header)
        layout.addSpacing(4)
        layout.addWidget(stats_row)
        
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


class PlayerStatsCard(QWidget):
    """Player statistics"""
    
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
        title = QLabel("Player Statistics")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Stats
        stats = [
            ("Total Players", "42", ACCENT),
            ("Regular Opponents", "12", SUCCESS),
            ("Highest Rated Win", "2450", WARNING),
            ("Most Played", "Alex Johnson", INFO)
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
            
            value_label = QLabel(str(stat_value))
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
            
            value_label = QLabel(str(stat_value))
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


class Players(QWidget):
    """Players Page"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: {BACKGROUND};
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(PADDING, PADDING, PADDING, PADDING)
        layout.setSpacing(CARD_PADDING)
        
        # Title
        title = QLabel("Players Database")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {TITLE_SIZE}px;
            font-weight: 600;
        """)
        
        # Main Content
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(CARD_PADDING)
        
        # Stats Card
        stats_card = PlayerStatsCard()
        stats_card.setMinimumWidth(280)
        
        # Players Grid
        players_container = QWidget()
        players_layout = QVBoxLayout()
        players_layout.setContentsMargins(0, 0, 0, 0)
        players_layout.setSpacing(CARD_PADDING)
        
        # Row 1
        row1 = QHBoxLayout()
        row1.setContentsMargins(0, 0, 0, 0)
        row1.setSpacing(CARD_PADDING)
        
        player1 = PlayerCard("Alex Johnson", 2150, 24, 58.3, "up")
        player1.setMinimumWidth(280)
        
        player2 = PlayerCard("Maria Garcia", 2080, 18, 61.1, "stable")
        player2.setMinimumWidth(280)
        
        player3 = PlayerCard("David Wilson", 1950, 12, 45.8, "down")
        player3.setMinimumWidth(280)
        
        row1.addWidget(player1)
        row1.addWidget(player2)
        row1.addWidget(player3)
        row1.addStretch()
        
        # Row 2
        row2 = QHBoxLayout()
        row2.setContentsMargins(0, 0, 0, 0)
        row2.setSpacing(CARD_PADDING)
        
        player4 = PlayerCard("Sarah Chen", 2200, 15, 66.7, "up")
        player4.setMinimumWidth(280)
        
        player5 = PlayerCard("Michael Brown", 1850, 8, 37.5, "down")
        player5.setMinimumWidth(280)
        
        player6 = PlayerCard("Emily Davis", 2050, 20, 55.0, "stable")
        player6.setMinimumWidth(280)
        
        row2.addWidget(player4)
        row2.addWidget(player5)
        row2.addWidget(player6)
        row2.addStretch()
        
        # Row 3
        row3 = QHBoxLayout()
        row3.setContentsMargins(0, 0, 0, 0)
        row3.setSpacing(CARD_PADDING)
        
        player7 = PlayerCard("James Wilson", 1980, 10, 50.0, "up")
        player7.setMinimumWidth(280)
        
        player8 = PlayerCard("Lisa Taylor", 2100, 14, 64.3, "up")
        player8.setMinimumWidth(280)
        
        player9 = PlayerCard("Robert Green", 1750, 6, 33.3, "down")
        player9.setMinimumWidth(280)
        
        row3.addWidget(player7)
        row3.addWidget(player8)
        row3.addWidget(player9)
        row3.addStretch()
        
        players_layout.addLayout(row1)
        players_layout.addLayout(row2)
        players_layout.addLayout(row3)
        players_container.setLayout(players_layout)
        
        main_layout.addWidget(stats_card)
        main_layout.addWidget(players_container)
        main_layout.addStretch()
        
        # Combine all
        layout.addWidget(title)
        layout.addSpacing(8)
        layout.addLayout(main_layout)
        layout.addStretch()
        
        self.setLayout(layout)
