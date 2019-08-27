import os


class Course:

    def __init__(self, title, code):
        self.title = title
        self.code = code
        self.teacher = None
        self.students = []

    def add(self, student):
        """ add one student or a sequence of students """
        try:
            self.students.extend(student)
        except TypeError:
            self.students.append(student)
        
    def drop(self, student):
        try:
            for each in student:
                self.students.remove(each)
        except TypeError:
            self.students.remove(student)

    def set_teacher(self, teacher):
        self.teacher = teacher

    def report(self):
        pass
