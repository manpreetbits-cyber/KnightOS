from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout

from app.theme import BACKGROUND, WINDOW_WIDTH, WINDOW_HEIGHT
from app.ui.sidebar import Sidebar
from app.ui.dashboard import Dashboard


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("♞ KnightOS")
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        # Style the entire application window
        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: {BACKGROUND};
            }}
        """)

        # Central widget
        central = QWidget()
        central.setStyleSheet(f"""
            background-color: {BACKGROUND};
        """)

        # Layout
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        layout.addWidget(Sidebar())
        layout.addWidget(Dashboard())

        central.setLayout(layout)

        self.setCentralWidget(central)