# Implement method overriding in a base and derived class.
class Vehicle:
    def __init__(self,start):
        self.start=start
    def Car(self):
        print(f"Car is start with {self.start}")
class EV(Vehicle):
    def __init__(self,start,key):
        super().__init__(start)
        self.key=key
    def ElectericEv(self):
        print(f"EV start with both {self.key} or without {self.start}.")
car1=EV("carkey","key")
car1.Car()
car1.ElectericEv()
