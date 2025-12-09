class BankAccount:
    def __init__(self,acc_holder,acc_number,balance):
        self.acc_holder = acc_holder
        self.acc_number = acc_number

        self.__balance = balance 

    def get_balance(self):
        return self.__balance
    
    def set_balance(self,amount):
        if amount >= 0:
            self.__balance = amount
            print(f"{amount}depositded successfully")
        else:
            print("Invalid amount")

    def wihtdraw(self,amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully")

    def show_account(self):
        print("\n ---- BANK ACCOUNT DETAILS ----")
        print("Account Holder:",self.acc_holder)
        print("Account Number:",self.acc_number)
        print("Account Balance:",self.__balance)

name = input("Enter account holder name:")
acc_no = input("Enter account number:")  
balance = float(input("Enter initial balance:"))

acc = BankAccount(name,acc_no,balance)

acc.show_account()

while True:
    print("\n----- MENU -----")
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance \n4. Exit")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        amount = float(input("Enter amount to deposit:"))
        acc.set_balance(amount)
    elif choice == 2:
        amount = float(input("Enter amount to withdraw:"))
        acc.wihtdraw(amount)
    elif choice == 3:
        acc.show_account()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")