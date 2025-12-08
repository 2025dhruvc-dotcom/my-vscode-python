# ----------------- Base Class -----------------
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


# ----------------- Creating Objects -----------------
m1 = Manager("TEJAS CHAVAN", 101, 12)
d1 = Developer("SAKSHAM GHARAT", 102, "Python")
i1 = Intern("PRINCE YADAC", 103, 6)

# ----------------- Display Details -----------------
m1.show_info()
d1.show_info()
i1.show_info()