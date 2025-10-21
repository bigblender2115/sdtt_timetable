"""
Conflict Resolution and Alternative Slot Suggestion System
"""

import json
import logging
from datetime import time, timedelta
from typing import Dict, List, Tuple, Optional, Set
from collections import defaultdict

class AlternativeSlotFinder:
    """Finds alternative time slots for unscheduled courses"""
    
    def __init__(self, config: dict):
        self.config = config
        self.days = config['timetable_settings']['days']
        self.start_time = time(*map(int, config['timetable_settings']['start_time'].split(':')))
        self.end_time = time(*map(int, config['timetable_settings']['end_time'].split(':')))
        self.slot_duration = config['timetable_settings']['slot_duration_minutes']
        
    def generate_time_slots(self) -> List[Tuple[time, time]]:
        """Generate all available time slots"""
        slots = []
        current_time = self.start_time
        while current_time < self.end_time:
            next_time = time(
                current_time.hour,
                (current_time.minute + self.slot_duration) % 60
            )
            if (current_time.minute + self.slot_duration) >= 60:
                next_time = time(current_time.hour + 1, (current_time.minute + self.slot_duration) % 60)
            slots.append((current_time, next_time))
            current_time = next_time
        return slots
    
    def find_available_slots(self, timetable: Dict, course_duration: int, 
                           faculty_schedule: Dict, room_availability: Dict) -> List[Tuple[int, int]]:
        """Find available slots for a course"""
        available_slots = []
        total_slots = len(self.generate_time_slots())
        
        for day in range(len(self.days)):
            for start_slot in range(total_slots - course_duration + 1):
                # Check if all required slots are free
                if self._is_slot_available(day, start_slot, course_duration, 
                                         timetable, faculty_schedule, room_availability):
                    available_slots.append((day, start_slot))
        
        return available_slots
    
    def _is_slot_available(self, day: int, start_slot: int, duration: int,
                          timetable: Dict, faculty_schedule: Dict, room_availability: Dict) -> bool:
        """Check if a slot is available"""
        for i in range(duration):
            slot_idx = start_slot + i
            if slot_idx in timetable.get(day, {}):
                return False
            if slot_idx in faculty_schedule.get(day, set()):
                return False
            if not room_availability.get(day, {}).get(slot_idx, True):
                return False
        return True
    
    def suggest_alternative_times(self, course_info: dict, timetable: Dict, 
                                faculty_schedule: Dict, room_availability: Dict) -> List[dict]:
        """Suggest alternative time slots for a course"""
        course_duration = self._get_course_duration(course_info)
        available_slots = self.find_available_slots(timetable, course_duration, 
                                                  faculty_schedule, room_availability)
        
        suggestions = []
        max_suggestions = self.config['scheduling']['conflict_resolution']['max_alternative_suggestions']
        
        for day, start_slot in available_slots[:max_suggestions]:
            time_slots = self.generate_time_slots()
            start_time = time_slots[start_slot][0]
            end_time = time_slots[start_slot + course_duration - 1][1]
            
            suggestions.append({
                'day': self.days[day],
                'start_time': start_time.strftime('%H:%M'),
                'end_time': end_time.strftime('%H:%M'),
                'day_index': day,
                'slot_index': start_slot,
                'duration_slots': course_duration,
                'priority_score': self._calculate_priority_score(day, start_slot, course_duration)
            })
        
        # Sort by priority score (higher is better)
        suggestions.sort(key=lambda x: x['priority_score'], reverse=True)
        return suggestions
    
    def _get_course_duration(self, course_info: dict) -> int:
        """Get course duration in slots"""
        durations = self.config['course_durations']
        
        if course_info.get('type') == 'LEC':
            return durations['lecture_duration_slots']
        elif course_info.get('type') == 'LAB':
            return durations['lab_duration_slots']
        elif course_info.get('type') == 'TUT':
            return durations['tutorial_duration_slots']
        else:
            return durations['lecture_duration_slots']  # Default
    
    def _calculate_priority_score(self, day: int, start_slot: int, duration: int) -> int:
        """Calculate priority score for a time slot"""
        score = 0
        
        # Prefer morning slots (9-12)
        if 0 <= start_slot <= 6:
            score += 10
        
        # Prefer afternoon slots (2-5)
        elif 10 <= start_slot <= 16:
            score += 8
        
        # Avoid lunch time slots
        if 7 <= start_slot <= 9:
            score -= 5
        
        # Prefer consecutive days
        if day in [0, 1, 2, 3]:  # Monday-Thursday
            score += 5
        
        return score

