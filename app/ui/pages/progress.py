"""
KnightOS Progress Page - Modern Graphs and Charts
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtCore import Qt

from app.theme import *
from app.ui.icons import (
    CHART_LINE_ICON, CHART_RADAR_ICON, 
    RATING_UP_ICON, CLOCK_ICON
)


class RadarChartWidget(QWidget):
    """Radar chart for chess skills"""
    
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
        title = QLabel("Chess Skills Radar")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Radar chart placeholder
        chart_placeholder = QLabel("Radar Chart Visualization")
        chart_placeholder.setFixedHeight(300)
        chart_placeholder.setStyleSheet(f"""
            background-color: {SIDEBAR};
            border-radius: {BUTTON_RADIUS}px;
            color: {TERTIARY_TEXT};
            font-size: {SMALL_SIZE}px;
        """)
        chart_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Skills legend
        skills = [
            ("Calculation", 85, ACCENT),
            ("Defence", 72, SUCCESS),
            ("Openings", 88, INFO),
            ("Endgames", 75, WARNING),
            ("Strategy", 78, ACCENT)
        ]
        
        legend_layout = QHBoxLayout()
        legend_layout.setContentsMargins(0, 0, 0, 0)
        legend_layout.setSpacing(CARD_PADDING)
        
        for skill_name, skill_value, color in skills:
            skill_container = QWidget()
            skill_layout = QVBoxLayout()
            skill_layout.setContentsMargins(0, 0, 0, 0)
            skill_layout.setSpacing(4)
            
            skill_name_label = QLabel(skill_name)
            skill_name_label.setStyleSheet(f"""
                color: {SECONDARY_TEXT};
                font-size: {CAPTION_SIZE}px;
            """)
            
            skill_value_label = QLabel(f"{skill_value}%")
            skill_value_label.setStyleSheet(f"""
                color: {color};
                font-size: {BODY_SIZE}px;
                font-weight: 600;
            """)
            
            skill_layout.addWidget(skill_name_label)
            skill_layout.addWidget(skill_value_label)
            skill_container.setLayout(skill_layout)
            
            legend_layout.addWidget(skill_container)
        
        legend_layout.addStretch()
        
        layout.addWidget(title)
        layout.addWidget(chart_placeholder)
        layout.addLayout(legend_layout)
        
        self.setLayout(layout)


class RatingGraphWidget(QWidget):
    """Rating progress graph"""
    
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
        title = QLabel("Rating Progress")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Graph placeholder
        graph_placeholder = QLabel("Rating Graph Visualization")
        graph_placeholder.setFixedHeight(250)
        graph_placeholder.setStyleSheet(f"""
            background-color: {SIDEBAR};
            border-radius: {BUTTON_RADIUS}px;
            color: {TERTIARY_TEXT};
            font-size: {SMALL_SIZE}px;
        """)
        graph_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Stats
        stats_layout = QHBoxLayout()
        stats_layout.setContentsMargins(0, 0, 0, 0)
        stats_layout.setSpacing(CARD_PADDING)
        
        # Current Rating
        current_rating = QWidget()
        current_layout = QVBoxLayout()
        current_layout.setContentsMargins(0, 0, 0, 0)
        current_layout.setSpacing(4)
        
        current_value = QLabel("2150")
        current_value.setStyleSheet(f"""
            color: {ACCENT};
            font-size: {TITLE_SIZE - 6}px;
            font-weight: bold;
        """)
        
        current_label = QLabel("Current Rating")
        current_label.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {CAPTION_SIZE}px;
        """)
        
        current_layout.addWidget(current_value)
        current_layout.addWidget(current_label)
        current_rating.setLayout(current_layout)
        
        # Peak Rating
        peak_rating = QWidget()
        peak_layout = QVBoxLayout()
        peak_layout.setContentsMargins(0, 0, 0, 0)
        peak_layout.setSpacing(4)
        
        peak_value = QLabel("2245")
        peak_value.setStyleSheet(f"""
            color: {SUCCESS};
            font-size: {TITLE_SIZE - 6}px;
            font-weight: bold;
        """)
        
        peak_label = QLabel("Peak Rating")
        peak_label.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {CAPTION_SIZE}px;
        """)
        
        peak_layout.addWidget(peak_value)
        peak_layout.addWidget(peak_label)
        peak_rating.setLayout(peak_layout)
        
        # Monthly Change
        monthly_change = QWidget()
        monthly_layout = QVBoxLayout()
        monthly_layout.setContentsMargins(0, 0, 0, 0)
        monthly_layout.setSpacing(4)
        
        monthly_value = QLabel("+42")
        monthly_value.setStyleSheet(f"""
            color: {SUCCESS};
            font-size: {TITLE_SIZE - 6}px;
            font-weight: bold;
        """)
        
        monthly_label = QLabel("This Month")
        monthly_label.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {CAPTION_SIZE}px;
        """)
        
        monthly_layout.addWidget(monthly_value)
        monthly_layout.addWidget(monthly_label)
        monthly_change.setLayout(monthly_layout)
        
        stats_layout.addWidget(current_rating)
        stats_layout.addWidget(peak_rating)
        stats_layout.addWidget(monthly_change)
        stats_layout.addStretch()
        
        layout.addWidget(title)
        layout.addWidget(graph_placeholder)
        layout.addLayout(stats_layout)
        
        self.setLayout(layout)


