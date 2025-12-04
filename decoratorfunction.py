def decorator(func):
    def wrapper():
        func()
        print("Before function call")
        func()
        print("After function call")
        func()
    return wrapper

@decorator
def greet():
    print("Hello, World!")
greet()