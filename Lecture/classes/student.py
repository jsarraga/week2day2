import math
from classes.person import Person


class Student(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        self.grades = {}
        self.role = "Student"
    
    def addgrade(self, course, grade):
        gradelist = self.grades.get(course.code, [])
        gradelist.append(float(grade))
        self.grades[course.code] = gradelist

    def gpa_for(self, course):
        if course.code not in self.grades.keys():
            raise KeyError
        gradelist = self.grades[course.code]
        if len(gradelist) == 0:
            return None
        return sum(gradelist) / len(gradelist)

    @classmethod
    def create_many(cls, namelist):
        newkids = []
        for firstname, lastname in namelist:
            newkids.append(cls(firstname, lastname))
        return newkids
