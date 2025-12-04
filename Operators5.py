a = int(input("Enter first value( 0 for False,any nonzero for True ): "))
b = int(input("Enter second number( 0 for False,any nonzero for True ): "))
print("\nResults of logical operations :")
print(f"{a} and {b} →", bool(a) and bool(b))
print(f"{a} or {b}  →", bool(a) or bool(b))
print(f"not {a} →", not bool(a))
print(f"not {b} →", not bool(b))

