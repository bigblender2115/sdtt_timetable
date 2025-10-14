### Unit Test Case Matrix

| Test case input | Description | Expected output |
| --- | --- | --- |
| `generate_time_slots()` | Generates half-hour slots between `START_TIME` and `END_TIME` | 19 slots; first `(09:00,09:30)`, last `(18:00,18:30)` |
| `calculate_lunch_breaks([3])` | Single semester lunch window | `lunch_breaks[3]` starts `12:30`, duration `60` mins |
| `calculate_lunch_breaks([3,5])` | Two semesters staggered | starts: `[12:30, 13:00]`, each 60 mins |
| `calculate_lunch_breaks([3,5,7])` | Three semesters staggered | starts: `[12:30, 12:45, 13:00]`, each 60 mins |
| `is_basket_course("B1-001")` | Basket detection true case | `True` |
| `is_basket_course("CS101")` | Basket detection false case | `False` |
| `get_basket_group("B3-999")` | Extract basket group | `"B3"` |
| `get_required_room_type({P:0, code:CS101})` | No practicals -> lecture | `"LECTURE_ROOM"` |
| `get_required_room_type({P:2, code:CS201})` | CS with practicals -> computer lab | `"COMPUTER_LAB"` |
| `get_required_room_type({P:2, code:EC101})` | EC with practicals -> hardware lab | `"HARDWARE_LAB"` |
| `calculate_required_slots({L:3,T:1,P:2,S:0})` | Mixed L/T/P | `(2,1,1,0)` |
| `calculate_required_slots({L:0,T:2,P:0,S:4})` | T with self-study | `(0,2,0,1)` |
| `calculate_required_slots({L:0,T:0,P:0,S:8})` | S only | `(0,0,0,0)` |
| `try_room_allocation` with R1(50) R2(120) and conflict | Capacity and conflict handling | `None` when conflict; `"R2"` when freed |
| `is_break_time(slot within lunch)` | Uses `lunch_breaks` to detect break | `True` |
| `generate_timetable()` (smoke) | End-to-end default generation | `timetable.xlsx` file created |

Notes
- Expected outputs align with constants in `main.py` and course logic.
- The smoke test avoids file I/O side effects by running in a temp directory.

