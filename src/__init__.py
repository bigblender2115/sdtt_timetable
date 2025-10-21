"""
Enhanced Timetable Generator Package

A comprehensive system for generating academic timetables with advanced features:
- Conflict resolution and auto-retry
- Priority-based scheduling
- Parallel processing optimization
- Configuration management
- Alternative slot suggestions
"""

__version__ = "2.0.0"
__author__ = "Timetable Generator Team"
__description__ = "Enhanced Academic Timetable Generator with Advanced Features"

# Import main classes for easy access
try:
    from .core.main import generate_timetable
    from .optimization.enhanced_main import EnhancedTimetableGenerator
    from .optimization.conflict_resolver import create_conflict_resolution_tools
except ImportError:
    # Handle import errors gracefully
    pass

__all__ = [
    'generate_timetable',
    'EnhancedTimetableGenerator', 
    'create_conflict_resolution_tools'
]
