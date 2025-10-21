# 🗓️ Enhanced Timetable Generator

A comprehensive Python system for generating academic timetables with advanced conflict resolution, optimization, and configuration management.

## 📁 Project Structure

```
ctimetable/
├── 📁 src/                          # Source code
│   ├── 📁 core/                     # Core timetable generation
│   │   ├── main.py                  # Original main generator
│   │   ├── TT_gen.py                # Alternative generator
│   │   ├── comprehensive_timetable.py # Comprehensive generator
│   │   └── main_enhanced.py         # Enhanced version of main.py
│   ├── 📁 optimization/             # Advanced features
│   │   ├── enhanced_main.py         # Fully enhanced generator
│   │   └── conflict_resolver.py     # Conflict resolution tools
│   ├── 📁 config/                   # Configuration management
│   │   └── config.json              # Main configuration file
│   ├── 📁 utils/                    # Utility functions
│   │   └── config_integration.py    # Configuration integration
│   ├── 📁 scheduling/               # Scheduling algorithms
│   └── run.py                       # Main runner script
├── 📁 tests/                        # Unit tests
│   ├── test_main_unit.py            # Unit tests for main functions
│   └── TEST_CASES.md                # Test case documentation
├── 📁 data/                         # Input data files
│   ├── Combined.csv                 # Course data
│   ├── Rooms.csv                    # Room data
│   └── ...
├── 📁 output/                       # Generated timetables
│   ├── timetable.xlsx               # Main output
│   └── ...
├── 📁 docs/                         # Documentation
├── 📁 examples/                     # Example configurations
├── 📁 logs/                         # Log files
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Git ignore rules
└── README.md                        # This file
```

## 🚀 Quick Start

### Installation
```bash
pip install -r requirements.txt
```

### Basic Usage
```bash
# Run original generator
python src/core/main.py

# Run enhanced version
python src/run.py enhanced

# Run with configuration
python src/run.py config
```

## 🔧 Features

### Core Features
- ✅ **Timetable Generation**: Creates Excel timetables with color coding
- ✅ **Basket Electives**: Fixed time slots for elective groups (B1-B9)
- ✅ **Room Allocation**: Smart room assignment based on capacity and type
- ✅ **Faculty Scheduling**: Prevents faculty conflicts
- ✅ **Lunch Breaks**: Staggered lunch breaks across semesters

### Enhanced Features
- 🔄 **Auto-Retry**: Multiple attempts with different random seeds
- 🎯 **Priority Scheduling**: Core courses scheduled first
- 🔍 **Conflict Resolution**: Detailed analysis and suggestions
- ⚡ **Parallel Processing**: Multi-threading for large datasets
- 📊 **Performance Monitoring**: Tracks generation time and conflicts
- ⚙️ **Configuration Management**: Centralized settings in JSON

## 📋 Configuration

Edit `src/config/config.json` to customize:

```json
{
  "timetable_settings": {
    "start_time": "09:00",
    "end_time": "18:30",
    "slot_duration_minutes": 30
  },
  "scheduling": {
    "max_retry_attempts": 10,
    "priority_order": ["core_courses", "basket_electives", ...]
  },
  "optimization": {
    "enable_parallel_processing": true,
    "max_workers": 4
  }
}
```

## 🧪 Testing

```bash
# Run unit tests
pytest tests/

# Run specific tests
pytest tests/test_main_unit.py
```

## 📊 Input Data Format

### Courses (Combined.csv)
| Department | Semester | Course Code | Course Name | Faculty | L | T | P | S | total_students |
|------------|----------|-------------|-------------|---------|---|---|---|---|----------------|
| CSE        | 3        | CS101       | Intro to CS | Prof A  | 3 | 1 | 2 | 0 | 140            |

### Rooms (Rooms.csv)
| id | capacity | type          | roomNumber |
|----|----------|---------------|------------|
| R1 | 70       | LECTURE_ROOM  | R101       |

## 🎨 Output Features

- **Color-coded timetables** with department-specific colors
- **Basket elective grouping** with shared time slots
- **Conflict reports** for unscheduled courses
- **Performance statistics** and generation logs
- **Alternative slot suggestions** for scheduling conflicts

## 🔧 Development

### Adding New Features
1. Add configuration options to `src/config/config.json`
2. Implement feature in appropriate module
3. Add tests in `tests/`
4. Update documentation

### Code Organization
- **Core**: Basic timetable generation logic
- **Optimization**: Advanced features and conflict resolution
- **Config**: Configuration management
- **Utils**: Helper functions and utilities
- **Scheduling**: Scheduling algorithms

## 📝 License

This project is part of an academic timetable management system.

## 🤝 Contributing

1. Follow the existing code structure
2. Add tests for new features
3. Update documentation
4. Ensure backward compatibility

## 📞 Support

For issues or questions, please refer to the test cases in `tests/TEST_CASES.md` or check the configuration options in `src/config/config.json`.