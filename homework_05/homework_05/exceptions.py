"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    print("Мало топлива. Требуется дозаправка.")

class NotEnoughFuel(Exception):
    print("Не достаточно топлива для преодоления дистанции. Требуется дозаправка.")

class CargoOverload(Exception):
    print("Транспорт перегружен. Требуется частичная разгрузка.")