class ConflictAnalyzer:
    """Analyzes and categorizes scheduling conflicts"""
    
    def __init__(self, config: dict):
        self.config = config
        
    def analyze_conflicts(self, unscheduled_components: Set) -> Dict:
        """Analyze and categorize conflicts"""
        conflicts = {
            'faculty_conflicts': [],
            'room_conflicts': [],
            'time_conflicts': [],
            'capacity_conflicts': [],
            'department_conflicts': []
        }
        
        for component in unscheduled_components:
            reason = component.reason.lower()
            
            if 'faculty' in reason:
                conflicts['faculty_conflicts'].append({
                    'course': component.code,
                    'faculty': component.faculty,
                    'reason': component.reason,
                    'department': component.department,
                    'semester': component.semester
                })
            elif 'room' in reason:
                conflicts['room_conflicts'].append({
                    'course': component.code,
                    'reason': component.reason,
                    'department': component.department,
                    'semester': component.semester
                })
            elif 'time' in reason or 'slot' in reason:
                conflicts['time_conflicts'].append({
                    'course': component.code,
                    'reason': component.reason,
                    'department': component.department,
                    'semester': component.semester
                })
            elif 'capacity' in reason:
                conflicts['capacity_conflicts'].append({
                    'course': component.code,
                    'reason': component.reason,
                    'department': component.department,
                    'semester': component.semester
                })
            else:
                conflicts['department_conflicts'].append({
                    'course': component.code,
                    'reason': component.reason,
                    'department': component.department,
                    'semester': component.semester
                })
        
        return conflicts
    
    def generate_conflict_report(self, conflicts: Dict) -> str:
        """Generate a human-readable conflict report"""
        report = "=== SCHEDULING CONFLICT ANALYSIS ===\n\n"
        
        total_conflicts = sum(len(conflict_list) for conflict_list in conflicts.values())
        report += f"Total Conflicts: {total_conflicts}\n\n"
        
        for conflict_type, conflict_list in conflicts.items():
            if conflict_list:
                report += f"{conflict_type.replace('_', ' ').title()} ({len(conflict_list)}):\n"
                for conflict in conflict_list:
                    report += f"  - {conflict['course']} ({conflict['department']} {conflict['semester']}): {conflict['reason']}\n"
                report += "\n"
        
        return report
    
    def suggest_resolutions(self, conflicts: Dict) -> Dict:
        """Suggest resolutions for different types of conflicts"""
        suggestions = {
            'faculty_conflicts': [],
            'room_conflicts': [],
            'time_conflicts': [],
            'general_suggestions': []
        }
        
        # Faculty conflict suggestions
        if conflicts['faculty_conflicts']:
            suggestions['faculty_conflicts'].extend([
                "Consider hiring additional faculty for overloaded courses",
                "Redistribute courses among existing faculty",
                "Schedule courses at different times to avoid faculty conflicts",
                "Use teaching assistants for large courses"
            ])
        
        # Room conflict suggestions
        if conflicts['room_conflicts']:
            suggestions['room_conflicts'].extend([
                "Increase room capacity or find larger rooms",
                "Schedule courses at different times",
                "Use alternative room types (labs for lectures if appropriate)",
                "Consider online or hybrid delivery for some courses"
            ])
        
        # Time conflict suggestions
        if conflicts['time_conflicts']:
            suggestions['time_conflicts'].extend([
                "Extend working hours (earlier start or later end)",
                "Use weekend slots for non-core courses",
                "Implement compressed scheduling",
                "Use alternative delivery methods"
            ])
        
        # General suggestions
        suggestions['general_suggestions'] = [
            "Review course prerequisites and dependencies",
            "Consider offering courses in multiple semesters",
            "Implement flexible scheduling with multiple time slots",
            "Use technology to optimize room utilization"
        ]
        
        return suggestions

class TimetableOptimizer:
    """Optimizes timetable generation with advanced algorithms"""
    
    def __init__(self, config: dict):
        self.config = config
        self.optimization_stats = {
            'improvements_found': 0,
            'conflicts_reduced': 0,
            'optimization_time': 0
        }
    
    def optimize_schedule(self, timetable: Dict, unscheduled_components: Set) -> Tuple[Dict, Set]:
        """Optimize the current schedule"""
        import time
        start_time = time.time()
        
        optimized_timetable = timetable.copy()
        optimized_unscheduled = set(unscheduled_components)
        
        # Try different optimization strategies
        optimized_timetable, optimized_unscheduled = self._optimize_room_allocation(
            optimized_timetable, optimized_unscheduled)
        
        optimized_timetable, optimized_unscheduled = self._optimize_time_slots(
            optimized_timetable, optimized_unscheduled)
        
        optimized_timetable, optimized_unscheduled = self._optimize_faculty_schedule(
            optimized_timetable, optimized_unscheduled)
        
        self.optimization_stats['optimization_time'] = time.time() - start_time
        
        return optimized_timetable, optimized_unscheduled
    
    def _optimize_room_allocation(self, timetable: Dict, unscheduled: Set) -> Tuple[Dict, Set]:
        """Optimize room allocation"""
        # Implementation would analyze room usage and suggest better allocations
        return timetable, unscheduled
    
    def _optimize_time_slots(self, timetable: Dict, unscheduled: Set) -> Tuple[Dict, Set]:
        """Optimize time slot assignments"""
        # Implementation would find better time slot arrangements
        return timetable, unscheduled
    
    def _optimize_faculty_schedule(self, timetable: Dict, unscheduled: Set) -> Tuple[Dict, Set]:
        """Optimize faculty schedule distribution"""
        # Implementation would balance faculty workload
        return timetable, unscheduled

def create_conflict_resolution_tools(config_file: str = 'config.json'):
    """Factory function to create conflict resolution tools"""
    with open(config_file, 'r') as f:
        config = json.load(f)
    
    return {
        'slot_finder': AlternativeSlotFinder(config),
        'conflict_analyzer': ConflictAnalyzer(config),
        'optimizer': TimetableOptimizer(config)
    }

if __name__ == "__main__":
    # Example usage
    tools = create_conflict_resolution_tools()
    
    # Example conflict analysis
    sample_conflicts = set()  # Would contain actual conflict data
    conflicts = tools['conflict_analyzer'].analyze_conflicts(sample_conflicts)
    report = tools['conflict_analyzer'].generate_conflict_report(conflicts)
    suggestions = tools['conflict_analyzer'].suggest_resolutions(conflicts)
    
    print(report)
    print("Suggestions:", json.dumps(suggestions, indent=2))
