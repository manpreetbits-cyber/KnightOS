"""
KnightOS AI Coach Page - Personal Chess Coach
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PySide6.QtCore import Qt

from app.theme import *
from app.ui.icons import (
    CHESS_ICON, AI_COACH_ICON, CHART_RADAR_ICON,
    RATING_UP_ICON, CLOCK_ICON
)


class CoachRecommendationPanel(QWidget):
    """Large AI coach recommendation panel"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background: linear-gradient(135deg, {CARD} 0%, {CARD_HOVER} 100%);
            border-radius: {CARD_RADIUS}px;
            padding: {CARD_PADDING + 8}px;
            box-shadow: {SHADOW_LARGE};
            border: 1px solid rgba(200, 155, 60, 0.3);
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(CARD_PADDING)
        
        # Header
        header = QWidget()
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(SMALL_PADDING)
        header_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        icon_label = QLabel()
        icon_label.setPixmap(self._create_icon(AI_COACH_ICON, 32, 32, ACCENT))
        icon_label.setFixedSize(32, 32)
        
        title = QLabel("Your Personal Coach")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 4}px;
            font-weight: 600;
        """)
        
        header_layout.addWidget(icon_label)
        header_layout.addWidget(title)
        header_layout.addStretch()
        header.setLayout(header_layout)
        
        # Recommendation
        recommendation = QLabel("Your tactical vision has improved significantly. Today's priority should be defending worse positions and converting small advantages. Focus on endgame precision.")
        recommendation.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {BODY_SIZE + 1}px;
            line-height: 1.8;
        """)
        recommendation.setWordWrap(True)
        
        # Coach Stats
        coach_stats = QWidget()
        coach_stats_layout = QHBoxLayout()
        coach_stats_layout.setContentsMargins(0, 0, 0, 0)
        coach_stats_layout.setSpacing(CARD_PADDING)
        
        # Stat 1
        stat1 = QWidget()
        stat1_layout = QVBoxLayout()
        stat1_layout.setContentsMargins(0, 0, 0, 0)
        stat1_layout.setSpacing(4)
        
        stat1_value = QLabel("247")
        stat1_value.setStyleSheet(f"""
            color: {ACCENT};
            font-size: {TITLE_SIZE - 8}px;
            font-weight: bold;
        """)
        
        stat1_label = QLabel("Games Analyzed")
        stat1_label.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {CAPTION_SIZE}px;
        """)
        
        stat1_layout.addWidget(stat1_value)
        stat1_layout.addWidget(stat1_label)
        stat1.setLayout(stat1_layout)
        
        # Stat 2
        stat2 = QWidget()
        stat2_layout = QVBoxLayout()
        stat2_layout.setContentsMargins(0, 0, 0, 0)
        stat2_layout.setSpacing(4)
        
        stat2_value = QLabel("89%")
        stat2_value.setStyleSheet(f"""
            color: {SUCCESS};
            font-size: {TITLE_SIZE - 8}px;
            font-weight: bold;
        """)
        
        stat2_label = QLabel("Accuracy")
        stat2_label.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {CAPTION_SIZE}px;
        """)
        
        stat2_layout.addWidget(stat2_value)
        stat2_layout.addWidget(stat2_label)
        stat2.setLayout(stat2_layout)
        
        # Stat 3
        stat3 = QWidget()
        stat3_layout = QVBoxLayout()
        stat3_layout.setContentsMargins(0, 0, 0, 0)
        stat3_layout.setSpacing(4)
        
        stat3_value = QLabel("12")
        stat3_value.setStyleSheet(f"""
            color: {WARNING};
            font-size: {TITLE_SIZE - 8}px;
            font-weight: bold;
        """)
        
        stat3_label = QLabel("Improvement Areas")
        stat3_label.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {CAPTION_SIZE}px;
        """)
        
        stat3_layout.addWidget(stat3_value)
        stat3_layout.addWidget(stat3_label)
        stat3.setLayout(stat3_layout)
        
        coach_stats_layout.addWidget(stat1)
        coach_stats_layout.addWidget(stat2)
        coach_stats_layout.addWidget(stat3)
        coach_stats_layout.addStretch()
        coach_stats.setLayout(coach_stats_layout)
        
        layout.addWidget(header)
        layout.addSpacing(8)
        layout.addWidget(recommendation)
        layout.addSpacing(CARD_PADDING)
        layout.addWidget(coach_stats)
        
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


class CoachInputCard(QWidget):
    """Ask your coach input card"""
    
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
        title = QLabel("Ask Your Coach")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Input Field
        input_container = QWidget()
        input_container.setFixedHeight(INPUT_HEIGHT)
        input_container.setStyleSheet(f"""
            background-color: {SIDEBAR};
            border-radius: {INPUT_RADIUS}px;
            padding: 0 {INPUT_PADDING}px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        """)
        
        input_layout = QHBoxLayout()
        input_layout.setContentsMargins(0, 0, 0, 0)
        input_layout.setSpacing(SMALL_PADDING)
        input_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        input_field = QLineEdit()
        input_field.setPlaceholderText("Ask your coach about openings, strategy, or game analysis...")
        input_field.setStyleSheet(f"""
            QLineEdit {{
                background: transparent;
                border: none;
                color: {PRIMARY_TEXT};
                font-size: {BODY_SIZE}px;
                padding: 0;
            }}
            QLineEdit::placeholder {{
                color: {SECONDARY_TEXT};
            }}
        """)
        
        # Send Button
        send_btn = QPushButton("Send")
        send_btn.setFixedHeight(36)
        send_btn.setFixedWidth(80)
        send_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {ACCENT};
                border-radius: {BUTTON_RADIUS - 4}px;
                color: {BACKGROUND};
                font-size: {BODY_SIZE - 1}px;
                font-weight: 600;
            }}
            QPushButton:hover {{
                background-color: {ACCENT_HOVER};
            }}
            QPushButton:pressed {{
                background-color: {ACCENT_PRESSED};
            }}
        """)
        
        input_layout.addWidget(input_field)
        input_layout.addWidget(send_btn)
        input_container.setLayout(input_layout)
        
        # Suggested Questions
        suggestions = [
            "How can I improve my opening repertoire?",
            "What are my biggest weaknesses?",
            "Analyze my last game",
            "Suggest a training plan for this week"
        ]
        
        suggestions_layout = QVBoxLayout()
        suggestions_layout.setContentsMargins(0, 0, 0, 0)
        suggestions_layout.setSpacing(SMALL_PADDING)
        
        for suggestion in suggestions:
            suggestion_btn = QPushButton(suggestion)
            suggestion_btn.setFixedHeight(40)
            suggestion_btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: transparent;
                    border-radius: {BUTTON_RADIUS - 4}px;
                    color: {SECONDARY_TEXT};
                    font-size: {BODY_SIZE - 1}px;
                    padding: 0 {SMALL_PADDING}px;
                    text-align: left;
                    border: 1px solid rgba(255, 255, 255, 0.05);
                }}
                QPushButton:hover {{
                    background-color: {SIDEBAR};
                    color: {PRIMARY_TEXT};
                    border-color: rgba(255, 255, 255, 0.1);
                }}
            """)
            suggestions_layout.addWidget(suggestion_btn)
        
        layout.addWidget(title)
        layout.addWidget(input_container)
        layout.addSpacing(CARD_PADDING)
        layout.addLayout(suggestions_layout)
        
        self.setLayout(layout)


class ImprovementAreasCard(QWidget):
    """Areas for improvement"""
    
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
        title = QLabel("Focus Areas")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Improvement areas
        areas = [
            ("Defending Worse Positions", 65, "Your ability to hold difficult positions needs work"),
            ("Endgame Conversion", 72, "Practice converting small advantages in endgames"),
            ("Opening Preparation", 85, "Good knowledge but could be deeper"),
            ("Tactical Vision", 88, "Strong but always room for improvement"),
            ("Time Management", 58, "Focus on using your clock more efficiently")
        ]
        
        for area_name, area_score, area_desc in areas:
            area_row = QWidget()
            area_row.setFixedHeight(60)
            area_row.setStyleSheet(f"""
                background-color: transparent;
                border-radius: {BUTTON_RADIUS}px;
            """)
            
            area_layout = QVBoxLayout()
            area_layout.setContentsMargins(0, 0, 0, 0)
            area_layout.setSpacing(4)
            
            # Header
            header = QWidget()
            header_layout = QHBoxLayout()
            header_layout.setContentsMargins(0, 0, 0, 0)
            header_layout.setSpacing(SMALL_PADDING)
            header_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            
            name_label = QLabel(area_name)
            name_label.setStyleSheet(f"""
                color: {PRIMARY_TEXT};
                font-size: {BODY_SIZE}px;
                font-weight: 500;
            """)
            
            score_label = QLabel(f"{area_score}%")
            score_color = SUCCESS if area_score >= 80 else WARNING if area_score >= 60 else ERROR
            score_label.setStyleSheet(f"""
                color: {score_color};
                font-size: {BODY_SIZE}px;
                font-weight: 600;
            """)
            
            header_layout.addWidget(name_label)
            header_layout.addStretch()
            header_layout.addWidget(score_label)
            header.setLayout(header_layout)
            
            # Description
            desc_label = QLabel(area_desc)
            desc_label.setStyleSheet(f"""
                color: {SECONDARY_TEXT};
                font-size: {CAPTION_SIZE}px;
            """)
            
            area_layout.addWidget(header)
            area_layout.addWidget(desc_label)
            area_row.setLayout(area_layout)
            
            layout.addWidget(area_row)
        
        layout.addWidget(title)
        for area_name, area_score, area_desc in areas:
            area_row = QWidget()
            area_row.setFixedHeight(60)
            
            area_layout = QVBoxLayout()
            area_layout.setContentsMargins(0, 0, 0, 0)
            area_layout.setSpacing(4)
            
            header = QWidget()
            header_layout = QHBoxLayout()
            header_layout.setContentsMargins(0, 0, 0, 0)
            header_layout.setSpacing(SMALL_PADDING)
            header_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            
            name_label = QLabel(area_name)
            name_label.setStyleSheet(f"""
                color: {PRIMARY_TEXT};
                font-size: {BODY_SIZE}px;
                font-weight: 500;
            """)
            
            score_label = QLabel(f"{area_score}%")
            score_color = SUCCESS if area_score >= 80 else WARNING if area_score >= 60 else ERROR
            score_label.setStyleSheet(f"""
                color: {score_color};
                font-size: {BODY_SIZE}px;
                font-weight: 600;
            """)
            
            header_layout.addWidget(name_label)
            header_layout.addStretch()
            header_layout.addWidget(score_label)
            header.setLayout(header_layout)
            
            desc_label = QLabel(area_desc)
            desc_label.setStyleSheet(f"""
                color: {SECONDARY_TEXT};
                font-size: {CAPTION_SIZE}px;
            """)
            
            area_layout.addWidget(header)
            area_layout.addWidget(desc_label)
            area_row.setLayout(area_layout)
            
            layout.addWidget(area_row)
        
        self.setLayout(layout)


class AICoach(QWidget):
    """AI Coach Page - Personal chess coach"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: {BACKGROUND};
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(PADDING, PADDING, PADDING, PADDING)
        layout.setSpacing(CARD_PADDING)
        
        # Title
        title = QLabel("AI Coach")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {TITLE_SIZE}px;
            font-weight: 600;
        """)
        
        # Main Recommendation Panel
        recommendation_panel = CoachRecommendationPanel()
        recommendation_panel.setMinimumWidth(600)
        
        # Input and Improvement Areas
        bottom_layout = QHBoxLayout()
        bottom_layout.setContentsMargins(0, 0, 0, 0)
        bottom_layout.setSpacing(CARD_PADDING)
        
        input_card = CoachInputCard()
        input_card.setMinimumWidth(400)
        
        improvement_card = ImprovementAreasCard()
        improvement_card.setMinimumWidth(350)
        
        bottom_layout.addWidget(input_card)
        bottom_layout.addWidget(improvement_card)
        bottom_layout.addStretch()
        
        # Combine all
        layout.addWidget(title)
        layout.addSpacing(8)
        layout.addWidget(recommendation_panel)
        layout.addSpacing(CARD_PADDING)
        layout.addLayout(bottom_layout)
        layout.addStretch()
        
        self.setLayout(layout)
