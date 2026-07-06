from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

from app.theme import *


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(SIDEBAR_WIDTH)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 25, 20, 25)
        layout.setSpacing(18)

        title = QLabel("♞ KnightOS")

        title.setStyleSheet(f"""
            color: {PRIMARY_TEXT};
            font-size: {TITLE_SIZE}px;
            font-weight: bold;
        """)

        layout.addWidget(title)

        items = [
            "🏠 Dashboard",
            "📅 Today",
            "🧩 Training",
            "♟ Openings",
            "📖 Games",
            "🤖 Coach",
            "📈 Progress",
            "⚙ Settings"
        ]

        for item in items:
            label = QLabel(item)

            label.setStyleSheet(f"""
                color: {PRIMARY_TEXT};
                font-size: {BODY_SIZE}px;
                padding:10px;
            """)

            layout.addWidget(label)

        layout.addStretch()

        self.setLayout(layout)

        self.setStyleSheet(f"""
            background:{SIDEBAR};
        """)