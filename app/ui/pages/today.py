"""
KnightOS Today Page - Daily Training Overview
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter

from app.theme import *
from app.ui.icons import CLOCK_ICON, CALENDAR_ICON, CHECK_ICON, ADD_ICON


class TodayTaskCard(QWidget):
    """Task card for today's training"""
    
    def __init__(self, title, duration, status="pending", parent=None):
        super().__init__(parent)
        
        status_colors = {
            "pending": SECONDARY_TEXT,
            "completed": SUCCESS,
            "in_progress": ACCENT
        }
        
        self.setStyleSheet(f"""
            background-color: {CARD};
            border-radius: {CARD_RADIUS}px;
            padding: {CARD_PADDING}px;
            
            border: 1px solid {status_colors[status]};
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
        
        # Status indicator
        status_indicator = QLabel()
        status_indicator.setFixedSize(12, 12)
        status_indicator.setStyleSheet(f"""
            background-color: {status_colors[status]};
            border-radius: 6px;
        """)
        
        title_label = QLabel(title)
        title_label.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {BODY_SIZE + 1}px;
            font-weight: 500;
        """)
        
        header_layout.addWidget(status_indicator)
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        # Duration
        duration_label = QLabel(duration)
        duration_label.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {SMALL_SIZE}px;
        """)
        
        header_layout.addWidget(duration_label)
        header.setLayout(header_layout)
        
        layout.addWidget(header)
        
        # Progress bar for in-progress tasks
        if status == "in_progress":
            progress = QWidget()
            progress.setFixedHeight(4)
            progress.setStyleSheet(f"""
                background-color: {SIDEBAR};
                border-radius: 2px;
            """)
            
            progress_fill = QWidget()
            progress_fill.setFixedHeight(4)
            progress_fill.setFixedWidth(100)
            progress_fill.setStyleSheet(f"""
                background-color: {ACCENT};
                border-radius: 2px;
            """)
            
            progress_layout = QHBoxLayout()
            progress_layout.setContentsMargins(0, 0, 0, 0)
            progress_layout.setSpacing(0)
            progress_layout.addWidget(progress_fill)
            progress.setLayout(progress_layout)
            
            layout.addWidget(progress)
        
        self.setLayout(layout)


class DailyScheduleCard(QWidget):
    """Daily schedule overview"""
    
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
        title = QLabel("Daily Schedule")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Schedule items
        schedule_items = [
            ("08:00 - 08:30", "Morning Warm-up", "completed"),
            ("09:00 - 10:00", "Opening Study", "completed"),
            ("11:00 - 12:00", "Tactical Training", "in_progress"),
            ("14:00 - 15:00", "Endgame Practice", "pending"),
            ("16:00 - 17:00", "Game Analysis", "pending"),
        ]
        
        for time, activity, status in schedule_items:
            item = QWidget()
            item.setFixedHeight(48)
            item.setStyleSheet(f"""
                background-color: transparent;
                border-radius: {BUTTON_RADIUS}px;
            """)
            
            item_layout = QHBoxLayout()
            item_layout.setContentsMargins(0, 0, 0, 0)
            item_layout.setSpacing(SMALL_PADDING)
            item_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            
            time_label = QLabel(time)
            time_label.setStyleSheet(f"""
                color: {TERTIARY_TEXT};
                font-size: {SMALL_SIZE}px;
            """)
            time_label.setFixedWidth(80)
            
            activity_label = QLabel(activity)
            activity_label.setStyleSheet(f"""
                color: {PRIMARY_TEXT};
                font-size: {BODY_SIZE}px;
            """)
            
            status_label = QLabel()
            status_label.setFixedSize(8, 8)
            status_colors = {
                "completed": SUCCESS,
                "in_progress": ACCENT,
                "pending": SECONDARY_TEXT
            }
            status_label.setStyleSheet(f"""
                background-color: {status_colors[status]};
                border-radius: 4px;
            """)
            
            item_layout.addWidget(time_label)
            item_layout.addWidget(activity_label)
            item_layout.addStretch()
            item_layout.addWidget(status_label)
            
            item.setLayout(item_layout)
            layout.addWidget(item)
        
        layout.addWidget(title)
        for time, activity, status in schedule_items:
            item = QWidget()
            item.setFixedHeight(48)
            item.setStyleSheet(f"""
                background-color: transparent;
                border-radius: {BUTTON_RADIUS}px;
            """)
            
            item_layout = QHBoxLayout()
            item_layout.setContentsMargins(0, 0, 0, 0)
            item_layout.setSpacing(SMALL_PADDING)
            item_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            
            time_label = QLabel(time)
            time_label.setStyleSheet(f"""
                color: {TERTIARY_TEXT};
                font-size: {SMALL_SIZE}px;
            """)
            time_label.setFixedWidth(80)
            
            activity_label = QLabel(activity)
            activity_label.setStyleSheet(f"""
                color: {PRIMARY_TEXT};
                font-size: {BODY_SIZE}px;
            """)
            
            status_label = QLabel()
            status_label.setFixedSize(8, 8)
            status_colors = {
                "completed": SUCCESS,
                "in_progress": ACCENT,
                "pending": SECONDARY_TEXT
            }
            status_label.setStyleSheet(f"""
                background-color: {status_colors[status]};
                border-radius: 4px;
            """)
            
            item_layout.addWidget(time_label)
            item_layout.addWidget(activity_label)
            item_layout.addStretch()
            item_layout.addWidget(status_label)
            
            item.setLayout(item_layout)
            layout.addWidget(item)
        
        self.setLayout(layout)


class QuickActionsCard(QWidget):
    """Quick actions for today"""
    
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
        title = QLabel("Quick Actions")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Action buttons
        actions = [
            ("Start Training", ADD_ICON),
            ("Review Game", """<svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M14 2H6C5.46957 2 4.96086 2.21071 4.58579 2.58579C4.21071 2.96086 4 3.46957 4 4V20C4 20.5304 4.21071 21.0391 4.58579 21.4142C4.96086 21.7893 5.46957 22 6 22H18C18.5304 22 19.0391 21.7893 19.4142 21.4142C19.7893 21.0391 20 20.5304 20 20V8L14 2Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M14 2V8H20" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M12 18H12.01" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""),
            ("Analyze Position", """<svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M21 16V8A2 2 0 0 0 19 6H5A2 2 0 0 0 3 8V16A2 2 0 0 0 5 18H19A2 2 0 0 0 21 16Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M7 12H17" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M7 8H17" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M7 16H17" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""),
            ("Set Goal", """<svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12 2L13.09 8.26L20 9L13.09 9.74L12 16L10.91 9.74L4 9L10.91 8.26L12 2Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M12 16V22" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M12 16C14.2091 16 16 17.7909 16 20C16 22.2091 14.2091 24 12 24C9.79086 24 8 22.2091 8 20C8 17.7909 9.79086 16 12 16Z" stroke="currentColor" stroke-width="2"/>
</svg>""")
        ]
        
        for action_text, icon_svg in actions:
            button = QPushButton()
            button.setFixedHeight(BUTTON_HEIGHT)
            button.setStyleSheet(f"""
                QPushButton {{
                    background-color: {SIDEBAR};
                    border-radius: {BUTTON_RADIUS}px;
                    color: {PRIMARY_TEXT};
                    font-size: {BODY_SIZE}px;
                    padding: 0 {BUTTON_PADDING}px;
                    text-align: left;
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
            
            button_layout = QHBoxLayout()
            button_layout.setContentsMargins(SMALL_PADDING, 0, SMALL_PADDING, 0)
            button_layout.setSpacing(SMALL_PADDING)
            button_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            
            icon_label = QLabel()
            icon_label.setPixmap(self._create_icon(icon_svg, 20, 20, ACCENT))
            icon_label.setFixedSize(20, 20)
            
            text_label = QLabel(action_text)
            text_label.setStyleSheet(f"""
                color: {PRIMARY_TEXT};
                font-size: {BODY_SIZE}px;
            """)
            
            button_layout.addWidget(icon_label)
            button_layout.addWidget(text_label)
            button_layout.addStretch()
            
            button_container = QWidget()
            button_container.setLayout(button_layout)
            
            # Use a container to avoid QPushButton layout issues
            button.setLayout(QHBoxLayout())
            button.layout().addWidget(button_container)
            
            layout.addWidget(button)
        
        layout.addWidget(title)
        for action_text, icon_svg in actions:
            button = QPushButton()
            button.setFixedHeight(BUTTON_HEIGHT)
            button.setStyleSheet(f"""
                QPushButton {{
                    background-color: {SIDEBAR};
                    border-radius: {BUTTON_RADIUS}px;
                    color: {PRIMARY_TEXT};
                    font-size: {BODY_SIZE}px;
                    padding: 0 {BUTTON_PADDING}px;
                    text-align: left;
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
            
            button_layout = QHBoxLayout()
            button_layout.setContentsMargins(SMALL_PADDING, 0, SMALL_PADDING, 0)
            button_layout.setSpacing(SMALL_PADDING)
            button_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            
            icon_label = QLabel()
            icon_label.setPixmap(self._create_icon(icon_svg, 20, 20, ACCENT))
            icon_label.setFixedSize(20, 20)
            
            text_label = QLabel(action_text)
            text_label.setStyleSheet(f"""
                color: {PRIMARY_TEXT};
                font-size: {BODY_SIZE}px;
            """)
            
            button_layout.addWidget(icon_label)
            button_layout.addWidget(text_label)
            button_layout.addStretch()
            
            button_container = QWidget()
            button_container.setLayout(button_layout)
            
            button.setLayout(QHBoxLayout())
            button.layout().addWidget(button_container)
            
            layout.addWidget(button)
        
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


class Today(QWidget):
    """Today Page - Daily training overview"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: {BACKGROUND};
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(PADDING, PADDING, PADDING, PADDING)
        layout.setSpacing(CARD_PADDING)
        
        # Title
        title = QLabel("Today's Training")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {TITLE_SIZE}px;
            font-weight: 600;
        """)
        
        # Stats Row
        stats_layout = QHBoxLayout()
        stats_layout.setContentsMargins(0, 0, 0, 0)
        stats_layout.setSpacing(CARD_PADDING)
        
        # Today's Tasks
        tasks_card = TodayTaskCard("Calculation Training", "45 min", "in_progress")
        tasks_card.setMinimumWidth(250)
        
        tasks_card2 = TodayTaskCard("Opening Review", "30 min", "completed")
        tasks_card2.setMinimumWidth(250)
        
        tasks_card3 = TodayTaskCard("Endgame Study", "25 min", "pending")
        tasks_card3.setMinimumWidth(250)
        
        stats_layout.addWidget(tasks_card)
        stats_layout.addWidget(tasks_card2)
        stats_layout.addWidget(tasks_card3)
        stats_layout.addStretch()
        
        # Main Content
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(CARD_PADDING)
        
        # Daily Schedule
        schedule_card = DailyScheduleCard()
        schedule_card.setMinimumWidth(350)
        
        # Quick Actions
        actions_card = QuickActionsCard()
        actions_card.setMinimumWidth(300)
        
        main_layout.addWidget(schedule_card)
        main_layout.addWidget(actions_card)
        main_layout.addStretch()
        
        # Combine all
        layout.addWidget(title)
        layout.addSpacing(8)
        layout.addLayout(stats_layout)
        layout.addSpacing(CARD_PADDING)
        layout.addLayout(main_layout)
        layout.addStretch()
        
        self.setLayout(layout)
