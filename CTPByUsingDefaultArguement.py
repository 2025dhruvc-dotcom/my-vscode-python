class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c
    
calc = Calculator()
print(calc.add(5))          # Calls add with one parameter, b and c default to
print(calc.add(5, 10))       # Calls add with two parameters, c defaults to 0
print(calc.add(5, 10, 15))    # Calls add with three parameters
