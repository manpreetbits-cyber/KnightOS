# KnightOS - Premium Chess Improvement Operating System

## Overview

KnightOS is a modern, elegant, and distraction-free chess improvement operating system designed for tournament players. It helps you train, review games, study openings, and receive AI coaching with a premium, Apple-inspired interface.

## Design Philosophy

KnightOS combines the best design elements from:
- **Apple Keynote** - Clean, elegant typography and spacing
- **Arc Browser** - Modern, card-based layouts
- **Linear** - Minimal, focused interface
- **Notion** - Organized, structured content
- **Raycast** - Fast, keyboard-driven workflows

## Features

### 🏠 Home
- **Dashboard** - Personal mission control with stats and recommendations
- **Today** - Daily training overview and schedule

### 🎯 Training
- **Training Plan** - Structured training modules and weekly schedule
- **Openings** - Visual repertoire management with progress tracking
- **Middlegame** - Thematic training and exercises
- **Endgames** - Comprehensive endgame training
- **Puzzles** - Tactical puzzle collection with statistics

### 📊 Database
- **Games** - Beautiful game cards with filtering and statistics
- **Players** - Opponent database with performance tracking

### 🤖 Analysis
- **AI Coach** - Personal chess coach with recommendations
- **Progress** - Modern graphs and skill tracking
- **Goals** - Goal setting and progress monitoring

### ⚙️ System
- **Settings** - Customize your experience

## Theme

- **Background**: Almost black (#090B10)
- **Cards**: Subtle elevation (#171C24)
- **Sidebar**: Slightly lighter (#11151C)
- **Accent**: Gold (#C89B3C)
- **Typography**: Soft white (#F5F7FA)
- **Secondary**: Muted gray (#A2AAB8)

## Installation

```bash
# Clone the repository
git clone https://github.com/manpreetbits-cyber/KnightOS.git
cd KnightOS

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## Requirements

- Python 3.8+
- PySide6 6.6.0+
- matplotlib 3.8.2+ (for charts)
- numpy 1.26.4+ (for data processing)

## Architecture

```
KnightOS/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── app/
│   ├── theme.py           # Theme constants and styling
│   └── ui/
│       ├── __init__.py
│       ├── main_window.py # Main application window
│       ├── sidebar.py     # Navigation sidebar
│       ├── topbar.py      # Top navigation bar
│       ├── icons.py       # SVG icons collection
│       └── pages/         # All application pages
│           ├── dashboard.py
│           ├── today.py
│           ├── training_plan.py
│           ├── openings.py
│           ├── middlegame.py
│           ├── endgames.py
│           ├── puzzles.py
│           ├── games.py
│           ├── players.py
│           ├── ai_coach.py
│           ├── progress.py
│           ├── goals.py
│           └── settings.py
```

## Design Principles

1. **Minimal & Clean** - No clutter, only essential elements
2. **Generous Whitespace** - Breathing room for focus
3. **Smooth Corners** - 18-20px rounded corners everywhere
4. **Subtle Shadows** - Depth without borders
5. **Modern Typography** - Clear, readable fonts
6. **Consistent Spacing** - Uniform padding and margins
7. **Premium Feel** - Every detail matters

## Contributing

Contributions are welcome! Please follow the existing design patterns and maintain the premium aesthetic.

## License

KnightOS is proprietary software. All rights reserved.

## Screenshots

The application features a beautiful OLED dark mode interface with:
- Floating stat cards on the dashboard
- Visual opening repertoire cards
- Beautiful game cards instead of spreadsheet rows
- Modern radar charts for skill tracking
- Personal AI coach recommendations

## Future Enhancements

- [ ] Chess board visualization
- [ ] Real-time game analysis
- [ ] Puzzle of the day
- [ ] Tournament preparation tools
- [ ] Multi-language support
- [ ] Cloud synchronization
- [ ] Mobile companion app
