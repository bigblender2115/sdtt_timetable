#!/usr/bin/env python3
"""
Enhanced Timetable Generator Runner
"""

import sys
import os

# Add current directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'enhanced':
            from optimization.enhanced_main import EnhancedTimetableGenerator
            generator = EnhancedTimetableGenerator()
            generator.generate_timetable()
        elif sys.argv[1] == 'config':
            from utils.config_integration import update_main_with_config
            update_main_with_config()
        elif sys.argv[1] == 'conflict':
            from optimization.conflict_resolver import create_conflict_resolution_tools
            tools = create_conflict_resolution_tools()
            print("Conflict resolution tools loaded successfully")
        elif sys.argv[1] == 'original':
            from core.main import generate_timetable
            generate_timetable()
        elif sys.argv[1] == 'help':
            print_help()
        else:
            print("Invalid option. Use 'python run.py help' for usage information.")
    else:
        print("Enhanced Timetable Generator")
        print("Usage: python run.py [enhanced|config|conflict|original|help]")
        print("Use 'python run.py help' for detailed usage information.")

def print_help():
    print("Enhanced Timetable Generator - Usage Guide")
    print()
    print("Available commands:")
    print("  enhanced    - Run the fully enhanced version with all features")
    print("  config      - Update main.py with configuration integration")
    print("  conflict    - Test conflict resolution tools")
    print("  original    - Run the original timetable generator")
    print("  help        - Show this help message")
    print()
    print("Examples:")
    print("  python run.py enhanced    # Run with auto-retry, optimization, and conflict resolution")
    print("  python run.py original    # Run the basic version")
    print("  python run.py conflict    # Test conflict resolution features")
    print()
    print("Configuration:")
    print("  Edit src/config/config.json to customize settings")
    print()
    print("Input Data:")
    print("  Place your CSV files in the data/ directory:")
    print("  - data/Combined.csv (course data)")
    print("  - data/Rooms.csv (room data)")
    print()
    print("Output:")
    print("  Generated timetables will be saved to output/ directory")
    print("  Logs will be saved to logs/ directory")

if __name__ == "__main__":
    main()
