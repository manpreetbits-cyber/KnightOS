"""
KnightOS Dashboard - Personal Mission Control
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter

from app.theme import *
from app.ui.icons import (
    RATING_UP_ICON, CLOCK_ICON, CALENDAR_ICON, 
    CHART_RADAR_ICON, CHESS_ICON, CHECK_ICON
)


class StatCard(QWidget):
    """Beautiful floating stat card for dashboard"""
    
    def __init__(self, title, value, subtitle, icon_svg, color=ACCENT, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: {CARD};
            border-radius: {CARD_RADIUS}px;
            padding: {CARD_PADDING}px;
            
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(SMALL_PADDING)
        
        # Header with icon and title
        header = QWidget()
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(TINY_PADDING)
        header_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        icon_label = QLabel()
        icon_label.setPixmap(self._create_icon(icon_svg, 24, 24, color))
        icon_label.setFixedSize(24, 24)
        
        title_label = QLabel(title)
        title_label.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {SMALL_SIZE}px;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        """)
        
        header_layout.addWidget(icon_label)
        header_layout.addWidget(title_label)
        header.setLayout(header_layout)
        
        # Value
        value_label = QLabel(value)
        value_label.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {TITLE_SIZE - 8}px;
            font-weight: bold;
        """)
        
        # Subtitle
        subtitle_label = QLabel(subtitle)
        subtitle_label.setStyleSheet(f"""
            color: {TERTIARY_TEXT};
            font-size: {CAPTION_SIZE}px;
        """)
        
        layout.addWidget(header)
        layout.addSpacing(4)
        layout.addWidget(value_label)
        layout.addWidget(subtitle_label)
        layout.addStretch()
        
        self.setLayout(layout)
    
    def _create_icon(self, svg_content, width, height, color):
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


class MissionCard(QWidget):
    """Today's Mission card with checkbox items"""
    
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
        title = QLabel("Today's Mission")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Mission Items
        mission_items = [
            "30 min Calculation",
            "Review Yesterday's Game",
            "Petrov Repertoire",
            "Endgame Study"
        ]
        
        for item_text in mission_items:
            item = self._create_mission_item(item_text)
            layout.addWidget(item)
        
        layout.addWidget(title)
        for item_text in mission_items:
            item = self._create_mission_item(item_text)
            layout.addWidget(item)
        
        self.setLayout(layout)
    
    def _create_mission_item(self, text):
        """Create a mission item with checkbox"""
        container = QWidget()
        container.setFixedHeight(48)
        container.setStyleSheet(f"""
            background-color: transparent;
            border-radius: {BUTTON_RADIUS}px;
        """)
        
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(SMALL_PADDING)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        # Checkbox
        checkbox = QLabel()
        checkbox.setFixedSize(24, 24)
        checkbox.setStyleSheet(f"""
            background-color: transparent;
            border: 2px solid {SECONDARY_TEXT};
            border-radius: 6px;
        """)
        checkbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Text
        text_label = QLabel(text)
        text_label.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {BODY_SIZE}px;
        """)
        
        layout.addWidget(checkbox)
        layout.addWidget(text_label)
        layout.addStretch()
        
        container.setLayout(layout)
        return container


class CoachRecommendationCard(QWidget):
    """AI Coach recommendation card"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background: linear-gradient(135deg, {CARD} 0%, {CARD_HOVER} 100%);
            border-radius: {CARD_RADIUS}px;
            padding: {CARD_PADDING}px;
            
            border: 1px solid rgba(200, 155, 60, 0.2);
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
        
        icon_label = QLabel()
        icon_label.setPixmap(self._create_icon(CHESS_ICON, 28, 28, ACCENT))
        icon_label.setFixedSize(28, 28)
        
        title = QLabel("Coach Recommendation")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE}px;
            font-weight: 600;
        """)
        
        header_layout.addWidget(icon_label)
        header_layout.addWidget(title)
        header_layout.addStretch()
        header.setLayout(header_layout)
        
        # Recommendation Text
        recommendation = QLabel("Your tactical vision has improved. Today's priority is defending worse positions.")
        recommendation.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {BODY_SIZE}px;
            line-height: 1.6;
        """)
        recommendation.setWordWrap(True)
        
        layout.addWidget(header)
        layout.addSpacing(8)
        layout.addWidget(recommendation)
        
        self.setLayout(layout)
    
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


class Dashboard(QWidget):
    """Main Dashboard page"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: {BACKGROUND};
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(PADDING, PADDING, PADDING, PADDING)
        layout.setSpacing(CARD_PADDING)
        
        # Greeting
        greeting = QLabel("Good afternoon, Shehzaad.")
        greeting.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {TITLE_SIZE + 4}px;
            font-weight: 600;
        """)
        
        # Stats Row
        stats_layout = QHBoxLayout()
        stats_layout.setContentsMargins(0, 0, 0, 0)
        stats_layout.setSpacing(CARD_PADDING)
        
        # Current Rating
        rating_card = StatCard(
            "Current Rating", 
            "2150", 
            "+42 this month", 
            RATING_UP_ICON, 
            SUCCESS
        )
        
        # Training Streak
        streak_card = StatCard(
            "Training Streak", 
            "12 days", 
            "Keep it going!", 
            """<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12 2L13.09 8.26L20 9L13.09 9.74L12 16L10.91 9.74L4 9L10.91 8.26L12 2Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>""", 
            WARNING
        )
        
        # Next Tournament
        tournament_card = StatCard(
            "Next Tournament", 
            "45 days", 
            "National Open 2024", 
            CALENDAR_ICON, 
            INFO
        )
        
        # Opening Preparedness
        opening_card = StatCard(
            "Opening Prep", 
            "85%", 
            "Sicilian Defense", 
            CHART_RADAR_ICON, 
            ACCENT
        )
        
        stats_layout.addWidget(rating_card)
        stats_layout.addWidget(streak_card)
        stats_layout.addWidget(tournament_card)
        stats_layout.addWidget(opening_card)
        stats_layout.addStretch()
        
        # Main Content
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(CARD_PADDING)
        
        # Today's Mission
        mission_card = MissionCard()
        mission_card.setMinimumWidth(400)
        
        # Coach Recommendation
        coach_card = CoachRecommendationCard()
        coach_card.setMinimumWidth(400)
        
        main_layout.addWidget(mission_card)
        main_layout.addWidget(coach_card)
        main_layout.addStretch()
        
        # Combine all
        layout.addWidget(greeting)
        layout.addSpacing(8)
        layout.addLayout(stats_layout)
        layout.addLayout(main_layout)
        layout.addStretch()
        
        self.setLayout(layout)
