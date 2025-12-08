class Employee:
    def __init__(self, emp_name, emp_id):
        self.emp_name = emp_name
        self.emp_id = emp_id

    def show_basic_info(self):
        print("Name:", self.emp_name)
        print("Employee ID:", self.emp_id)


# ----------------- Class 1: Manager -----------------
class Manager(Employee):
    def __init__(self, emp_name, emp_id, team_size):
        super().__init__(emp_name, emp_id)
        self.team_size = team_size

    def show_info(self):
        print("\n===== MANAGER DETAILS =====")
        self.show_basic_info()
        print("Team Size:", self.team_size)


# ----------------- Class 2: Developer -----------------
class Developer(Employee):
    def __init__(self, emp_name, emp_id, programming_lang):
        super().__init__(emp_name, emp_id)
        self.programming_lang = programming_lang

    def show_info(self):
        print("\n===== DEVELOPER DETAILS =====")
        self.show_basic_info()
        print("Programming Language:", self.programming_lang)


# ----------------- Class 3: Intern -----------------
class Intern(Employee):
    def __init__(self, emp_name, emp_id, duration_months):
        super().__init__(emp_name, emp_id)
        self.duration_months = duration_months

    def show_info(self):
        print("\n===== INTERN DETAILS =====")
        self.show_basic_info()
        print("Internship Duration:", self.duration_months, "months")

while True:
    print("\n ===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Manager")
    print("2. Add Developer")
    print("3. Add Intern")
    print("4. Exit")
    choice = int(input("Enter your choice (1/2/3/4): "))

    if choice == 1:
        name = input("Enter Manager Name: ")
        emp_id = input("Enter Employee ID: ")
        team = int(input("Enter Team Size: "))

        m = Manager(name, emp_id, team)
        m.show_info()

    elif choice == 2:
        name = input("Enter Developer Name: ")
        emp_id = input("Enter Employee ID: ")
        lang = input("Enter Programming Language: ")

        d = Developer(name, emp_id, lang)
        d.show_info()

    elif choice == 3:
        name = input("Enter Intern Name: ")
        emp_id = input("Enter Employee ID: ")
        duration = int(input("Enter Duration (months): "))

        i = Intern(name, emp_id, duration)
        i.show_info()
    elif choice == 4:
        print("Exiting the system.")
        break
    else:
        print("Invalid Choice!")
        
    print("==============================================")