from classes import Teacher, Student, Course


compsci = Course("Computer Science 101", "CS101")
maria = Student("Maria", "Martinez")
joe = Student("Joe", "Smith")
ashven = Student("Ashven", "Matthew")

imani = Teacher("Imani", "Matthews")

compsci.add([maria, joe, ashven])
compsci.set_teacher(imani)

print(compsci.teacher, compsci.students)

joe.addgrade(compsci, 80)
joe.addgrade(compsci, 89)
joe.addgrade(compsci, 100)

print()
print("GPA for {} is {:.2f}.".format(joe, joe.gpa_for(compsci)))