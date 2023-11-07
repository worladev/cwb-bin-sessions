'''
IN SESSION 18 CODING CHALLENGE (09/10/2023)
Mentor and Facilitator ==> ANDY AFFUL

PROBLEM STATEMENT:
You are tasked with creating a Python class GradeTracker to manage students' grades. The class should have the
following functionalities:

- Initialization: The class should initialize with an empty dictionary to store student names as keys and their
  corresponding grades as values.

- Adding Grades: Implement a method add_grade(name, grade) that takes a student's name (a string) and a grade
(an integer), and adds the grade to the student's record. If the student is not already in the records, add them.

- Getting Grades: Implement a method grades(name) that takes a student's name and returns a list of their grades
in ascending order.
'''
class GradeTracker:
    def __init__(self):
        self.grade_records = {}

    def add_grade(self, name, grade):
        if name in self.grade_records:
            self.grade_records[name].append(grade)
        else:
            self.grade_records[name] = [grade]

    def grades(self, name):
        return sorted(self.grade_records.get(name, []))


# Example Usage:
tracker = GradeTracker()
