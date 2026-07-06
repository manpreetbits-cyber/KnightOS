"""
KnightOS Top Bar - Search and User Profile
"""

from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap, QIcon
import sys
import os

from app.theme import *
from app.ui.icons import SEARCH_ICON, NOTIFICATION_ICON, USER_ICON


class TopBar(QWidget):
    """Top navigation bar with search and user profile"""
    
    search_text_changed = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(TOPBAR_HEIGHT)
        self.setStyleSheet(f"""
            background-color: {BACKGROUND};
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        """)
        
        layout = QHBoxLayout()
        layout.setContentsMargins(PADDING, 0, PADDING, 0)
        layout.setSpacing(SMALL_PADDING)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        # Search Container
        search_container = QWidget()
        search_container.setFixedHeight(INPUT_HEIGHT)
        search_container.setStyleSheet(f"""
            background-color: {CARD};
            border-radius: {INPUT_RADIUS}px;
            padding: 0 {INPUT_PADDING}px;
        """)
        
        search_layout = QHBoxLayout()
        search_layout.setContentsMargins(0, 0, 0, 0)
        search_layout.setSpacing(TINY_PADDING)
        search_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        # Search Icon
        search_icon = QLabel()
        search_icon.setPixmap(self._create_icon(SEARCH_ICON, 20, 20, SECONDARY_TEXT))
        search_icon.setStyleSheet(f"color: {SECONDARY_TEXT};")
        
        # Search Input
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search games, openings, players...")
        self.search_input.setStyleSheet(f"""
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
        self.search_input.setFixedHeight(INPUT_HEIGHT)
        self.search_input.textChanged.connect(self._on_search_changed)
        
        search_layout.addWidget(search_icon)
        search_layout.addWidget(self.search_input)
        search_container.setLayout(search_layout)
        
        # Spacer
        layout.addWidget(search_container)
        layout.addStretch()
        
        # Right side - Notification and User
        right_container = QWidget()
        right_layout = QHBoxLayout()
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(SMALL_PADDING)
        right_layout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        
        # Notification Button
        notification_btn = QPushButton()
        notification_btn.setIcon(self._create_icon(NOTIFICATION_ICON, 20, 20, SECONDARY_TEXT))
        notification_btn.setIconSize(QPixmap(20, 20).size())
        notification_btn.setFixedSize(40, 40)
        notification_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: transparent;
                border: none;
                border-radius: 10px;
            }}
            QPushButton:hover {{
                background-color: {CARD_HOVER};
            }}
            QPushButton:pressed {{
                background-color: {SIDEBAR};
            }}
        """)
        
        # User Profile
        user_container = QWidget()
        user_layout = QHBoxLayout()
        user_layout.setContentsMargins(0, 0, 0, 0)
        user_layout.setSpacing(TINY_PADDING)
        user_layout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        
        # User Avatar
        user_avatar = QLabel()
        user_avatar.setFixedSize(AVATAR_SIZE, AVATAR_SIZE)
        user_avatar.setStyleSheet(f"""
            background-color: {ACCENT};
            border-radius: {AVATAR_RADIUS}px;
            color: {BACKGROUND};
            font-weight: bold;
            display: flex;
            align-items: center;
            justify-content: center;
        """)
        user_avatar.setText("S")
        user_avatar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # User Name and Dropdown
        user_info = QWidget()
        user_info_layout = QHBoxLayout()
        user_info_layout.setContentsMargins(0, 0, 0, 0)
        user_info_layout.setSpacing(4)
        
        user_name = QLabel("Shehzaad")
        user_name.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {BODY_SIZE}px;
            font-weight: 500;
        """)
        
        user_dropdown = QPushButton()
        user_dropdown.setIcon(self._create_icon("▼", 12, 12, SECONDARY_TEXT))
        user_dropdown.setFixedSize(20, 20)
        user_dropdown.setStyleSheet(f"""
            QPushButton {{
                background: transparent;
                border: none;
                color: {SECONDARY_TEXT};
                font-size: 10px;
            }}
        """)
        
        user_info_layout.addWidget(user_name)
        user_info_layout.addWidget(user_dropdown)
        user_info.setLayout(user_info_layout)
        
        user_layout.addWidget(user_avatar)
        user_layout.addWidget(user_info)
        user_container.setLayout(user_layout)
        
        right_layout.addWidget(notification_btn)
        right_layout.addWidget(user_container)
        right_container.setLayout(right_layout)
        
        layout.addWidget(right_container)
        self.setLayout(layout)
    
    def _on_search_changed(self, text):
        self.search_text_changed.emit(text)
    
    def _create_icon(self, svg_content, width, height, color):
        """Create an icon from SVG content"""
        from PySide6.QtSvg import QSvgRenderer
        from PySide6.QtGui import QImage
        
        renderer = QSvgRenderer()
        svg_with_color = svg_content.replace('stroke="currentColor"', f'stroke="{color}"')
        svg_with_color = svg_with_color.replace('fill="currentColor"', f'fill="{color}"')
        renderer.load(svg_with_color.encode())
        
        image = QImage(width, height, QImage.Format.Format_ARGB32)
        image.fill(Qt.GlobalColor.transparent)
        
        painter = QPixmap(width, height)
        painter.fill(Qt.GlobalColor.transparent)
        
        svg_painter = QPixmap(width, height)
        svg_painter.fill(Qt.GlobalColor.transparent)
        
        svg_renderer = QSvgRenderer()
        svg_renderer.load(svg_with_color.encode())
        
        p = QPixmap(width, height)
        p.fill(Qt.GlobalColor.transparent)
        
        painter = QPixmap(p)
        svg_renderer.render(painter)
        
        return QIcon(p).pixmap(width, height)
    
    def get_search_text(self):
        return self.search_input.text()
    
    def set_search_text(self, text):
        self.search_input.setText(text)
