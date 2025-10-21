# 📖 Usage Guide

## Quick Start

### 1. Basic Timetable Generation
```bash
# Run the original generator
python src/core/main.py

# Run enhanced version with all features
python src/run.py enhanced

# Run with conflict resolution
python src/run.py conflict
```

### 2. Configuration Setup
1. Copy example configuration:
   ```bash
   cp examples/example_config.json src/config/config.json
   ```

2. Edit `src/config/config.json` to customize settings

3. Run with custom configuration:
   ```bash
   python src/run.py enhanced
   ```

## Advanced Usage

### Priority-Based Scheduling
The system schedules courses in this order:
1. **Core Courses** (CS, EC, MA, PH courses)
2. **Basket Electives** (B1-B9 groups)
3. **Regular Electives** (Other lecture courses)
4. **Tutorials** (T component > 0)
5. **Labs** (P component > 0)
6. **Self-Study** (S component only)

### Conflict Resolution
- **Auto-retry**: Up to 10 attempts with different random seeds
- **Alternative slots**: Suggests 5 best alternative time slots
- **Conflict analysis**: Detailed reports on scheduling issues

### Parallel Processing
- Automatically enabled for datasets > 10 courses
- Configurable worker count (default: 4)
- Memory optimization for large timetables

## Configuration Options

### Time Settings
```json
{
  "timetable_settings": {
    "start_time": "09:00",
    "end_time": "18:30",
    "slot_duration_minutes": 30
  }
}
```

### Scheduling Options
```json
{
  "scheduling": {
    "max_retry_attempts": 10,
    "priority_order": ["core_courses", "basket_electives", ...]
  }
}
```

### Optimization Settings
```json
{
  "optimization": {
    "enable_parallel_processing": true,
    "max_workers": 4,
    "memory_optimization": true
  }
}
```

## Input Data Requirements

### Course Data (Combined.csv)
Required columns:
- `Department`: Course department (CSE, ECE, etc.)
- `Semester`: Semester number
- `Course Code`: Unique course identifier
- `Course Name`: Course title
- `Faculty`: Instructor name
- `L`: Lecture hours
- `T`: Tutorial hours
- `P`: Practical hours
- `S`: Self-study hours
- `total_students`: Number of students

### Room Data (Rooms.csv)
Required columns:
- `id`: Room identifier
- `capacity`: Maximum occupancy
- `type`: Room type (LECTURE_ROOM, COMPUTER_LAB, etc.)
- `roomNumber`: Physical room number

## Output Files

### Generated Files
- `output/timetable.xlsx`: Main timetable output
- `logs/timetable_generation.log`: Generation log
- `conflict_suggestions.json`: Alternative slot suggestions

### Timetable Features
- Color-coded by course type
- Basket electives grouped by time slots
- Faculty conflict prevention
- Room capacity optimization
- Unscheduled components report

## Troubleshooting

### Common Issues

1. **No courses scheduled**
   - Check CSV file format
   - Verify column names
   - Ensure valid data types

2. **Too many conflicts**
   - Increase `max_retry_attempts`
   - Adjust room capacities
   - Review faculty assignments

3. **Performance issues**
   - Enable parallel processing
   - Reduce dataset size
   - Check memory usage

### Debug Mode
Enable detailed logging:
```json
{
  "logging": {
    "enable_logging": true,
    "log_level": "DEBUG"
  }
}
```

## Best Practices

1. **Data Preparation**
   - Validate CSV files before processing
   - Ensure unique course codes
   - Check room capacity vs. student count

2. **Configuration**
   - Start with example configuration
   - Test with small datasets first
   - Gradually increase complexity

3. **Performance**
   - Use parallel processing for large datasets
   - Monitor memory usage
   - Enable caching for repeated runs

4. **Quality Assurance**
   - Review unscheduled components
   - Check conflict suggestions
   - Validate room allocations
