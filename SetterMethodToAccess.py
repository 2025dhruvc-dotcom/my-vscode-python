class Bank:
    def __init__(self,balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    
    def set_balance(self,amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount. Balance cannot be negative.")

b = Bank(20000)
b.set_balance(2000)
print(b.get_balance())


