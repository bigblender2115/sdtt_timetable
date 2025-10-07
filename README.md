# 🗓️ Timetable Generator

A Python script to **generate academic timetables**, scheduling lectures, tutorials, labs, and self-study sessions.  
Basket electives (B1–B4) are grouped in **fixed time slots** across all branches for a semester.

---

## 🚀 Features

- Reads **course data (`courses.csv`)** and **room data (`classrooms.csv`)**
- Schedules **basket electives** in fixed slots:
  - **B1:** 9:00–10:30  
  - **B2:** 10:30–12:00  
  - **B3:** 14:00–15:30  
  - **B4:** 15:30–17:00
- Assigns rooms based on course type and student capacity  
- Staggers **lunch breaks (12:30–14:00)**  
- Outputs `timetable.xlsx` with **color-coded schedules and legend**
- Handles **missing files** or **NaN values** with sensible defaults

---

## 🧩 Requirements

- **Python 3.8+**
- Libraries:  
  ```bash
  pip install pandas openpyxl


## 📂 Input Files

### `courses.csv`

| Department | Semester | Course Code | Course Name   | Faculty | L | T | P | S | total_students |
|-------------|-----------|--------------|----------------|----------|---|---|---|----------------|
| CSE | 3 | CS101 | Intro to CS | Prof A | 3 | 1 | 2 | 0 | 140 |
| ECE | 3 | B1-001 | Elective 1A | Prof C | 2 | 0 | 0 | 0 | 35 |

---

### `classrooms.csv`

| id | capacity | type | roomNumber |
|----|-----------|----------------|-------------|
| R1 | 70 | LECTURE_ROOM | R101 |
| L1 | 35 | COMPUTER_LAB | L101 |

## ⚙️ Usage

1. Place the input files — **`courses.csv`** and **`classrooms.csv`** — in the same directory as **`timetable_generator.py`**.

2. Run the script using Python:
   ```bash
   python timetable_generator.py

## 📊 Output

- **File:** `timetable.xlsx`
- **Contents:** One sheet per department-semester-section (e.g., `CSE_3_A`)
- **Includes:**
  - Timetable grid (9:00–18:30, Monday–Friday)
  - Color-coded courses (basket electives and regular)
  - Lunch breaks in gray
  - Self-study courses and unscheduled components
  - Legend for color codes

---

## 🎨 Color Codes

| Category | Color |
|-----------|--------|
| **B1** | Soft Coral |
| **B2** | Mint |
| **B3** | Pale Blue |
| **B4** | Warm Yellow |
| **Others** | Light Pastels |

---

## 🧠 Notes

- Basket electives (e.g., `B1-001`, `B1-002`) share a **single slot** across all branches.
- Defaults are used if input files are missing.
- Ensure **room capacity** is sufficient for basket electives.
- The script auto-handles missing or incomplete data gracefully.

---

## 🧰 Troubleshooting

| Issue | Cause | Fix |
|--------|--------|-----|
| **Missing files** | `courses.csv` or `classrooms.csv` not found | Script uses default data and prints a warning |
| **NaN values** | Empty cells in CSV | Defaults to `0` (hours) or `60` (students) |
| **Unscheduled courses** | Conflicts or no available room | Check the **"Unscheduled Components"** sheet in the output |

