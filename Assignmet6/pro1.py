# Create a Car class with attributes like brand, model, and speed, and methods to accelerate/brake.
class Car:
    def __init__(self,brand,model,speed=33):
        self.brand=brand
        self.model=model
        self.speed=speed
    def accelerate(self,increase):
        self.speed += increase
        print(f"Accelerate.Current.speed:{self.speed}km/h")
    def brake(self,decrease):
        self.speed -=decrease
        if self.speed < 0:
            self.speed =0
        print(f"Brake.current.sppeed:{self.speed}km/h")
car1=Car("toyato","fortuner")
car1.accelerate(20)
car1.brake(5)