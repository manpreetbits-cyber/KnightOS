"""
KnightOS Training Plan Page
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

from app.theme import *
from app.ui.icons import (
    CHESS_ICON, CLOCK_ICON, CALENDAR_ICON, 
    CHART_LINE_ICON, ADD_ICON, CHECK_ICON
)


class TrainingModuleCard(QWidget):
    """Training module card"""
    
    def __init__(self, title, description, progress, duration, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: {CARD};
            border-radius: {CARD_RADIUS}px;
            padding: {CARD_PADDING}px;
            box-shadow: {SHADOW_SMALL};
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
        icon_label.setPixmap(self._create_icon(CHESS_ICON, 24, 24, ACCENT))
        icon_label.setFixedSize(24, 24)
        
        title_label = QLabel(title)
        title_label.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE}px;
            font-weight: 600;
        """)
        
        header_layout.addWidget(icon_label)
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
        progress_container.setFixedHeight(8)
        progress_container.setStyleSheet(f"""
            background-color: {SIDEBAR};
            border-radius: 4px;
        """)
        
        progress_fill = QWidget()
        progress_fill.setFixedHeight(8)
        progress_fill.setFixedWidth(int(progress * 2.8))  # Scale to container width
        progress_fill.setStyleSheet(f"""
            background: linear-gradient(90deg, {ACCENT} 0%, {ACCENT_HOVER} 100%);
            border-radius: 4px;
        """)
        
        progress_layout = QHBoxLayout()
        progress_layout.setContentsMargins(0, 0, 0, 0)
        progress_layout.setSpacing(0)
        progress_layout.addWidget(progress_fill)
        progress_container.setLayout(progress_layout)
        
        # Progress Text
        progress_text = QLabel(f"{int(progress)}% Complete")
        progress_text.setStyleSheet(f"""
            color: {ACCENT};
            font-size: {CAPTION_SIZE}px;
            font-weight: 500;
        """)
        
        layout.addWidget(header)
        layout.addSpacing(4)
        layout.addWidget(desc_label)
        layout.addSpacing(SMALL_PADDING)
        layout.addWidget(progress_container)
        layout.addSpacing(4)
        layout.addWidget(progress_text)
        
        self.setLayout(layout)
    
    def _create_icon(self, svg_content, width, height, color=ACCENT):
        """Create an icon from SVG content"""
        from PySide6.QtSvg import QSvgRenderer
        from PySide6.QtGui import QPixmap
        
        renderer = QSvgRenderer()
        svg_with_color = svg_content.replace('stroke="currentColor"', f'stroke="{color}"')
        svg_with_color = svg_with_color.replace('fill="currentColor"', f'fill="{color}"')
        renderer.load(svg_with_color.encode())
        
        pixmap = QPixmap(width, height)
        pixmap.fill(Qt.GlobalColor.transparent)
        renderer.render(QPixmap(pixmap))
        
        return pixmap


