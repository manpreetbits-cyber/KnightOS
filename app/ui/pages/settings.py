"""
KnightOS Settings Page
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QSlider
from PySide6.QtCore import Qt

from app.theme import *
from app.ui.icons import (
    SETTINGS_ICON, USER_ICON, CHESS_ICON,
    CHART_LINE_ICON, CLOCK_ICON
)


class SettingsSection(QWidget):
    """Settings section with title and options"""
    
    def __init__(self, title, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: transparent;
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(SMALL_PADDING)
        
        # Section Title
        title_label = QLabel(title)
        title_label.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE}px;
            font-weight: 600;
        """)
        
        # Section Divider
        divider = QWidget()
        divider.setFixedHeight(1)
        divider.setStyleSheet(f"""
            background-color: rgba(255, 255, 255, 0.1);
        """)
        
        layout.addWidget(title_label)
        layout.addWidget(divider)
        
        self.setLayout(layout)


class SettingsItem(QWidget):
    """Individual settings item"""
    
    def __init__(self, label, value_widget, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: transparent;
        """)
        
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(SMALL_PADDING)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        # Label
        label_widget = QLabel(label)
        label_widget.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {BODY_SIZE}px;
        """)
        
        layout.addWidget(label_widget)
        layout.addStretch()
        layout.addWidget(value_widget)
        
        self.setLayout(layout)


