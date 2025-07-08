"""
Создайте класс `Plane`, наследник `Vehicle`
"""
from homework_05.exceptions import NotEnoughFuel, LowFuelError, CargoOverload
from homework_05.base import BaseVehicle

class plane(BaseVehicle):
    # cargo: float = 0.0
    # max_cargo: float = 0.0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, weight):
        full_weight = self.cargo + weight
        if full_weight >= self.max_cargo:
            raise CargoOverload
        else: 
            self.cargo += weight

    def remove_all_cargo(self):
        rac = self.cargo
        self.cargo = 0.0
        return rac