class WeeklyScheduleCard(QWidget):
    """Weekly training schedule"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: {CARD};
            border-radius: {CARD_RADIUS}px;
            padding: {CARD_PADDING}px;
            box-shadow: {SHADOW_MEDIUM};
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(CARD_PADDING)
        
        # Title
        title = QLabel("Weekly Schedule")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Days of week
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        
        # Schedule data
        schedule = [
            ["Tactics", "Openings", "-", "-", "-"],
            ["Endgames", "Calculation", "-", "-", "-"],
            ["Review", "Puzzles", "-", "-", "-"],
            ["Analysis", "Training", "-", "-", "-"],
            ["Rest", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-"]
        ]
        
        # Header row
        header_row = QWidget()
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(0)
        
        # Empty cell for time
        empty_header = QLabel("")
        empty_header.setFixedWidth(60)
        header_layout.addWidget(empty_header)
        
        for day in days:
            day_label = QLabel(day)
            day_label.setFixedWidth(80)
            day_label.setStyleSheet(f"""
                color: {TERTIARY_TEXT};
                font-size: {CAPTION_SIZE}px;
                font-weight: 600;
                text-align: center;
            """)
            header_layout.addWidget(day_label)
        
        header_row.setLayout(header_layout)
        
        # Schedule rows
        times = ["08:00", "09:00", "10:00", "11:00", "12:00"]
        
        for i, time in enumerate(times):
            row = QWidget()
            row_layout = QHBoxLayout()
            row_layout.setContentsMargins(0, 0, 0, 0)
            row_layout.setSpacing(0)
            
            # Time label
            time_label = QLabel(time)
            time_label.setFixedWidth(60)
            time_label.setStyleSheet(f"""
                color: {SECONDARY_TEXT};
                font-size: {SMALL_SIZE}px;
            """)
            row_layout.addWidget(time_label)
            
            # Schedule cells
            for j in range(5):
                if i < len(schedule) and j < len(schedule[i]):
                    cell_text = schedule[i][j]
                else:
                    cell_text = "-"
                
                cell = QLabel(cell_text if cell_text != "-" else "")
                cell.setFixedWidth(80)
                cell.setFixedHeight(40)
                cell.setAlignment(Qt.AlignmentFlag.AlignCenter)
                
                if cell_text != "-":
                    cell.setStyleSheet(f"""
                        background-color: {SIDEBAR};
                        color: {PRIMARY_TEXT};
                        font-size: {SMALL_SIZE}px;
                        border-radius: {BUTTON_RADIUS - 4}px;
                    """)
                else:
                    cell.setStyleSheet(f"""
                        color: transparent;
                    """)
                
                row_layout.addWidget(cell)
            
            row.setLayout(row_layout)
            layout.addWidget(row)
        
        layout.addWidget(title)
        layout.addWidget(header_row)
        for i, time in enumerate(times):
            row = QWidget()
            row_layout = QHBoxLayout()
            row_layout.setContentsMargins(0, 0, 0, 0)
            row_layout.setSpacing(0)
            
            time_label = QLabel(time)
            time_label.setFixedWidth(60)
            time_label.setStyleSheet(f"""
                color: {SECONDARY_TEXT};
                font-size: {SMALL_SIZE}px;
            """)
            row_layout.addWidget(time_label)
            
            for j in range(5):
                if i < len(schedule) and j < len(schedule[i]):
                    cell_text = schedule[i][j]
                else:
                    cell_text = "-"
                
                cell = QLabel(cell_text if cell_text != "-" else "")
                cell.setFixedWidth(80)
                cell.setFixedHeight(40)
                cell.setAlignment(Qt.AlignmentFlag.AlignCenter)
                
                if cell_text != "-":
                    cell.setStyleSheet(f"""
                        background-color: {SIDEBAR};
                        color: {PRIMARY_TEXT};
                        font-size: {SMALL_SIZE}px;
                        border-radius: {BUTTON_RADIUS - 4}px;
                    """)
                else:
                    cell.setStyleSheet(f"""
                        color: transparent;
                    """)
                
                row_layout.addWidget(cell)
            
            row.setLayout(row_layout)
            layout.addWidget(row)
        
        self.setLayout(layout)


class TrainingStatsCard(QWidget):
    """Training statistics card"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: {CARD};
            border-radius: {CARD_RADIUS}px;
            padding: {CARD_PADDING}px;
            box-shadow: {SHADOW_MEDIUM};
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(CARD_PADDING)
        
        # Title
        title = QLabel("Training Stats")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Stats
        stats = [
            ("Total Hours", "24h 30m", SUCCESS),
            ("Puzzles Solved", "1,247", INFO),
            ("Games Analyzed", "42", WARNING),
            ("Streak", "12 days", ACCENT)
        ]
        
        for stat_name, stat_value, color in stats:
            stat_row = QWidget()
            stat_row.setFixedHeight(48)
            stat_row.setStyleSheet(f"""
                background-color: transparent;
            """)
            
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


class TrainingPlan(QWidget):
    """Training Plan Page"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: {BACKGROUND};
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(PADDING, PADDING, PADDING, PADDING)
        layout.setSpacing(CARD_PADDING)
        
        # Title
        title = QLabel("Training Plan")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {TITLE_SIZE}px;
            font-weight: 600;
        """)
        
        # Training Modules
        modules_layout = QHBoxLayout()
        modules_layout.setContentsMargins(0, 0, 0, 0)
        modules_layout.setSpacing(CARD_PADDING)
        
        # Module 1
        module1 = TrainingModuleCard(
            "Tactical Training",
            "Solve puzzles to improve your tactical vision and pattern recognition",
            75,
            "45 min/day"
        )
        module1.setMinimumWidth(300)
        
        # Module 2
        module2 = TrainingModuleCard(
            "Opening Preparation",
            "Study and practice your opening repertoire",
            60,
            "30 min/day"
        )
        module2.setMinimumWidth(300)
        
        # Module 3
        module3 = TrainingModuleCard(
            "Endgame Mastery",
            "Learn essential endgame techniques and conversions",
            40,
            "25 min/day"
        )
        module3.setMinimumWidth(300)
        
        modules_layout.addWidget(module1)
        modules_layout.addWidget(module2)
        modules_layout.addWidget(module3)
        modules_layout.addStretch()
        
        # Main Content
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(CARD_PADDING)
        
        # Weekly Schedule
        schedule_card = WeeklyScheduleCard()
        schedule_card.setMinimumWidth(400)
        
        # Training Stats
        stats_card = TrainingStatsCard()
        stats_card.setMinimumWidth(300)
        
        main_layout.addWidget(schedule_card)
        main_layout.addWidget(stats_card)
        main_layout.addStretch()
        
        # Combine all
        layout.addWidget(title)
        layout.addSpacing(8)
        layout.addLayout(modules_layout)
        layout.addSpacing(CARD_PADDING)
        layout.addLayout(main_layout)
        layout.addStretch()
        
        self.setLayout(layout)