class TrainingStreakWidget(QWidget):
    """Training streak display"""
    
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
        title = QLabel("Training Streak")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Streak Display
        streak_display = QWidget()
        streak_layout = QHBoxLayout()
        streak_layout.setContentsMargins(0, 0, 0, 0)
        streak_layout.setSpacing(CARD_PADDING)
        streak_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        # Streak Number
        streak_number = QLabel("12")
        streak_number.setStyleSheet(f"""
            color: {ACCENT};
            font-size: {TITLE_SIZE}px;
            font-weight: bold;
        """)
        
        # Days Label
        days_label = QLabel("days")
        days_label.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {HEADING_SIZE}px;
        """)
        
        streak_layout.addWidget(streak_number)
        streak_layout.addWidget(days_label)
        streak_display.setLayout(streak_layout)
        
        # Streak Info
        streak_info = QLabel("Keep your streak going! Train today to maintain your progress.")
        streak_info.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {BODY_SIZE - 1}px;
            line-height: 1.6;
        """)
        
        # Progress Bar
        progress_container = QWidget()
        progress_container.setFixedHeight(8)
        progress_container.setStyleSheet(f"""
            background-color: {SIDEBAR};
            border-radius: 4px;
        """)
        
        progress_fill = QWidget()
        progress_fill.setFixedHeight(8)
        progress_fill.setFixedWidth(200)
        progress_fill.setStyleSheet(f"""
            background: linear-gradient(90deg, {SUCCESS} 0%, {SUCCESS} 100%);
            border-radius: 4px;
        """)
        
        progress_layout = QHBoxLayout()
        progress_layout.setContentsMargins(0, 0, 0, 0)
        progress_layout.setSpacing(0)
        progress_layout.addWidget(progress_fill)
        progress_container.setLayout(progress_layout)
        
        layout.addWidget(title)
        layout.addWidget(streak_display)
        layout.addSpacing(8)
        layout.addWidget(streak_info)
        layout.addSpacing(CARD_PADDING)
        layout.addWidget(progress_container)
        
        self.setLayout(layout)


class ProgressStatsCard(QWidget):
    """Additional progress statistics"""
    
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
        title = QLabel("Progress Metrics")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Stats
        stats = [
            ("Puzzles Solved", "1,247", ACCENT),
            ("Games Analyzed", "247", INFO),
            ("Training Hours", "89h 30m", WARNING),
            ("Improvement", "+245", SUCCESS),
            ("Consistency", "92%", SUCCESS)
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


class Progress(QWidget):
    """Progress Page - Modern graphs and statistics"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: {BACKGROUND};
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(PADDING, PADDING, PADDING, PADDING)
        layout.setSpacing(CARD_PADDING)
        
        # Title
        title = QLabel("Progress Tracking")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {TITLE_SIZE}px;
            font-weight: 600;
        """)
        
        # Top Row - Rating Graph and Radar Chart
        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0, 0, 0, 0)
        top_layout.setSpacing(CARD_PADDING)
        
        rating_graph = RatingGraphWidget()
        rating_graph.setMinimumWidth(450)
        
        radar_chart = RadarChartWidget()
        radar_chart.setMinimumWidth(400)
        
        top_layout.addWidget(rating_graph)
        top_layout.addWidget(radar_chart)
        top_layout.addStretch()
        
        # Bottom Row - Training Streak and Progress Stats
        bottom_layout = QHBoxLayout()
        bottom_layout.setContentsMargins(0, 0, 0, 0)
        bottom_layout.setSpacing(CARD_PADDING)
        
        streak_widget = TrainingStreakWidget()
        streak_widget.setMinimumWidth(350)
        
        progress_stats = ProgressStatsCard()
        progress_stats.setMinimumWidth(350)
        
        bottom_layout.addWidget(streak_widget)
        bottom_layout.addWidget(progress_stats)
        bottom_layout.addStretch()
        
        # Combine all
        layout.addWidget(title)
        layout.addSpacing(8)
        layout.addLayout(top_layout)
        layout.addSpacing(CARD_PADDING)
        layout.addLayout(bottom_layout)
        layout.addStretch()
        
        self.setLayout(layout)