class ProfileSettingsCard(QWidget):
    """Profile settings card"""
    
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
        title = QLabel("Profile Settings")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Profile Info
        profile_layout = QVBoxLayout()
        profile_layout.setContentsMargins(0, 0, 0, 0)
        profile_layout.setSpacing(SMALL_PADDING)
        
        # Avatar
        avatar_container = QWidget()
        avatar_layout = QHBoxLayout()
        avatar_layout.setContentsMargins(0, 0, 0, 0)
        avatar_layout.setSpacing(SMALL_PADDING)
        avatar_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        avatar_label = QLabel()
        avatar_label.setFixedSize(AVATAR_LARGE, AVATAR_LARGE)
        avatar_label.setStyleSheet(f"""
            background-color: {ACCENT};
            border-radius: {AVATAR_RADIUS}px;
            color: {BACKGROUND};
            font-weight: bold;
            font-size: {TITLE_SIZE}px;
            display: flex;
            align-items: center;
            justify-content: center;
        """)
        avatar_label.setText("S")
        avatar_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        name_label = QLabel("Shehzaad")
        name_label.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        avatar_layout.addWidget(avatar_label)
        avatar_layout.addWidget(name_label)
        avatar_layout.addStretch()
        
        # Edit Button
        edit_btn = QPushButton("Edit Profile")
        edit_btn.setFixedHeight(36)
        edit_btn.setStyleSheet(f"""
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
        """)
        
        avatar_layout.addWidget(edit_btn)
        avatar_container.setLayout(avatar_layout)
        
        # Stats
        stats_layout = QHBoxLayout()
        stats_layout.setContentsMargins(0, 0, 0, 0)
        stats_layout.setSpacing(CARD_PADDING)
        
        # Rating
        rating_container = QWidget()
        rating_layout = QVBoxLayout()
        rating_layout.setContentsMargins(0, 0, 0, 0)
        rating_layout.setSpacing(4)
        
        rating_value = QLabel("2150")
        rating_value.setStyleSheet(f"""
            color: {ACCENT};
            font-size: {TITLE_SIZE - 4}px;
            font-weight: bold;
        """)
        
        rating_label = QLabel("Current Rating")
        rating_label.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {CAPTION_SIZE}px;
        """)
        
        rating_layout.addWidget(rating_value)
        rating_layout.addWidget(rating_label)
        rating_container.setLayout(rating_layout)
        
        # Games
        games_container = QWidget()
        games_layout = QVBoxLayout()
        games_layout.setContentsMargins(0, 0, 0, 0)
        games_layout.setSpacing(4)
        
        games_value = QLabel("247")
        games_value.setStyleSheet(f"""
            color: {INFO};
            font-size: {TITLE_SIZE - 4}px;
            font-weight: bold;
        """)
        
        games_label = QLabel("Games Played")
        games_label.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {CAPTION_SIZE}px;
        """)
        
        games_layout.addWidget(games_value)
        games_layout.addWidget(games_label)
        games_container.setLayout(games_layout)
        
        # Member Since
        member_container = QWidget()
        member_layout = QVBoxLayout()
        member_layout.setContentsMargins(0, 0, 0, 0)
        member_layout.setSpacing(4)
        
        member_value = QLabel("2 years")
        member_value.setStyleSheet(f"""
            color: {SUCCESS};
            font-size: {TITLE_SIZE - 4}px;
            font-weight: bold;
        """)
        
        member_label = QLabel("Member Since")
        member_label.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {CAPTION_SIZE}px;
        """)
        
        member_layout.addWidget(member_value)
        member_layout.addWidget(member_label)
        member_container.setLayout(member_layout)
        
        stats_layout.addWidget(rating_container)
        stats_layout.addWidget(games_container)
        stats_layout.addWidget(member_container)
        stats_layout.addStretch()
        
        profile_layout.addWidget(avatar_container)
        profile_layout.addLayout(stats_layout)
        
        layout.addWidget(title)
        layout.addLayout(profile_layout)
        
        self.setLayout(layout)


class AppearanceSettingsCard(QWidget):
    """Appearance settings card"""
    
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
        title = SettingsSection("Appearance")
        
        # Theme
        theme_combo = QComboBox()
        theme_combo.addItems(["Dark", "Light", "System"])
        theme_combo.setCurrentIndex(0)
        theme_combo.setFixedWidth(150)
        theme_combo.setStyleSheet(f"""
            QComboBox {{
                background-color: {SIDEBAR};
                border-radius: {BUTTON_RADIUS - 4}px;
                color: {PRIMARY_TEXT};
                font-size: {BODY_SIZE - 1}px;
                padding: {TINY_PADDING}px {SMALL_PADDING}px;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }}
            QComboBox::drop-down {{
                border: none;
            }}
            QComboBox QAbstractItemView {{
                background-color: {SIDEBAR};
                color: {PRIMARY_TEXT};
                selection-background-color: {CARD_HOVER};
            }}
        """)
        
        theme_item = SettingsItem("Theme", theme_combo)
        
        # Accent Color
        accent_combo = QComboBox()
        accent_combo.addItems(["Gold", "Blue", "Green", "Purple", "Red"])
        accent_combo.setCurrentIndex(0)
        accent_combo.setFixedWidth(150)
        accent_combo.setStyleSheet(f"""
            QComboBox {{
                background-color: {SIDEBAR};
                border-radius: {BUTTON_RADIUS - 4}px;
                color: {PRIMARY_TEXT};
                font-size: {BODY_SIZE - 1}px;
                padding: {TINY_PADDING}px {SMALL_PADDING}px;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }}
            QComboBox::drop-down {{
                border: none;
            }}
        """)
        
        accent_item = SettingsItem("Accent Color", accent_combo)
        
        # Font Size
        font_slider = QSlider(Qt.Horizontal)
        font_slider.setRange(12, 20)
        font_slider.setValue(15)
        font_slider.setFixedWidth(150)
        font_slider.setStyleSheet(f"""
            QSlider::groove:horizontal {{
                background: {SIDEBAR};
                border-radius: 4px;
                height: 8px;
            }}
            QSlider::handle:horizontal {{
                background: {ACCENT};
                border-radius: 4px;
                width: 16px;
                height: 16px;
                margin: -4px 0;
            }}
            QSlider::add-page:horizontal {{
                background: {CARD_HOVER};
                border-radius: 4px;
            }}
            QSlider::sub-page:horizontal {{
                background: {ACCENT};
                border-radius: 4px;
            }}
        """)
        
        font_item = SettingsItem("Font Size", font_slider)
        
        layout.addWidget(title)
        layout.addWidget(theme_item)
        layout.addWidget(accent_item)
        layout.addWidget(font_item)
        layout.addStretch()
        
        self.setLayout(layout)


class NotificationSettingsCard(QWidget):
    """Notification settings card"""
    
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
        title = SettingsSection("Notifications")
        
        # Toggle Buttons
        notification_types = [
            "Daily Reminders",
            "Training Tips",
            "Game Analysis Complete",
            "New Puzzles Available",
            "Tournament Alerts"
        ]
        
        for notification_type in notification_types:
            toggle = QPushButton("ON")
            toggle.setFixedWidth(60)
            toggle.setStyleSheet(f"""
                QPushButton {{
                    background-color: {SUCCESS};
                    border-radius: {BUTTON_RADIUS - 4}px;
                    color: {BACKGROUND};
                    font-size: {CAPTION_SIZE}px;
                    font-weight: 600;
                }}
                QPushButton:hover {{
                    background-color: {SUCCESS};
                }}
            """)
            
            item = SettingsItem(notification_type, toggle)
            layout.addWidget(item)
        
        layout.addWidget(title)
        for notification_type in notification_types:
            toggle = QPushButton("ON")
            toggle.setFixedWidth(60)
            toggle.setStyleSheet(f"""
                QPushButton {{
                    background-color: {SUCCESS};
                    border-radius: {BUTTON_RADIUS - 4}px;
                    color: {BACKGROUND};
                    font-size: {CAPTION_SIZE}px;
                    font-weight: 600;
                }}
                QPushButton:hover {{
                    background-color: {SUCCESS};
                }}
            """)
            
            item = SettingsItem(notification_type, toggle)
            layout.addWidget(item)
        
        self.setLayout(layout)


class AboutSettingsCard(QWidget):
    """About settings card"""
    
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
        title = QLabel("About KnightOS")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {HEADING_SIZE + 2}px;
            font-weight: 600;
        """)
        
        # Version
        version = QLabel("Version 1.0.0")
        version.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {BODY_SIZE - 1}px;
        """)
        
        # Description
        desc = QLabel("KnightOS is a premium chess improvement operating system designed to help tournament players train, review games, study openings, and receive AI coaching.")
        desc.setStyleSheet(f"""
            color: {SECONDARY_TEXT};
            font-size: {BODY_SIZE - 1}px;
            line-height: 1.6;
        """)
        desc.setWordWrap(True)
        
        # Copyright
        copyright = QLabel("© 2024 KnightOS. All rights reserved.")
        copyright.setStyleSheet(f"""
            color: {TERTIARY_TEXT};
            font-size: {CAPTION_SIZE}px;
        """)
        
        layout.addWidget(title)
        layout.addSpacing(8)
        layout.addWidget(version)
        layout.addSpacing(8)
        layout.addWidget(desc)
        layout.addStretch()
        layout.addWidget(copyright)
        
        self.setLayout(layout)


class Settings(QWidget):
    """Settings Page"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setStyleSheet(f"""
            background-color: {BACKGROUND};
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(PADDING, PADDING, PADDING, PADDING)
        layout.setSpacing(CARD_PADDING)
        
        # Title
        title = QLabel("Settings")
        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {TITLE_SIZE}px;
            font-weight: 600;
        """)
        
        # Profile Card
        profile_card = ProfileSettingsCard()
        profile_card.setMinimumWidth(400)
        
        # Settings Cards Grid
        settings_layout = QHBoxLayout()
        settings_layout.setContentsMargins(0, 0, 0, 0)
        settings_layout.setSpacing(CARD_PADDING)
        
        # Column 1
        column1 = QVBoxLayout()
        column1.setContentsMargins(0, 0, 0, 0)
        column1.setSpacing(CARD_PADDING)
        
        appearance_card = AppearanceSettingsCard()
        appearance_card.setMinimumWidth(350)
        
        notification_card = NotificationSettingsCard()
        notification_card.setMinimumWidth(350)
        
        column1.addWidget(appearance_card)
        column1.addWidget(notification_card)
        column1.addStretch()
        
        # Column 2
        column2 = QVBoxLayout()
        column2.setContentsMargins(0, 0, 0, 0)
        column2.setSpacing(CARD_PADDING)
        
        about_card = AboutSettingsCard()
        about_card.setMinimumWidth(350)
        
        column2.addWidget(about_card)
        column2.addStretch()
        
        settings_layout.addLayout(column1)
        settings_layout.addLayout(column2)
        settings_layout.addStretch()
        
        # Combine all
        layout.addWidget(title)
        layout.addSpacing(8)
        layout.addWidget(profile_card)
        layout.addSpacing(CARD_PADDING)
        layout.addLayout(settings_layout)
        layout.addStretch()
        
        self.setLayout(layout)
