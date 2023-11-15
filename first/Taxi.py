from Car import Car

class Taxi(Car):
    def __init__(self, brand, model, fuel_consumption, speed, price):
        super().__init__(brand, model, fuel_consumption, speed)
        self.price = price

    def get_info(self):
        return super().get_info() + f", Price: {self.price} $"