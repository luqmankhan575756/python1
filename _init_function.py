class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Add new student in database")

# create objects
s1 = Student("karan", 55)
print(s1.name, s1.marks)

s2 = Student("karan khan", 88)
print(s2.name, s2.marks)

