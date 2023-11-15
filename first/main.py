from TaxiPark import *

def display_menu():
    print("\n1. Додати таксі")
    print("2. Розрахувати вартість автопарку")
    print("3. Відсортувати автомобілі за витратами палива")
    print("4. Знайти автомобіль за діапазоном швидкості")
    print("5. Вийти")

def display_add_taxi(taxi_park):
    brand = input("Введіть марку автомобіля: ")
    model = input("Введіть модель автомобіля: ")
    fuel_consumption = float(input("Введіть витрати палива (L/100km): "))
    speed = int(input("Введіть швидкість автомобіля (km/h): "))
    price = float(input("Введіть вартість автомобіля: "))

    taxi = Taxi(brand, model, fuel_consumption, speed, price)
    taxi_park.add_taxi(taxi)
    print("Автомобіль додано до таксопарку.")

def main():
    taxi_park = TaxiPark()

    while True:
        display_menu()
        choice = input("Виберіть опцію (1-5): ")

        if choice == '1':
            display_add_taxi(taxi_park)
        elif choice == '2':
            total_cost = taxi_park.calculate_total_cost()
            print(f"Загальна вартість автопарку: {total_cost} $")
        elif choice == '3':
            sorted_taxi = taxi_park.sort_by_fuel_consumption()
            for taxi in sorted_taxi:
                print(taxi.get_info())
        elif choice == '4':
            min_speed = int(input("Введіть мінімальну швидкість: "))
            max_speed = int(input("Введіть максимальну швидкість: "))
            found_taxi = taxi_park.find_by_speed_range(min_speed, max_speed)
            for taxi in found_taxi:
                print(taxi.get_info())
        elif choice == '5':
            print("Дякую за використання програми. Завершення роботи.")
            break
        else:
            print("Неправильний вибір. Будь ласка, виберіть знову.")

if __name__ == "__main__":
    main()