"""
KnightOS Puzzles Page
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt

from app.theme import *
from app.ui.icons import (
    CHESS_ICON, CHART_LINE_ICON, CLOCK_ICON,
    CHECK_ICON, CLOSE_ICON, ADD_ICON
)


class PuzzleCard(QWidget):
    """Puzzle card with difficulty and status"""
    
    def __init__(self, puzzle_id, difficulty, theme, status="unsolved", parent=None):
        super().__init__(parent)
        
        difficulty_colors = {
            "Easy": SUCCESS,
            "Medium": WARNING,
            "Hard": ERROR,
            "Master": ACCENT
        }
        
        status_colors = {
            "solved": SUCCESS,
            "unsolved": SECONDARY_TEXT,
            "failed": ERROR,
            "skipped": TERTIARY_TEXT
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
        
        # Puzzle ID
        id_label = QLabel(f"#{puzzle_id}")
        id_label.setStyleSheet(f"""
            color: {TERTIARY_TEXT};
            font-size: {CAPTION_SIZE}px;
            font-family: monospace;
        """)
        
        # Difficulty Badge
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
        
        header_layout.addWidget(id_label)
        header_layout.addStretch()
        header_layout.addWidget(difficulty_badge)
        header.setLayout(header_layout)
        
        # Theme
        theme_label = QLabel(theme)
        theme_label.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {BODY_SIZE + 1}px;
            font-weight: 500;
        """)
        
        # Status
        status_label = QLabel()
        status_text = {
            "solved": "✓ Solved",
            "unsolved": "• Unsolved",
            "failed": "✗ Failed",
            "skipped": "» Skipped"
        }
        status_color = status_colors.get(status, SECONDARY_TEXT)
        status_label.setText(status_text.get(status, ""))
        status_label.setStyleSheet(f"""
            color: {status_color};
            font-size: {SMALL_SIZE}px;
        """)
        
        # Board placeholder
        board_placeholder = QLabel("Puzzle Position")
        board_placeholder.setFixedHeight(100)
        board_placeholder.setStyleSheet(f"""
            background-color: {SIDEBAR};
            border-radius: {BUTTON_RADIUS}px;
            color: {TERTIARY_TEXT};
            font-size: {SMALL_SIZE}px;
        """)
        board_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(header)
        layout.addSpacing(4)
        layout.addWidget(theme_label)
        layout.addSpacing(8)
        layout.addWidget(board_placeholder)
        layout.addSpacing(8)
        layout.addWidget(status_label)
        
        self.setLayout(layout)


