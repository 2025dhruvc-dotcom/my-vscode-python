class Calculator:
    def add(self,a,b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + " " + b
        else:
            return "Invalid input types"
        
calc = Calculator()
print(calc.ad(5, 10))               # Calls ad with two integers
print(calc.ad("Hello", "World"))    # Calls ad with two strings
print(calc.ad(5, "World"))          # Calls ad with mixed types





