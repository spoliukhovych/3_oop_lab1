import unittest
from Taxi import Taxi
from TaxiPark import TaxiPark

class TestCar(unittest.TestCase):
    def test_car_info(self):
        car = Taxi("Toyota", "Camry", 8.5, 120, 50000)
        expected_info = "Toyota Camry - Fuel Consumption: 8.5 L/100km, Speed: 120 km/h, Price: 50000 $"
        self.assertEqual(car.get_info(), expected_info)

class TestTaxiPark(unittest.TestCase):
    def setUp(self):
        self.taxi_park = TaxiPark()
        self.taxi1 = Taxi("Toyota", "Camry", 8.5, 120, 50000)
        self.taxi2 = Taxi("Honda", "Accord", 7.2, 130, 60000)

    def test_add_taxi(self):
        self.taxi_park.add_taxi(self.taxi1)
        self.assertEqual(len(self.taxi_park.taxi_list), 1)

    def test_calculate_total_cost(self):
        self.taxi_park.add_taxi(self.taxi1)
        self.taxi_park.add_taxi(self.taxi2)
        self.assertEqual(self.taxi_park.calculate_total_cost(), 110000)

    def test_sort_by_fuel_consumption(self):
        self.taxi_park.add_taxi(self.taxi1)
        self.taxi_park.add_taxi(self.taxi2)
        sorted_taxi = self.taxi_park.sort_by_fuel_consumption()
        self.assertEqual(sorted_taxi, [self.taxi2, self.taxi1])

    def test_find_by_speed_range(self):
        self.taxi_park.add_taxi(self.taxi1)
        self.taxi_park.add_taxi(self.taxi2)
        found_taxi = self.taxi_park.find_by_speed_range(120, 130)
        self.assertEqual(found_taxi, [self.taxi1, self.taxi2])