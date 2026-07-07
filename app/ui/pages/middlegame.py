"""
KnightOS Middlegame Page
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtCore import Qt

from app.theme import *
from app.ui.icons import CHESS_ICON, CHART_LINE_ICON


class MiddlegameThemeCard(QWidget):
    """Middlegame theme card"""
    
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


class MiddlegameExerciseCard(QWidget):
    """Middlegame exercise card"""
    
    def __init__(self, title, difficulty, parent=None):
        super().__init__(parent)
        
        difficulty_colors = {
            "Easy": SUCCESS,
            "Medium": WARNING,
            "Hard": ERROR,
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
        
        # Exercise preview
        preview_label = QLabel("Solve the position")
        preview_label.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {SMALL_SIZE}px;
        """)
        
        layout.addWidget(header)
        layout.addSpacing(8)
        layout.addWidget(preview_label)
        layout.addStretch()
        
        self.setLayout(layout)


class MiddlegameStatsCard(QWidget):
    """Middlegame statistics"""
    
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
        title = QLabel("Middlegame Skills")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Skills
        skills = [
            ("Calculation", 85, ACCENT),
            ("Tactical Vision", 78, SUCCESS),
            ("Positional Play", 72, WARNING),
            ("Pattern Recognition", 88, SUCCESS),
            ("Planning", 75, ACCENT)
        ]
        
        for skill_name, skill_value, color in skills:
            skill_row = QWidget()
            skill_row.setFixedHeight(48)
            
            skill_layout = QHBoxLayout()
            skill_layout.setContentsMargins(0, 0, 0, 0)
            skill_layout.setSpacing(SMALL_PADDING)
            skill_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            
            name_label = QLabel(skill_name)
            name_label.setStyleSheet(f"""
                color: {SECONDARY_TEXT};
                font-size: {BODY_SIZE - 1}px;
            """)
            
            value_label = QLabel(f"{skill_value}%")
            value_label.setStyleSheet(f"""
                color: {color};
                font-size: {BODY_SIZE + 1}px;
                font-weight: 600;
            """)
            
            skill_layout.addWidget(name_label)
            skill_layout.addStretch()
            skill_layout.addWidget(value_label)
            
            skill_row.setLayout(skill_layout)
            layout.addWidget(skill_row)
        
        layout.addWidget(title)
        for skill_name, skill_value, color in skills:
            skill_row = QWidget()
            skill_row.setFixedHeight(48)
            
            skill_layout = QHBoxLayout()
            skill_layout.setContentsMargins(0, 0, 0, 0)
            skill_layout.setSpacing(SMALL_PADDING)
            skill_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            
            name_label = QLabel(skill_name)
            name_label.setStyleSheet(f"""
                color: {SECONDARY_TEXT};
                font-size: {BODY_SIZE - 1}px;
            """)
            
            value_label = QLabel(f"{skill_value}%")
            value_label.setStyleSheet(f"""
                color: {color};
                font-size: {BODY_SIZE + 1}px;
                font-weight: 600;
            """)
            
            skill_layout.addWidget(name_label)
            skill_layout.addStretch()
            skill_layout.addWidget(value_label)
            
            skill_row.setLayout(skill_layout)
            layout.addWidget(skill_row)
        
        self.setLayout(layout)


class Middlegame(QWidget):
    """Middlegame Page"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: {BACKGROUND};
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(PADDING, PADDING, PADDING, PADDING)
        layout.setSpacing(CARD_PADDING)
        
        # Title
        title = QLabel("Middlegame Training")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {TITLE_SIZE}px;
            font-weight: 600;
        """)
        
        # Themes Grid
        themes_layout = QHBoxLayout()
        themes_layout.setContentsMargins(0, 0, 0, 0)
        themes_layout.setSpacing(CARD_PADDING)
        
        theme1 = MiddlegameThemeCard(
            "Attacking Play",
            "Learn to launch and coordinate attacks against the opponent's position",
            80
        )
        theme1.setMinimumWidth(280)
        
        theme2 = MiddlegameThemeCard(
            "Defensive Techniques",
            "Master the art of defending and counter-attacking",
            65
        )
        theme2.setMinimumWidth(280)
        
        theme3 = MiddlegameThemeCard(
            "Piece Coordination",
            "Improve your ability to coordinate pieces for maximum effect",
            75
        )
        theme3.setMinimumWidth(280)
        
        themes_layout.addWidget(theme1)
        themes_layout.addWidget(theme2)
        themes_layout.addWidget(theme3)
        themes_layout.addStretch()
        
        # Exercises Grid
        exercises_layout = QHBoxLayout()
        exercises_layout.setContentsMargins(0, 0, 0, 0)
        exercises_layout.setSpacing(CARD_PADDING)
        
        exercise1 = MiddlegameExerciseCard("Tactical Strike", "Medium")
        exercise1.setMinimumWidth(280)
        
        exercise2 = MiddlegameExerciseCard("Positional Mastery", "Hard")
        exercise2.setMinimumWidth(280)
        
        exercise3 = MiddlegameExerciseCard("Calculation Puzzle", "Easy")
        exercise3.setMinimumWidth(280)
        
        exercises_layout.addWidget(exercise1)
        exercises_layout.addWidget(exercise2)
        exercises_layout.addWidget(exercise3)
        exercises_layout.addStretch()
        
        # Stats Card
        stats_card = MiddlegameStatsCard()
        stats_card.setMinimumWidth(350)
        
        # Combine all
        layout.addWidget(title)
        layout.addSpacing(8)
        layout.addLayout(themes_layout)
        layout.addSpacing(CARD_PADDING)
        layout.addLayout(exercises_layout)
        layout.addSpacing(CARD_PADDING)
        layout.addWidget(stats_card)
        layout.addStretch()
        
        self.setLayout(layout)
