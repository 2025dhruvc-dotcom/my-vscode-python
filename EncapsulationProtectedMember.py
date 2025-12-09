class Car:
    def __init__(self,brand,price):
        self._brand = brand         
        self._price = price        
car1 = Car("BMW",50000)
print(car1._brand)
print(car1._price)
