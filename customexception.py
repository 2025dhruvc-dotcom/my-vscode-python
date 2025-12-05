class InsufficientBalanceError(Exception):
    def _int_(self):
        super()._init_(
           f"Insufficient balance to perform this operation."
        )

class ATMaccount():
    def _int_(self,balance):
         self.balance = balance  

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError()
        self.balance -= amount
        print(f"Withdrew {amount}. New balance is {self.balance}.")
        print("Withdrawal successful.")
        return self.balance     

try:
    account = ATMaccount()
    account.balance = 500  # Initial balance

    # Attempt to withdraw an amount greater than the balance
    account.withdraw(600)
except InsufficientBalanceError as e:
    print(e)
except Exception as e:
    print(f"An error occurred: {e}")        # Initial balance # Trying to withdraw more than balance