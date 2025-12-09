class calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c=0):
        return a + b + c
    
calc = calculator()
print(calc.add(2, 3))  # Calls the second add method with two parameters



 