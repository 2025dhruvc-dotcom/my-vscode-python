
print("--------------------------------------------------------------------")


class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        print("Name:", name ,"|", "Roll Number:", roll)

# Example usage:
student1 = Student("Alice", 101)  

print("--------------------------------------------------------------------")


#New Example
class Marksheet:
    def __init__(self, name, rollno, m1, m2, m3):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.percentage = (m1 + m2 + m3) / 3
        self.show_report()

    def show_report(self):
        print("\n ----- Marksheet ----- \n")
        print("Name:", self.name)
        print("Roll Number:", self.rollno)
        print("Marks in English:", self.m1)
        print("Marks in Marathi:", self.m2)
        print("Marks in Hindi:", self.m3)
        print("Percentage:", self.percentage)


name = input("Enter Student Name : ")
rollno = int(input("Enter Roll Number : "))
m1 = int(input("Enter Marks in English : "))
m2 = int(input("Enter Marks in Marathi : "))
m3 = int(input("Enter Marks in Hindi : "))

s1 = Marksheet(name,rollno, m1, m2, m3)
