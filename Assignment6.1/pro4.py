
# Demonstrate multiple inheritance with two parent classes.
class Animal:
    def __init__(self,animal):
        self.animal=animal
    def animal_name(self):
        print(f"{self.animal} is a Running")
class Bird(Animal):
    def __init__(self, animal, bird):
        super().__init__(animal)
        self.bird = bird
    def bird_name(self):
        print(f"{self.bird} is flying")
class Zoo(Bird):
    def __init__(self,animal,bird):
        super().__init__(animal,bird)
    def zoo_name(self):
        print(f"{self.animal},{self.bird} in a Zoo.")
Z=Zoo("tiger","peacock")
Z.animal_name()
Z.bird_name()
Z.zoo_name()