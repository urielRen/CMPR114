# Uriel Renteria
# 4/15/23

class Teacher:
    def __init__(self, name, classRoom, course):
        self.name = name
        self.classRoom = classRoom
        self.course = course

    def GetProfessor(self):
        print("Professor name is " + self.name)
        print("Professor assigned class is " + self.classRoom)
        print("Professor is teaching " + self.course)

Teacher1 = Teacher('Prof. Sim', 'A206', 'Python Programming')

Teacher1.GetProfessor()