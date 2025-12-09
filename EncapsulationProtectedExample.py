class Bank:
    def __init__(self, name, acc_no, balance):
        self._name = name
        self._acc_no = acc_no
        self._balance = balance
acc1 = Bank("John Doe", "123456789", 5000)
print("Account Holder:", acc1._name)
class Manager(Bank):
    def __init__(self, name, acc_no, balance, department):
        super().__init__(name, acc_no, balance)
        self._department = department
manager1 = Manager("Alice", "987654321", 10000, "Sales")
print("Manager Name:", manager1._name)
print("Department:", manager1._department)
print("Balance:", acc1._balance)


