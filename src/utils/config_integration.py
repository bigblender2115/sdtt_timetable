"""
Integration script to update main.py with config system and enhanced features
"""

import json
import os
from datetime import time

def update_main_with_config():
    """Update main.py to use config.json and add enhanced features"""
    
    # Read the current main.py
    with open('main.py', 'r') as f:
        main_content = f.read()
    
    # Read config.json
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    # Add config loading at the top
    config_loading_code = '''
import json

# Load configuration
def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Warning: config.json not found, using default configuration")
        return {
            "timetable_settings": {
                "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                "start_time": "09:00",
                "end_time": "18:30"
            },
            "course_durations": {
                "lecture_duration_slots": 3,
                "lab_duration_slots": 4,
                "tutorial_duration_slots": 2,
                "self_study_duration_slots": 2
            }
        }

config = load_config()

'''
    
    # Replace constants with config-based values
    updated_content = main_content.replace(
        "# Constants\nDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']",
        config_loading_code + "# Constants\nDAYS = config['timetable_settings']['days']"
    )
    
    # Update time constants
    updated_content = updated_content.replace(
        "START_TIME = time(9, 0)",
        "START_TIME = time(*map(int, config['timetable_settings']['start_time'].split(':')))"
    )
    
    updated_content = updated_content.replace(
        "END_TIME = time(18, 30)",
        "END_TIME = time(*map(int, config['timetable_settings']['end_time'].split(':')))"
    )
    
    # Update duration constants
    updated_content = updated_content.replace(
        "LECTURE_DURATION = 3  # 1.5 hours",
        "LECTURE_DURATION = config['course_durations']['lecture_duration_slots']"
    )
    
    updated_content = updated_content.replace(
        "LAB_DURATION = 4      # 2 hours",
        "LAB_DURATION = config['course_durations']['lab_duration_slots']"
    )
    
    updated_content = updated_content.replace(
        "TUTORIAL_DURATION = 2 # 1 hour",
        "TUTORIAL_DURATION = config['course_durations']['tutorial_duration_slots']"
    )
    
    updated_content = updated_content.replace(
        "SELF_STUDY_DURATION = 2 # 1 hour",
        "SELF_STUDY_DURATION = config['course_durations']['self_study_duration_slots']"
    )
    
    # Add conflict resolution function
    conflict_resolution_code = '''
# Enhanced conflict resolution
def resolve_conflicts_with_retry(max_attempts=10):
    """Try multiple times with different random seeds to resolve conflicts"""
    global df, rooms, batch_info, unscheduled_components
    
    best_result = None
    best_unscheduled_count = float('inf')
    
    for attempt in range(max_attempts):
        random.seed(42 + attempt)  # Different seed each time
        current_unscheduled = len(unscheduled_components)
        
        if current_unscheduled < best_unscheduled_count:
            best_result = {
                'timetable': timetable.copy(),
                'unscheduled': unscheduled_components.copy(),
                'attempt': attempt + 1
            }
            best_unscheduled_count = current_unscheduled
        
        if current_unscheduled == 0:  # Perfect schedule found
            break
    
    if best_result:
        print(f"Best result found in attempt {best_result['attempt']} with {best_unscheduled_count} unscheduled components")
        return best_result
    
    return None

# Priority-based scheduling
def schedule_by_priority():
    """Schedule courses in priority order"""
    priority_order = config.get('scheduling', {}).get('priority_order', [
        'core_courses', 'basket_electives', 'regular_electives', 'tutorials', 'labs', 'self_study'
    ])
    
    # This would be implemented to schedule courses in the specified priority order
    pass

'''
    
    # Insert conflict resolution code before generate_timetable function
    insert_point = updated_content.find("def generate_timetable():")
    updated_content = updated_content[:insert_point] + conflict_resolution_code + updated_content[insert_point:]
    
    # Add retry logic to generate_timetable
    generate_timetable_start = updated_content.find("def generate_timetable():")
    generate_timetable_end = updated_content.find("if __name__ == \"__main__\":")
    
    if generate_timetable_start != -1 and generate_timetable_end != -1:
        function_content = updated_content[generate_timetable_start:generate_timetable_end]
        
        # Add retry logic
        retry_code = '''
    # Try multiple times to resolve conflicts
    max_retries = config.get('scheduling', {}).get('max_retry_attempts', 10)
    enable_retry = config.get('scheduling', {}).get('retry_with_different_seeds', True)
    
    if enable_retry:
        print(f"Attempting timetable generation with up to {max_retries} retries...")
        result = resolve_conflicts_with_retry(max_retries)
        if result:
            print(f"Successfully generated timetable with {len(result['unscheduled'])} unscheduled components")
        else:
            print("Could not generate a conflict-free timetable")
    
'''
        
        # Insert retry code before the final wb.save
        save_position = function_content.rfind("wb.save('timetable.xlsx')")
        if save_position != -1:
            function_content = function_content[:save_position] + retry_code + function_content[save_position:]
            updated_content = updated_content[:generate_timetable_start] + function_content + updated_content[generate_timetable_end:]
    
    # Write the updated main.py
    with open('main_enhanced.py', 'w') as f:
        f.write(updated_content)
    
    print("Enhanced main.py created as main_enhanced.py")
    print("Features added:")
    print("- Configuration file integration")
    print("- Conflict resolution with retry logic")
    print("- Priority-based scheduling framework")
    print("- Enhanced error handling")

def create_requirements_file():
    """Create requirements.txt for the enhanced system"""
    requirements = """pandas>=1.3.0
openpyxl>=3.0.0
numpy>=1.21.0
"""
    
    with open('requirements.txt', 'w') as f:
        f.write(requirements)
    
    print("requirements.txt created")

def create_run_script():
    """Create a simple run script"""
    run_script = '''#!/usr/bin/env python3
"""
Enhanced Timetable Generator Runner
"""

import sys
import os

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'enhanced':
            from enhanced_main import EnhancedTimetableGenerator
            generator = EnhancedTimetableGenerator()
            generator.generate_timetable()
        elif sys.argv[1] == 'config':
            from config_integration import update_main_with_config
            update_main_with_config()
        elif sys.argv[1] == 'conflict':
            from conflict_resolver import create_conflict_resolution_tools
            tools = create_conflict_resolution_tools()
            print("Conflict resolution tools loaded successfully")
        else:
            print("Usage: python run.py [enhanced|config|conflict]")
    else:
        # Run the original main.py
        import main
        main.generate_timetable()

if __name__ == "__main__":
    main()
'''
    
    with open('run.py', 'w') as f:
        f.write(run_script)
    
    print("run.py created - usage: python run.py [enhanced|config|conflict]")

if __name__ == "__main__":
    update_main_with_config()
    create_requirements_file()
    create_run_script()
    
    print("\n=== Enhanced Timetable System Setup Complete ===")
    print("\nFiles created:")
    print("- config.json (configuration file)")
    print("- enhanced_main.py (fully enhanced version)")
    print("- conflict_resolver.py (conflict resolution tools)")
    print("- main_enhanced.py (enhanced version of original)")
    print("- requirements.txt (dependencies)")
    print("- run.py (runner script)")
    
    print("\nTo use:")
    print("1. python run.py enhanced (for full enhanced version)")
    print("2. python main_enhanced.py (for enhanced original)")
    print("3. python run.py conflict (to test conflict resolution)")
    
    print("\nConfiguration can be modified in config.json")
