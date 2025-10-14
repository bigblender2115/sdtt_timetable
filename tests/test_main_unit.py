import os
from datetime import time

import pytest

import main as m


def test_generate_time_slots_count_and_bounds():
    slots = m.generate_time_slots()
    assert len(slots) == 19
    assert slots[0] == (m.START_TIME, time(9, 30))
    assert slots[-1] == (time(18, 0), m.END_TIME)


@pytest.mark.parametrize(
    "semesters, expected_starts",
    [
        ([3], [time(12, 30)]),
        ([3, 5], [time(12, 30), time(13, 0)]),
        ([3, 5, 7], [time(12, 30), time(12, 45), time(13, 0)]),
    ],
)
def test_calculate_lunch_breaks_staggering(semesters, expected_starts):
    m.calculate_lunch_breaks(semesters)
    assert set(m.lunch_breaks.keys()) == set(semesters)
    actual_starts = [m.lunch_breaks[s][0] for s in sorted(semesters)]
    assert actual_starts == expected_starts
    for sem in semesters:
        start, end = m.lunch_breaks[sem]
        assert (end.hour * 60 + end.minute) - (start.hour * 60 + start.minute) == m.LUNCH_DURATION


@pytest.mark.parametrize(
    "code, expected",
    [("B1-001", True), ("CS101", False), ("B2", False), ("B4-ABC", True)],
)
def test_is_basket_course(code, expected):
    assert m.is_basket_course(code) is expected


@pytest.mark.parametrize(
    "code, expected",
    [("B1-001", "B1"), ("CS101", None), ("B3-999", "B3")],
)
def test_get_basket_group(code, expected):
    assert m.get_basket_group(code) == expected


@pytest.mark.parametrize(
    "course, expected",
    [
        ({"Course Code": "CS101", "P": 0}, "LECTURE_ROOM"),
        ({"Course Code": "CS201", "P": 2}, "COMPUTER_LAB"),
        ({"Course Code": "DS301", "P": 4}, "COMPUTER_LAB"),
        ({"Course Code": "EC101", "P": 2}, "HARDWARE_LAB"),
        ({"Course Code": "MA101", "P": 2}, "COMPUTER_LAB"),
    ],
)
def test_get_required_room_type(course, expected):
    assert m.get_required_room_type(course) == expected


@pytest.mark.parametrize(
    "course, expected",
    [
        ({"L": 3, "T": 1, "P": 2, "S": 0}, (2, 1, 1, 0)),
        ({"L": 0, "T": 2, "P": 0, "S": 4}, (0, 2, 0, 1)),
        ({"L": 2, "T": 0, "P": 0, "S": 4}, (1, 0, 0, 1)),
        ({"L": 0, "T": 0, "P": 4, "S": 2}, (0, 0, 2, 0)),
        ({"L": 0, "T": 0, "P": 0, "S": 8}, (0, 0, 0, 0)),
    ],
)
def test_calculate_required_slots(course, expected):
    assert m.calculate_required_slots(course) == expected


def test_try_room_allocation_capacity_and_conflict():
    rooms = {
        "R1": {"capacity": 50, "schedule": {day: set() for day in range(len(m.DAYS))}},
        "R2": {"capacity": 120, "schedule": {day: set() for day in range(len(m.DAYS))}},
    }
    day = 0
    start_slot = 2
    duration = 3
    # Fill R2 for a conflicting slot to force skip when occupied
    rooms["R2"]["schedule"][day].add(start_slot + 1)
    chosen = m.try_room_allocation(rooms, "LEC", 70, day, start_slot, duration, used_room_ids=set())
    assert chosen is None  # R1 too small, R2 has conflict
    # Free R2 and expect it to be chosen
    rooms["R2"]["schedule"][day].clear()
    chosen = m.try_room_allocation(rooms, "LEC", 70, day, start_slot, duration, used_room_ids=set())
    assert chosen == "R2"


def test_is_break_time_uses_lunch_breaks():
    semesters = [3]
    m.calculate_lunch_breaks(semesters)
    lunch_start, lunch_end = m.lunch_breaks[3]
    assert m.is_break_time((lunch_start, time(lunch_start.hour, (lunch_start.minute + 30) % 60)), 3) is True
    assert m.is_break_time((time(9, 0), time(9, 30)), 3) is False


@pytest.mark.slow
def test_generate_timetable_smoke(tmp_path, monkeypatch):
    # Run in a temp cwd so output file is isolated
    monkeypatch.chdir(tmp_path)
    # Ensure no courses.csv, so default dataset path is taken
    m.generate_timetable()
    assert os.path.exists("timetable.xlsx")


