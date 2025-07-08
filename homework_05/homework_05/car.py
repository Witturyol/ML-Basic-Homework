"""
Создайте класс `Car`, наследник `Vehicle`
"""
from homework_05.base import BaseVehicle
from homework_05.engine import Engine

class Car(BaseVehicle):
    
    def __init__(self, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine: Engine = None

    def set_engine(self, engine):
        self.engine = engine