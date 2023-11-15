from Taxi import Taxi

class TaxiPark:
    def __init__(self):
        self.taxi_list = []

    def add_taxi(self, taxi):
        self.taxi_list.append(taxi)

    def calculate_total_cost(self):
        return sum(taxi.price for taxi in self.taxi_list)

    def sort_by_fuel_consumption(self):
        return sorted(self.taxi_list, key=lambda x: x.fuel_consumption)

    def find_by_speed_range(self, min_speed, max_speed):
        return [taxi for taxi in self.taxi_list if min_speed <= taxi.speed <= max_speed]