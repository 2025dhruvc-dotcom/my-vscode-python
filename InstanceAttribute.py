class Student:
    def __init__(self):
        self.name = "Amit"  
s1 = Student()
s2 = Student()

s2.name = "Neha"

print(s1.name)
print(s2.name)