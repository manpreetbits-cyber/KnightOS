from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

from app.theme import *


class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(15)

        title = QLabel("Good afternoon, Shehzaad!")

        title.setStyleSheet(f"""
            color:{PRIMARY_TEXT};
            font-size:{TITLE_SIZE}px;
            font-weight:bold;
        """)

        subtitle = QLabel("KnightOS v0.1 Alpha")

        subtitle.setStyleSheet(f"""
            color:{SECONDARY_TEXT};
            font-size:{BODY_SIZE}px;
        """)

        tasks = QLabel(
            "Today's Training\n\n"
            "□ 30 min Calculation\n"
            "□ Middlegame Study\n"
            "□ Endgames\n"
            "□ Review Tournament Games"
        )

        tasks.setStyleSheet(f"""
            color:{PRIMARY_TEXT};
            font-size:{HEADING_SIZE}px;
            margin-top:30px;
        """)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(40)
        layout.addWidget(tasks)
        layout.addStretch()

        self.setLayout(layout)

        self.setStyleSheet(f"""
            background:{BACKGROUND};
        """)