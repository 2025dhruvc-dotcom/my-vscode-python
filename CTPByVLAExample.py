class Calculator:
    def add(self, *args):
        choose = input("Choose operator (*,+,-,/): ")

        if choose == "+":
            print("Addition:", args[0] + args[1])
        elif choose == "-":
            print("Subtraction:", args[0] - args[1])
        elif choose == "*":
            print("Multiplication:", args[0] * args[1])
        elif choose == "/":
            print("Division:", args[0] / args[1])
        else:
            print("Invalid operator")

c = Calculator()

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

c.add(a, b)

