# Experiment 8: Polymorphism

class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f'{self.name} is moving.')

    def describe(self):
        print(f'Vehicle: {self.name}')


class Car(Vehicle):
    def __init__(self, name, brand):
        super().__init__(name)
        self.brand = brand

    def move(self):   # Override
        print(f'{self.brand} {self.name} - Driving on the road')


class Bicycle(Vehicle):
    def __init__(self, name, gear_count):
        super().__init__(name)
        self.gear_count = gear_count

    def move(self):   # Override
        print(f'{self.name} ({self.gear_count}-gear) - Pedaling on the road')


class Boat(Vehicle):
    def move(self):   # Override
        print(f'{self.name} - Sailing on the water')


# Demonstrate Polymorphism
vehicles = [
    Car('Sedan', 'Toyota'),
    Car('SUV', 'Honda'),
    Bicycle('Mountain Bike', 21),
    Bicycle('Road Bike', 18),
    Boat('Speedboat'),
]

print('--- Polymorphic move() calls ---')
for v in vehicles:
    v.move()

print('\n--- Direct calls ---')
car = Car('Hatchback', 'Maruti')
bike = Bicycle('City Bike', 7)
car.move()
bike.move()
