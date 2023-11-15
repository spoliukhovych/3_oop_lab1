class Car:
    def __init__(self, brand, model, fuel_consumption, speed):
        self.brand = brand
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.speed = speed

    def get_info(self):
        return f"{self.brand} {self.model} - Fuel Consumption: {self.fuel_consumption} L/100km, Speed: {self.speed} km/h"