class Preferences:
    def __init__(self, year, branch, section, electives=None, minors=None, timetable_option=None):
        self.year = year
        self.branch = branch
        self.section = section
        self.electives = electives or []
        self.minors = minors or []
        self.timetable_option = timetable_option
