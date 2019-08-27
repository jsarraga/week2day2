from classes.person import Person


class Teacher(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
        self.role = "Teacher"

    def fullname(self):
        return "Prof. {} {}".format(self.firstname, self.lastname)