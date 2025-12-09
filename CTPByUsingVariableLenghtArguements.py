class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(2))
print(calc.add(2, 3))
print(calc.add(2, 3, 4))
