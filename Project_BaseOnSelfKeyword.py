class Employee:
    def __init__(self, empid, name):
        self.empid = empid
        self.name = name
        self.attendace = 0

    def mark_attendance(self):

        self.attendace += 1
        print("\n---------------------------")
        print(f"Attendance marked for {self.name}. Total attendance: {self.attendace} days")   
        print("Attendance marking successful.")
        print("\n---------------------------")

    def display_info(self):
        print(f"Employee ID: {self.empid}, Name: {self.name}, Attendance: {self.attendace} days")
        print("\n---------------------------")

emp1 = Employee(101, "Raj")
emp1.mark_attendance()
emp1.mark_attendance()
emp1.display_info()     

emp2 = Employee(102, "Prince")
emp2.mark_attendance()
emp2.mark_attendance()
emp2.mark_attendance()

emp2.display_info()

emp3 = Employee(103, "Tejas")
emp3.display_info()
