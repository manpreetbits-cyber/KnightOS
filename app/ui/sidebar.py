"""
KnightOS Sidebar - Premium Navigation
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap, QIcon, QPainter

from app.theme import *
from app.ui.icons import (
    CHESS_KNIGHT_ICON, DASHBOARD_ICON, TODAY_ICON,
    TRAINING_PLAN_ICON, OPENINGS_ICON, MIDDLEGAME_ICON, 
    ENDGAMES_ICON, PUZZLES_ICON,
    GAMES_ICON, PLAYERS_ICON,
    AI_COACH_ICON, PROGRESS_ICON, GOALS_ICON,
    SETTINGS_ICON
)


class SidebarItem(QPushButton):
    """Custom sidebar navigation item"""
    
    def __init__(self, icon_svg, text, is_active=False, parent=None):
        super().__init__(parent)
        self.text = text
        self.is_active = is_active
        
        self.setFixedHeight(SIDEBAR_ITEM_HEIGHT)
        self.setStyleSheet(self._get_style())
        
        layout = QHBoxLayout()
        layout.setContentsMargins(SIDEBAR_ITEM_PADDING, 0, SIDEBAR_ITEM_PADDING, 0)
        layout.setSpacing(SIDEBAR_ITEM_PADDING)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        # Icon
        self.icon_label = QLabel()
        self.icon_label.setFixedSize(SIDEBAR_ICON_SIZE, SIDEBAR_ICON_SIZE)
        self.icon_label.setPixmap(self._create_icon(icon_svg, SIDEBAR_ICON_SIZE, SIDEBAR_ICON_SIZE))
        
        # Text
        self.text_label = QLabel(text)
        self.text_label.setStyleSheet(f"""
            color: {PRIMARY_TEXT if is_active else SECONDARY_TEXT};
            font-size: {BODY_SIZE}px;
            font-weight: {500 if is_active else 400};
        """)
        
        layout.addWidget(self.icon_label)
        layout.addWidget(self.text_label)
        layout.addStretch()
        
        self.setLayout(layout)
    
    def _get_style(self):
        if self.is_active:
            return f"""
                QPushButton {{
                    background-color: {CARD};
                    border-radius: {CARD_RADIUS - 4}px;
                    border: none;
                }}
                QPushButton:hover {{
                    background-color: {CARD_HOVER};
                }}
                QPushButton:pressed {{
                    background-color: {SIDEBAR};
                }}
            """
        else:
            return f"""
                QPushButton {{
                    background-color: transparent;
                    border-radius: {CARD_RADIUS - 4}px;
                    border: none;
                }}
                QPushButton:hover {{
                    background-color: {CARD};
                }}
                QPushButton:pressed {{
                    background-color: {CARD_HOVER};
                }}
            """
    
    def _create_icon(self, svg_content, width, height):
        """Create an icon from SVG content"""
        from PySide6.QtSvg import QSvgRenderer
        from PySide6.QtGui import QPixmap
        
        renderer = QSvgRenderer()
        color = ACCENT if self.is_active else SECONDARY_TEXT
        svg_with_color = svg_content.replace('stroke="currentColor"', f'stroke="{color}"')
        svg_with_color = svg_with_color.replace('fill="currentColor"', f'fill="{color}"')
        renderer.load(svg_with_color.encode())
        
        pixmap = QPixmap(width, height)
        pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()

        return pixmap
    
    def set_active(self, active):
        self.is_active = active
        self.setStyleSheet(self._get_style())
        color = ACCENT if active else SECONDARY_TEXT
        self.icon_label.setPixmap(self._create_icon(
            self._get_icon_svg(self.text), 
            SIDEBAR_ICON_SIZE, SIDEBAR_ICON_SIZE
        ))
        self.text_label.setStyleSheet(f"""
            color: {PRIMARY_TEXT if active else SECONDARY_TEXT};
            font-size: {BODY_SIZE}px;
            font-weight: {500 if active else 400};
        """)
    
    def _get_icon_svg(self, text):
        icons = {
            "Dashboard": DASHBOARD_ICON,
            "Today": TODAY_ICON,
            "Training Plan": TRAINING_PLAN_ICON,
            "Openings": OPENINGS_ICON,
            "Middlegame": MIDDLEGAME_ICON,
            "Endgames": ENDGAMES_ICON,
            "Puzzles": PUZZLES_ICON,
            "Games": GAMES_ICON,
            "Players": PLAYERS_ICON,
            "AI Coach": AI_COACH_ICON,
            "Progress": PROGRESS_ICON,
            "Goals": GOALS_ICON,
            "Settings": SETTINGS_ICON
        }
        return icons.get(text, DASHBOARD_ICON)


class SectionHeader(QLabel):
    """Sidebar section header"""
    
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet(f"""
            color: {TERTIARY_TEXT};
            font-size: {CAPTION_SIZE}px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            padding: {TINY_PADDING}px {SIDEBAR_ITEM_PADDING}px;
        """)
        self.setFixedHeight(32)


class Sidebar(QWidget):
    """Main sidebar with navigation sections"""
    
    page_changed = Signal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.items = {}
        self.setFixedWidth(SIDEBAR_WIDTH)
        self.setStyleSheet(f"""
            background-color: {SIDEBAR};
            border-right: 1px solid rgba(255, 255, 255, 0.05);
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, PADDING, 0, PADDING)
        layout.setSpacing(0)
        
        # Logo/Title
        logo_container = QWidget()
        logo_container.setFixedHeight(60)
        logo_layout = QVBoxLayout()
        logo_layout.setContentsMargins(SIDEBAR_ITEM_PADDING, 0, SIDEBAR_ITEM_PADDING, 0)
        
        logo_icon = QLabel()
        logo_icon.setPixmap(self._create_icon(CHESS_KNIGHT_ICON, 28, 28, ACCENT))
        logo_icon.setFixedSize(28, 28)
        
        logo_text = QLabel("KnightOS")
        logo_text.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {TITLE_SIZE - 4}px;
            font-weight: bold;
        """)
        
        logo_layout.addWidget(logo_icon)
        logo_layout.addWidget(logo_text)
        logo_container.setLayout(logo_layout)
        
        layout.addWidget(logo_container)
        layout.addSpacing(SIDEBAR_SECTION_SPACING)
        
        # Navigation Sections
        self._add_section(layout, "HOME", ["Dashboard", "Today"])
        self._add_section(layout, "TRAINING", ["Training Plan", "Openings", "Middlegame", "Endgames", "Puzzles"])
        self._add_section(layout, "DATABASE", ["Games", "Players"])
        self._add_section(layout, "ANALYSIS", ["AI Coach", "Progress", "Goals"])
        self._add_section(layout, "SYSTEM", ["Settings"])
        
        # Spacer
        layout.addStretch()
        
        self.setLayout(layout)
        
        # Store items for active state management
        self._collect_items(logo_container)
    
    def _add_section(self, layout, title, items):
        """Add a navigation section to the sidebar"""
        # Section Header
        header = SectionHeader(title)
        layout.addWidget(header)
        layout.addSpacing(4)
        
        # Section Items
        for item_text in items:
            item = SidebarItem(
                self._get_icon_svg(item_text),
                item_text,
                is_active=(item_text == "Dashboard")  # Default active
            )
            item.clicked.connect(lambda checked, text=item_text: self._on_item_clicked(text))
            layout.addWidget(item)
            self.items[item_text] = item
        
        layout.addSpacing(SIDEBAR_SECTION_SPACING - 8)
    
    def _get_icon_svg(self, text):
        icons = {
            "Dashboard": DASHBOARD_ICON,
            "Today": TODAY_ICON,
            "Training Plan": TRAINING_PLAN_ICON,
            "Openings": OPENINGS_ICON,
            "Middlegame": MIDDLEGAME_ICON,
            "Endgames": ENDGAMES_ICON,
            "Puzzles": PUZZLES_ICON,
            "Games": GAMES_ICON,
            "Players": PLAYERS_ICON,
            "AI Coach": AI_COACH_ICON,
            "Progress": PROGRESS_ICON,
            "Goals": GOALS_ICON,
            "Settings": SETTINGS_ICON
        }
        return icons.get(text, DASHBOARD_ICON)
    
    def _collect_items(self, widget):
        """Recursively collect all SidebarItem instances"""
        for child in widget.findChildren(QWidget):
            if isinstance(child, SidebarItem):
                self.items[child.text] = child
            # recurse into child widgets
            self._collect_items(child)
    
    def _on_item_clicked(self, page_name):
        """Handle navigation item click"""
        # Update active states
        for item_text, item in self.items.items():
            item.set_active(item_text == page_name)
        
        self.page_changed.emit(page_name)
    
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

        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()

        return pixmap
    
    def set_active_page(self, page_name):
        """Set the active page programmatically"""
        for item_text, item in self.items.items():
            item.set_active(item_text == page_name)
