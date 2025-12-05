print("-----------------------------------------------------------")
print("\n 😈Student Details😈:\n")
class Students:
    name = ""
    rollno = 0
    
    def display(self):
        print("Name:",self.name)
        print("Rollno:",self.rollno)

s1 = Students()
s1.name = input("Enter Student Name: ")
s1.rollno = input("Enter Roll Number: ")



print("\n-----------------------------------------------------------")

print("\n 💀Employee Details:\n")
class employee:
    name = ""
    empid = 0
    company = ""
    email = ""
    def display(self):
        print("Name:",self.name)
        print("Employee ID:",self.empid)
        print("Company:",self.company)
        print("Email:",self.email)

e1 = employee()
e1.name = input("Enter Employee Name: ")
e1.empid = input("Enter Employee ID: ")
e1.company = input("Enter Company Name: ")
e1.email = input("Enter Email ID: ")

print("-----------------------------------------------------------")