from homework_05.exceptions import NotEnoughFuel, LowFuelError, CargoOverload

class BaseVehicle():
    
    started: bool = False
    weight: float = 0.0
    fuel: float = 0.0
    fuel_consumption: float = 0.0
    
    def __init__(self, weight: float, fuel: float, fuel_consumption: float):
        self.started = False
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
    
    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, dist: float):
        road_consumption = self.fuel_consumption * dist
        if road_consumption > self.fuel:
            self.fuel -= road_consumption
        else: 
            raise NotEnoughFuel