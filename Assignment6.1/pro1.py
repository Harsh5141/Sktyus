# Create a base class Animal and subclasses Dog and Cat.
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("The souand animal makes")
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says:Bark")
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says:Miyau")
dog = Dog("Tommy")
cat =Cat("Miku")
dog.speak()
cat.speak()