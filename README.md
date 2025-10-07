Timetable Generator
This Python script generates a timetable for academic courses, scheduling lectures, tutorials, labs, and self-study sessions while handling basket electives (B1, B2, B3, B4) in fixed time slots across all branches for a given semester.
Features

Input Files: Reads course data from courses.csv and room data from classrooms.csv.
Basket Electives: Schedules all electives within the same basket group (e.g., B1-001, B1-002) in a single slot:
B1: 9:00-10:30
B2: 10:30-12:00
B3: 14:00-15:30
B4: 15:30-17:00


Room Allocation: Assigns rooms based on course type and student capacity.
Lunch Breaks: Staggers lunch breaks between 12:30-14:00 for different semesters.
Output: Generates an Excel file (timetable.xlsx) with formatted timetables, including color-coded courses, breaks, and a legend.
Error Handling: Uses default data if input files are missing or contain errors (e.g., NaN values).

Requirements

Python 3.8+
Libraries: pandas, openpyxl

Install dependencies:
pip install pandas openpyxl

Input Files

courses.csv:

Columns: Department, Semester, Course Code, Course Name, Faculty, L (lecture hours), T (tutorial hours), P (practical hours), S (self-study hours), total_students
Example:Department,Semester,Course Code,Course Name,Faculty,L,T,P,S,total_students
CSE,3,CS101,Intro to CS,Prof A,3,1,2,0,140
ECE,3,B1-001,Elective 1A,Prof C,2,0,0,0,35




classrooms.csv:

Columns: id, capacity, type, roomNumber
Example:id,capacity,type,roomNumber
R1,70,LECTURE_ROOM,R101
L1,35,COMPUTER_LAB,L101





Usage

Place courses.csv and classrooms.csv in the same directory as the script.
Run the script:python timetable_generator.py


Check the output timetable.xlsx for the generated timetable.

Output

timetable.xlsx: Contains one sheet per department-semester-section (e.g., CSE_3_A).
Each sheet includes:
Timetable grid with days and time slots (9:00-18:30).
Color-coded courses (basket electives and regular courses).
Lunch breaks marked in gray.
Self-study courses listed below the timetable.
Unscheduled components with reasons (if any).
Legend with course codes, names, faculty, and colors.



Notes

Basket electives are grouped by basket (B1, B2, B3, B4) and scheduled in fixed slots across all branches in a semester.
Colors are visually appealing (soft coral, mint, pale blue, warm yellow for baskets; pastel shades for others).
If input files are missing, the script uses default data (sample courses and rooms).
Ensure sufficient room capacity for basket electives, as they combine students from multiple branches.

Troubleshooting

Missing Files: The script will use default data and print warnings.
NaN Values: Handled by filling with defaults (e.g., 0 for hours, 60 for students).
Unscheduled Courses: Check the "Unscheduled Components" section in the output for conflicts or insufficient rooms.
