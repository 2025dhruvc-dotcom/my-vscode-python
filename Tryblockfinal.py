try:
    x = 10
    print(x)
except NameError:
    print("Variable x is not defined")
except Exception:
    print("Something went wrong")
else:
    print("No errors occurred")
finally:
    print("Execution completed")
    

