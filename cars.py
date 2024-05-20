import random


class Car:
    def __init__(self, economy, color, model, mileage=0, fuel=100):
        self.mileage = mileage
        self.fuel = fuel
        self.economy = economy
        self.color = color
        self.model = model

    def drive(self, distance):
        required_fuel = distance / self.economy
        if required_fuel > self.fuel:
            raise ValueError("Недостатньо палива для поїздки на таку відстань.")
        self.mileage += distance
        self.fuel -= required_fuel

    def distance_left(self):
        return self.fuel * self.economy

    def fuel_up(self):
        self.fuel += 20


colors = ["Red", "Blue", "Green", "Black", "White", "Yellow", "Purple", "Gray", "Orange", "Brown"]
models = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
economy_values = [random.randint(10, 20) for _ in range(10)]

cars = []
for i in range(10):
    color = random.choice(colors)
    model = random.choice(models)
    economy = random.choice(economy_values)
    car = Car(economy=economy, color=color, model=model)
    cars.append(car)

for car in cars:
    print(car)

my_car = Car(economy=15, color="Red", model="Toyota Corolla")
print(my_car)

try:
    my_car.drive(150)
    print(my_car)
except ValueError as e:
    print(e)

print(f"Відстань, що залишилася: {my_car.distance_left()} км")

try:
    my_car.drive(1000)
    print(my_car)
except ValueError as e:
    print(e)

my_car.fuel_up()

for car in cars:
    try:
        car.drive(200)
        car.fuel_up()
        car.drive(100)
    except ValueError as e:
        print(f"Помилка: {e}")

most_fuel_car = max(cars, key=lambda car: car.fuel)

max_fuel = max(car.fuel for car in cars)

cars_with_max_fuel = [car for car in cars if car.fuel == max_fuel]
