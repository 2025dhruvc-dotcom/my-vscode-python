class Student:
    college = "ABC College"  # Class Attribute
    def __init__(self, name):
        self.name = name  # Instance Attribute

s1 = Student("Amit")
s2 = Student("Neha")

print(s1.college)
print(s2.college)
Student.college = "XYZ University"
print(s1.college)
print(s2.college)
print(s1.name)  
print(s2.name)