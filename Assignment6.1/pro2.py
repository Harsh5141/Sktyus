# Create a class hierarchy for Vehicle → Car → ElectricCar.
class Vehical:
    def  __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def start(self):
        print(f"{self.brand} Vehecal is starting.")
    def show_speed(self):
        print(f"Speed:{self.speed}km/h")
class Car(Vehical):
    def __init__(self,brand,speed,doors):
        super().__init__(brand,speed)
        self.doors=doors
    def car_info(self):
        print(f"Brand:{self.brand},Doors:{self.doors}")
class ElectricCar(Car):
    def __init__(self,brand,speed,doors,battery_capacity):
        super().__init__(brand,speed,doors)
        self.battery_capacity=battery_capacity
    def charge(self):
        print(f"Battery_capacity:{self.battery_capacity}kwh")
    def fuel_type(self):
        print("Fuel_type:Electric")
Ec=ElectricCar("EV",180,4,120)
Ec.start()
Ec.show_speed()
Ec.car_info()
Ec.charge()
Ec.fuel_type()
    

        