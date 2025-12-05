class InsufficientBalanceError(Exception):
    def __init__(self):
        super().__init__("Insufficient balance to perform this operation.")


class ATMaccount:
    def __init__(self, balance):
        self.balance = balance  

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError()
        self.balance -= amount
        print(f"Withdrew {amount}. New balance is {self.balance}.")
        print("Withdrawal successful.")
        return self.balance     


try:
    account = ATMaccount(500)  # Initial balance

    # Attempt to withdraw an amount greater than the balance
    account.withdraw(500)

except InsufficientBalanceError as e:
    print(e)

except Exception as e:
    print(f"An error occurred: {e}")

