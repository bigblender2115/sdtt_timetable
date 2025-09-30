class Course:
    def __init__(self, code, name, semester, department, credits, instructor, elective=False, half_sem=False):
        self.code = code
        self.name = name
        self.semester = semester
        self.department = department
        self.credits = credits
        self.instructor = instructor
        self.elective = elective
        self.half_sem = half_sem
