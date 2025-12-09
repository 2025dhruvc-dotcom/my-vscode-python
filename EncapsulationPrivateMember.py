class Cart:
    def __init__(self,brand,price):
        self.__brand = brand
        self.__price = price
car1 = Cart("BMW",50000)
print(car1.__brand)  # This will raise an AttributeError
print(car1.__price)  # This will raise an AttributeError