class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a = Animal()
b = Dog()
c = Cat()

a.sound()  # Output: Animal makes a sound
b.sound()  # Output: Dog barks
c.sound()  # Output: Cat meows