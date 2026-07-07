"""
KnightOS Goals Page
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt

from app.theme import *
from app.ui.icons import (
    CHESS_ICON, CHART_LINE_ICON, CLOCK_ICON,
    CHECK_ICON, ADD_ICON, CALENDAR_ICON
)


class GoalCard(QWidget):
    """Goal card with progress tracking"""
    
    def __init__(self, title, description, progress, target, deadline, status="active", parent=None):
        super().__init__(parent)
        
        status_colors = {
            "active": ACCENT,
            "completed": SUCCESS,
            "overdue": ERROR,
            "abandoned": TERTIARY_TEXT
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
            font-weight: 600;
        """)
        
        header_layout.addWidget(status_indicator)
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        # Deadline
        deadline_label = QLabel(deadline)
        deadline_label.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {CAPTION_SIZE}px;
        """)
        
        header_layout.addWidget(deadline_label)
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
        progress_fill.setFixedWidth(int(progress * 2.5))
        progress_fill.setStyleSheet(f"""
            background: linear-gradient(90deg, {status_colors[status]} 0%, {status_colors[status]} 100%);
            border-radius: 4px;
        """)
        
        progress_layout = QHBoxLayout()
        progress_layout.setContentsMargins(0, 0, 0, 0)
        progress_layout.setSpacing(0)
        progress_layout.addWidget(progress_fill)
        progress_container.setLayout(progress_layout)
        
        # Progress Text
        progress_text = QLabel(f"{int(progress)}% of {target}")
        progress_text.setStyleSheet(f"""
            color: {status_colors[status]};
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


class GoalStatsCard(QWidget):
    """Goal statistics"""
    
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
        title = QLabel("Goal Statistics")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Stats
        stats = [
            ("Total Goals", "12", ACCENT),
            ("Completed", "5", SUCCESS),
            ("In Progress", "4", WARNING),
            ("Success Rate", "41.7%", SUCCESS),
            ("Average Progress", "68%", INFO)
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


class NewGoalCard(QWidget):
    """Create new goal card"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: {CARD};
            border-radius: {CARD_RADIUS}px;
            padding: {CARD_PADDING}px;
            
            border: 2px dashed rgba(200, 155, 60, 0.3);
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(CARD_PADDING)
        
        # Title
        title = QLabel("Create New Goal")
        title.setStyleSheet(f"""
            color: {ACCENT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Description
        desc = QLabel("Set a new training goal to track your progress")
        desc.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {BODY_SIZE - 1}px;
            line-height: 1.6;
        """)
        
        # Create Button
        create_btn = QPushButton("Create Goal")
        create_btn.setFixedHeight(BUTTON_HEIGHT)
        create_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {ACCENT};
                border-radius: {BUTTON_RADIUS}px;
                color: {BACKGROUND};
                font-size: {BODY_SIZE}px;
                font-weight: 600;
            }}
            QPushButton:hover {{
                background-color: {ACCENT_HOVER};
            }}
            QPushButton:pressed {{
                background-color: {ACCENT_PRESSED};
            }}
        """)
        
        layout.addWidget(title)
        layout.addSpacing(8)
        layout.addWidget(desc)
        layout.addSpacing(CARD_PADDING)
        layout.addWidget(create_btn)
        layout.addStretch()
        
        self.setLayout(layout)


class Goals(QWidget):
    """Goals Page"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: {BACKGROUND};
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(PADDING, PADDING, PADDING, PADDING)
        layout.setSpacing(CARD_PADDING)
        
        # Title
        title = QLabel("Training Goals")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {TITLE_SIZE}px;
            font-weight: 600;
        """)
        
        # Goals Grid
        goals_layout = QHBoxLayout()
        goals_layout.setContentsMargins(0, 0, 0, 0)
        goals_layout.setSpacing(CARD_PADDING)
        
        # Row 1
        goal1 = GoalCard(
            "Reach 2200 Rating",
            "Improve my FIDE rating to 2200 by the end of the year",
            65,
            "2200",
            "Dec 31, 2024",
            "active"
        )
        goal1.setMinimumWidth(300)
        
        goal2 = GoalCard(
            "Solve 1000 Puzzles",
            "Complete 1000 tactical puzzles to improve pattern recognition",
            45,
            "1000",
            "Mar 15, 2024",
            "active"
        )
        goal2.setMinimumWidth(300)
        
        goal3 = GoalCard(
            "Master Sicilian Defense",
            "Achieve 90% confidence in Sicilian Defense repertoire",
            85,
            "90%",
            "Feb 28, 2024",
            "active"
        )
        goal3.setMinimumWidth(300)
        
        # Row 2
        goal4 = GoalCard(
            "Win Tournament",
            "Win the upcoming National Open tournament",
            10,
            "1st Place",
            "Apr 1, 2024",
            "active"
        )
        goal4.setMinimumWidth(300)
        
        goal5 = GoalCard(
            "Endgame Mastery",
            "Complete all basic endgame lessons",
            100,
            "100%",
            "Jan 31, 2024",
            "completed"
        )
        goal5.setMinimumWidth(300)
        
        goal6 = NewGoalCard()
        goal6.setMinimumWidth(300)
        
        row1 = QHBoxLayout()
        row1.setContentsMargins(0, 0, 0, 0)
        row1.setSpacing(CARD_PADDING)
        row1.addWidget(goal1)
        row1.addWidget(goal2)
        row1.addWidget(goal3)
        row1.addStretch()
        
        row2 = QHBoxLayout()
        row2.setContentsMargins(0, 0, 0, 0)
        row2.setSpacing(CARD_PADDING)
        row2.addWidget(goal4)
        row2.addWidget(goal5)
        row2.addWidget(goal6)
        row2.addStretch()
        
        # Stats Card
        stats_card = GoalStatsCard()
        stats_card.setMinimumWidth(350)
        
        # Combine all
        layout.addWidget(title)
        layout.addSpacing(8)
        layout.addLayout(row1)
        layout.addSpacing(CARD_PADDING)
        layout.addLayout(row2)
        layout.addSpacing(CARD_PADDING)
        layout.addWidget(stats_card)
        layout.addStretch()
        
        self.setLayout(layout)
