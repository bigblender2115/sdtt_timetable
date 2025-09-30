# SDTT Automated Timetable Project

**SDTT Timetable** is a Python-based project to automate the generation and management of academic timetables. It supports scheduling for courses, classrooms, exams, and faculty availability while considering constraints and validations.

## Features

- Manage **courses, classrooms, students, and faculty** data efficiently.
- Define **exam schedules** with automatic constraint checking.
- Generate optimized class schedules using **custom scheduling algorithms**.
- Validate input data to ensure correctness before scheduling.
- Visualize generated timetables with simple visual aids.
- Includes CSV templates for easy data input and testing.

## Project Structure

SDTT_Timetable/
├── data/
│   └── templates/                  # CSV templates for input data
├── timetable/
│   ├── models/                      # Data models (Course, Exam, Faculty, etc.)
│   ├── scheduler/                   # Scheduling logic and constraints
│   ├── utils/                        # I/O, validation, and visualization utilities
│   ├── config.py                     # Project configuration
│   └── main.py                       # Entry point for the project
├── tests/                            # Unit tests
├── LICENSE
├── README.md
├── pyproject.toml
├── requirements.txt
└── setup.py