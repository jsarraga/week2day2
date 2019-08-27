import math


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.role = "Person"

    def fullname(self):
        return self.lastname + ", " + self.firstname

    def __str__(self):
        return "{}: {}".format(self.role, self.fullname())
