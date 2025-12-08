class Person:
    def __init__ (self,name):
        self.name = name
    
    def show(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self, name, rollno):
        super().__init__(name)
        self.rollno = rollno

    def display(self):
        print("Roll Number:",self.rollno)
    
s1 = Student("Alice", 101)
s1.show()
s1.display()
print("\n")
p1 = Person("Bob")
p1.show()
#p1.display()  # This will raise an AttributeError since Person has no display method
