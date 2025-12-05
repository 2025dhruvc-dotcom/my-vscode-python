print("-----------------------------------------------------------")
print("\n Student Details:\n")
class Students:
    name = ""
    rollno = 0
    
    def display(self):
        print("Name:",self.name)
        print("Rollno:",self.rollno)

s1 = Students()
s1.name = "Dhruv"
s1.rollno = 101
s1.display()


print("\n-----------------------------------------------------------")

print("\n Employee Details:\n")
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
e1.name = "Amit"
e1.empid = 501
e1.company = "Google"
e1.email = "chavdadhruv@gmail.com"
e1.display()

print("-----------------------------------------------------------")