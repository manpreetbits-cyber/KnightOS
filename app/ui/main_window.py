"""
KnightOS Main Window - Premium Chess Improvement Operating System
"""

from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QStackedWidget
from PySide6.QtCore import Qt

from app.theme import BACKGROUND, WINDOW_WIDTH, WINDOW_HEIGHT
from app.ui.sidebar import Sidebar
from app.ui.topbar import TopBar
from app.ui.pages import (
    Dashboard, Today, TrainingPlan, Openings, Middlegame, Endgames, Puzzles,
    Games, Players, AICoach, Progress, Goals, Settings
)


class MainWindow(QMainWindow):
    """Main application window with sidebar navigation"""
    
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
        
        # Main Layout
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Sidebar
        self.sidebar = Sidebar()
        self.sidebar.page_changed.connect(self._on_page_changed)
        
        # Top Bar
        self.topbar = TopBar()
        self.topbar.setFixedHeight(70)
        
        # Content Area
        content_area = QWidget()
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)
        
        # Add top bar to content area
        content_layout.addWidget(self.topbar)
        
        # Stacked Widget for Pages
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setStyleSheet(f"""
            background-color: {BACKGROUND};
        """)
        
        # Initialize all pages
        self._initialize_pages()
        
        content_layout.addWidget(self.stacked_widget)
        content_area.setLayout(content_layout)
        
        # Add sidebar and content to main layout
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(content_area)
        
        central.setLayout(main_layout)
        self.setCentralWidget(central)
        
        # Set default page
        self._on_page_changed("Dashboard")
    
    def _initialize_pages(self):
        """Initialize all application pages"""
        
        # Home Pages
        self.dashboard_page = Dashboard()
        self.today_page = Today()
        
        # Training Pages
        self.training_plan_page = TrainingPlan()
        self.openings_page = Openings()
        self.middlegame_page = Middlegame()
        self.endgames_page = Endgames()
        self.puzzles_page = Puzzles()
        
        # Database Pages
        self.games_page = Games()
        self.players_page = Players()
        
        # Analysis Pages
        self.ai_coach_page = AICoach()
        self.progress_page = Progress()
        self.goals_page = Goals()
        
        # System Pages
        self.settings_page = Settings()
        
        # Add pages to stacked widget
        self.stacked_widget.addWidget(self.dashboard_page)
        self.stacked_widget.addWidget(self.today_page)
        self.stacked_widget.addWidget(self.training_plan_page)
        self.stacked_widget.addWidget(self.openings_page)
        self.stacked_widget.addWidget(self.middlegame_page)
        self.stacked_widget.addWidget(self.endgames_page)
        self.stacked_widget.addWidget(self.puzzles_page)
        self.stacked_widget.addWidget(self.games_page)
        self.stacked_widget.addWidget(self.players_page)
        self.stacked_widget.addWidget(self.ai_coach_page)
        self.stacked_widget.addWidget(self.progress_page)
        self.stacked_widget.addWidget(self.goals_page)
        self.stacked_widget.addWidget(self.settings_page)
        
        # Page mapping
        self.page_mapping = {
            "Dashboard": 0,
            "Today": 1,
            "Training Plan": 2,
            "Openings": 3,
            "Middlegame": 4,
            "Endgames": 5,
            "Puzzles": 6,
            "Games": 7,
            "Players": 8,
            "AI Coach": 9,
            "Progress": 10,
            "Goals": 11,
            "Settings": 12
        }
    
    def _on_page_changed(self, page_name):
        """Handle page navigation from sidebar"""
        page_index = self.page_mapping.get(page_name, 0)
        self.stacked_widget.setCurrentIndex(page_index)
        self.sidebar.set_active_page(page_name)
        
        # Update window title
        self.setWindowTitle(f"♞ KnightOS - {page_name}")
