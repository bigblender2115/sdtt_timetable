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
        if sys.argv[1] == 'generate':
            from core.TT_gen import generate_all_timetables
            generate_all_timetables()
        elif sys.argv[1] == 'enhanced':
            from optimization.enhanced_main import EnhancedTimetableGenerator
            # Ensure the enhanced generator loads the config from src/config/config.json relative to this file
            config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config', 'config.json')
            generator = EnhancedTimetableGenerator(config_file=config_path)
            generator.generate_timetable()
        elif sys.argv[1] == 'help':
            print_help()
        else:
            print("Invalid option. Use 'python run.py help' for usage information.")
    else:
        # Default: run the main generator
        from core.TT_gen import generate_all_timetables
        generate_all_timetables()

def print_help():
    print("Timetable Generator - Usage Guide")
    print()
    print("Available commands:")
    print("  (no args)   - Run the main timetable generator (default)")
    print("  generate    - Run the main timetable generator")
    print("  enhanced    - Run with logging and performance metrics")
    print("  help        - Show this help message")
    print()
    print("Examples:")
    print("  python run.py              # Generate all timetables")
    print("  python run.py generate     # Same as above")
    print("  python run.py enhanced     # Run with logging and metrics")
    print()
    print("Configuration:")
    print("  Edit src/config/config.json to customize settings")
    print()
    print("Input Data:")
    print("  Place your CSV files in the data/ directory:")
    print("  - data/Combined.csv (course data)")
    print("  - data/Rooms.csv (room data)")
    print()
    print("Output Files (saved to output/ directory):")
    print("  - output/timetable_all_departments.xlsx    (all department timetables)")
    print("  - output/all_faculty_timetables.xlsx       (individual faculty schedules)")
    print("  - output/unscheduled_courses.xlsx          (conflict analysis report)")
    print()
    print("  Logs will be saved to logs/ directory (enhanced mode only)")

if __name__ == "__main__":
    main()
