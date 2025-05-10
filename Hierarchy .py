
class Creature:
    def speak(self):
        print("Creature makes a sound")

class Animal(Creature):
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

class Bulldog(Dog, Cat):
    pass

b = Bulldog()
b.speak()

print("MRO:", Bulldog.__mro__)
