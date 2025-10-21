# 📁 Project Structure Overview

## 🎯 **Organized File Structure**

Your timetable project has been completely reorganized into a professional structure:

```
ctimetable/
├── 📁 src/                          # Source code (organized by functionality)
│   ├── 📁 core/                     # Core timetable generation engines
│   │   ├── main.py                  # Original main generator
│   │   ├── TT_gen.py                # Alternative generator  
│   │   ├── comprehensive_timetable.py # Comprehensive generator
│   │   └── main_enhanced.py         # Enhanced version of main.py
│   ├── 📁 optimization/             # Advanced features & algorithms
│   │   ├── enhanced_main.py         # Fully enhanced generator with all features
│   │   └── conflict_resolver.py     # Conflict resolution & alternative slots
│   ├── 📁 config/                   # Configuration management
│   │   └── config.json              # Main configuration file
│   ├── 📁 utils/                    # Utility functions & helpers
│   │   └── config_integration.py    # Configuration integration tools
│   ├── 📁 scheduling/               # Scheduling algorithms (ready for expansion)
│   ├── run.py                       # Main runner script
│   └── __init__.py                  # Package initialization
├── 📁 tests/                        # Unit tests & test documentation
│   ├── test_main_unit.py            # Comprehensive unit tests
│   └── TEST_CASES.md                # Test case documentation
├── 📁 data/                         # Input data files
│   ├── Combined.csv                 # Course data
│   ├── Rooms.csv                    # Room data
│   └── [other CSV files]
├── 📁 output/                       # Generated timetables
│   ├── timetable.xlsx               # Main output
│   └── [other generated files]
├── 📁 docs/                         # Documentation
│   └── USAGE.md                     # Detailed usage guide
├── 📁 examples/                     # Example configurations
│   └── example_config.json          # Sample configuration file
├── 📁 logs/                         # Log files (auto-created)
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Git ignore rules
├── README.md                        # Main project documentation
└── PROJECT_STRUCTURE.md             # This file
```

## 🚀 **How to Use the New Structure**

### **Quick Commands:**
```bash
# Run enhanced version with all features
python src/run.py enhanced

# Run original version
python src/run.py original

# Get help
python src/run.py help

# Test conflict resolution
python src/run.py conflict
```

### **File Organization Benefits:**

1. **📁 src/core/**: All your original generators are preserved
2. **📁 src/optimization/**: New advanced features are isolated
3. **📁 src/config/**: Configuration is centralized and easy to modify
4. **📁 data/**: All input files are organized in one place
5. **📁 output/**: Generated files are separated from source code
6. **📁 tests/**: Your test cases are properly organized
7. **📁 docs/**: Documentation is structured and accessible

## 🔧 **Key Improvements Made:**

### **1. Conflict Resolution System**
- ✅ Auto-retry with different random seeds
- ✅ Priority-based scheduling (core → basket → electives → tutorials → labs)
- ✅ Activation slot suggestions for unscheduled courses
- ✅ Detailed conflict analysis and reporting

### **2. Configuration Management**
- ✅ Centralized `config.json` with all settings
- ✅ Easy customization of time slots, durations, colors
- ✅ Department-specific settings
- ✅ Fallback options for missing files

### **3. Optimization Features**
- ✅ Parallel processing for large datasets
- ✅ Memory optimization
- ✅ Performance monitoring and logging
- ✅ Advanced scheduling algorithms

### **4. Professional Structure**
- ✅ Modular code organization
- ✅ Clear separation of concerns
- ✅ Comprehensive documentation
- ✅ Proper testing framework

## 📊 **What Each Directory Contains:**

| Directory | Purpose | Key Files |
|-----------|---------|-----------|
| `src/core/` | Original generators | `main.py`, `TT_gen.py`, `comprehensive_timetable.py` |
| `src/optimization/` | Advanced features | `enhanced_main.py`, `conflict_resolver.py` |
| `src/config/` | Configuration | `config.json` |
| `src/utils/` | Helper functions | `config_integration.py` |
| `data/` | Input files | `Combined.csv`, `Rooms.csv` |
| `output/` | Generated files | `timetable.xlsx`, etc. |
| `tests/` | Testing | `test_main_unit.py`, `TEST_CASES.md` |
| `docs/` | Documentation | `USAGE.md` |
| `examples/` | Examples | `example_config.json` |

## 🎯 **Next Steps:**

1. **Test the enhanced system**: `python src/run.py enhanced`
2. **Customize configuration**: Edit `src/config/config.json`
3. **Add your data**: Place CSV files in `data/` directory
4. **Run tests**: `pytest tests/`
5. **Generate timetables**: Use the runner script with your preferred mode

## 💡 **Benefits of This Structure:**

- **🔧 Maintainable**: Easy to find and modify specific functionality
- **🚀 Scalable**: Easy to add new features without breaking existing code
- **📚 Documented**: Clear documentation and examples
- **🧪 Testable**: Organized test structure
- **⚙️ Configurable**: Centralized configuration management
- **🎯 Professional**: Industry-standard project organization

Your timetable system is now organized like a professional software project with all the advanced features you requested!