class PuzzleStatsCard(QWidget):
    """Puzzle statistics"""
    
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
        title = QLabel("Puzzle Statistics")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Stats
        stats = [
            ("Total Puzzles", "1,247", ACCENT),
            ("Solved", "989", SUCCESS),
            ("Success Rate", "79.3%", SUCCESS),
            ("Current Streak", "12", WARNING),
            ("Best Streak", "24", ACCENT)
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


class PuzzleThemesCard(QWidget):
    """Puzzle themes overview"""
    
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
        title = QLabel("Puzzle Themes")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Themes
        themes = [
            ("Fork", 124, 85),
            ("Pin", 98, 78),
            ("Skewer", 76, 72),
            ("Discovered Attack", 65, 68),
            ("Deflection", 89, 80),
            ("Interference", 54, 60)
        ]
        
        for theme_name, theme_count, theme_progress in themes:
            theme_row = QWidget()
            theme_row.setFixedHeight(40)
            
            theme_layout = QHBoxLayout()
            theme_layout.setContentsMargins(0, 0, 0, 0)
            theme_layout.setSpacing(SMALL_PADDING)
            theme_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            
            name_label = QLabel(theme_name)
            name_label.setStyleSheet(f"""
                color: {PRIMARY_TEXT};
                font-size: {BODY_SIZE - 1}px;
            """)
            name_label.setFixedWidth(120)
            
            # Progress bar
            progress_container = QWidget()
            progress_container.setFixedHeight(4)
            progress_container.setFixedWidth(100)
            progress_container.setStyleSheet(f"""
                background-color: {SIDEBAR};
                border-radius: 2px;
            """)
            
            progress_fill = QWidget()
            progress_fill.setFixedHeight(4)
            progress_fill.setFixedWidth(int(theme_progress * 1.0))
            progress_fill.setStyleSheet(f"""
                background: linear-gradient(90deg, {ACCENT} 0%, {ACCENT_HOVER} 100%);
                border-radius: 2px;
            """)
            
            progress_layout = QHBoxLayout()
            progress_layout.setContentsMargins(0, 0, 0, 0)
            progress_layout.setSpacing(0)
            progress_layout.addWidget(progress_fill)
            progress_container.setLayout(progress_layout)
            
            count_label = QLabel(f"{theme_count}")
            count_label.setStyleSheet(f"""
                color: {SECONDARY_TEXT};
                font-size: {CAPTION_SIZE}px;
            """)
            
            theme_layout.addWidget(name_label)
            theme_layout.addWidget(progress_container)
            theme_layout.addStretch()
            theme_layout.addWidget(count_label)
            
            theme_row.setLayout(theme_layout)
            layout.addWidget(theme_row)
        
        layout.addWidget(title)
        for theme_name, theme_count, theme_progress in themes:
            theme_row = QWidget()
            theme_row.setFixedHeight(40)
            
            theme_layout = QHBoxLayout()
            theme_layout.setContentsMargins(0, 0, 0, 0)
            theme_layout.setSpacing(SMALL_PADDING)
            theme_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            
            name_label = QLabel(theme_name)
            name_label.setStyleSheet(f"""
                color: {PRIMARY_TEXT};
                font-size: {BODY_SIZE - 1}px;
            """)
            name_label.setFixedWidth(120)
            
            progress_container = QWidget()
            progress_container.setFixedHeight(4)
            progress_container.setFixedWidth(100)
            progress_container.setStyleSheet(f"""
                background-color: {SIDEBAR};
                border-radius: 2px;
            """)
            
            progress_fill = QWidget()
            progress_fill.setFixedHeight(4)
            progress_fill.setFixedWidth(int(theme_progress * 1.0))
            progress_fill.setStyleSheet(f"""
                background: linear-gradient(90deg, {ACCENT} 0%, {ACCENT_HOVER} 100%);
                border-radius: 2px;
            """)
            
            progress_layout = QHBoxLayout()
            progress_layout.setContentsMargins(0, 0, 0, 0)
            progress_layout.setSpacing(0)
            progress_layout.addWidget(progress_fill)
            progress_container.setLayout(progress_layout)
            
            count_label = QLabel(f"{theme_count}")
            count_label.setStyleSheet(f"""
                color: {SECONDARY_TEXT};
                font-size: {CAPTION_SIZE}px;
            """)
            
            theme_layout.addWidget(name_label)
            theme_layout.addWidget(progress_container)
            theme_layout.addStretch()
            theme_layout.addWidget(count_label)
            
            theme_row.setLayout(theme_layout)
            layout.addWidget(theme_row)
        
        self.setLayout(layout)


class Puzzles(QWidget):
    """Puzzles Page"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: {BACKGROUND};
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(PADDING, PADDING, PADDING, PADDING)
        layout.setSpacing(CARD_PADDING)
        
        # Title
        title = QLabel("Tactical Puzzles")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {TITLE_SIZE}px;
            font-weight: 600;
        """)
        
        # Puzzles Grid
        puzzles_layout = QHBoxLayout()
        puzzles_layout.setContentsMargins(0, 0, 0, 0)
        puzzles_layout.setSpacing(CARD_PADDING)
        
        # Row 1
        puzzle1 = PuzzleCard(12345, "Medium", "Fork", "solved")
        puzzle1.setMinimumWidth(250)
        
        puzzle2 = PuzzleCard(12346, "Hard", "Pin", "unsolved")
        puzzle2.setMinimumWidth(250)
        
        puzzle3 = PuzzleCard(12347, "Easy", "Skewer", "solved")
        puzzle3.setMinimumWidth(250)
        
        puzzle4 = PuzzleCard(12348, "Master", "Deflection", "unsolved")
        puzzle4.setMinimumWidth(250)
        
        # Row 2
        puzzle5 = PuzzleCard(12349, "Medium", "Discovered Attack", "failed")
        puzzle5.setMinimumWidth(250)
        
        puzzle6 = PuzzleCard(12350, "Hard", "Interference", "unsolved")
        puzzle6.setMinimumWidth(250)
        
        puzzle7 = PuzzleCard(12351, "Easy", "Double Attack", "solved")
        puzzle7.setMinimumWidth(250)
        
        puzzle8 = PuzzleCard(12352, "Medium", "Zugzwang", "unsolved")
        puzzle8.setMinimumWidth(250)
        
        row1 = QHBoxLayout()
        row1.setContentsMargins(0, 0, 0, 0)
        row1.setSpacing(CARD_PADDING)
        row1.addWidget(puzzle1)
        row1.addWidget(puzzle2)
        row1.addWidget(puzzle3)
        row1.addWidget(puzzle4)
        row1.addStretch()
        
        row2 = QHBoxLayout()
        row2.setContentsMargins(0, 0, 0, 0)
        row2.setSpacing(CARD_PADDING)
        row2.addWidget(puzzle5)
        row2.addWidget(puzzle6)
        row2.addWidget(puzzle7)
        row2.addWidget(puzzle8)
        row2.addStretch()
        
        # Stats and Themes
        stats_layout = QHBoxLayout()
        stats_layout.setContentsMargins(0, 0, 0, 0)
        stats_layout.setSpacing(CARD_PADDING)
        
        stats_card = PuzzleStatsCard()
        stats_card.setMinimumWidth(300)
        
        themes_card = PuzzleThemesCard()
        themes_card.setMinimumWidth(350)
        
        stats_layout.addWidget(stats_card)
        stats_layout.addWidget(themes_card)
        stats_layout.addStretch()
        
        # Combine all
        layout.addWidget(title)
        layout.addSpacing(8)
        layout.addLayout(row1)
        layout.addSpacing(CARD_PADDING)
        layout.addLayout(row2)
        layout.addSpacing(CARD_PADDING)
        layout.addLayout(stats_layout)
        layout.addStretch()
        
        self.setLayout(layout)
