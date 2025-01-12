class Transport:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    # method
    def change_color(self, new_color):
        self.color = new_color


class Plane(Transport):
    def __init__(self, model, year, color):
        super().__init__(model, year, color)


class Car(Transport):
    # class attribute
    counter = 0

    # constructor                   # parameters
    def __init__(self, model, year, color, penalties=0):
        # attributes / fields
        super().__init__(model, year, color)
        self.penalties = penalties
        Car.counter += 1

    # method
    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')


class Truck(Car):
    counter = 0
    def __init__(self, model, year, color, penalties=0, load_capacity=0):
        super().__init__(model, year, color, penalties)
        self.load_capacity = load_capacity
        Truck.counter += 1

    def load_cargo(self, weight, product):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity} kg!')
        else:
            print(f'You successfully loaded {product} - {weight} kg!')


print(f'Factory CAR produced: {Car.counter} cars.')
number = 3
bmw_car = Car('BMW E30', 1992, 'black')

print(number)
print(bmw_car)
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} COLOR: {bmw_car.color} '
      f'PENALTIES: {bmw_car.penalties}')
# bmw_car.color = 'red'
bmw_car.change_color('red')
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} NEW COLOR: {bmw_car.color} '
      f'PENALTIES: {bmw_car.penalties}')

mers_car = Car('Mers W211', 2007, 'silver', 700)
print(f'MODEL: {mers_car.model} YEAR: {mers_car.year} COLOR: {mers_car.color} '
      f'PENALTIES: {mers_car.penalties}')

honda_car = Car(year=2015, model='Honda CR-V', color='white', penalties=1400)
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} COLOR: {honda_car.color} '
      f'PENALTIES: {honda_car.penalties}')

bmw_car.drive('Osh')
bmw_car.drive('Batken')

mers_car.drive('Kant')

print(f'Factory CAR produced: {Car.counter} cars.')

boeing_plane = Plane('Boeing 747', 2023, 'blue')
print(f'MODEL: {boeing_plane.model} YEAR: {boeing_plane.year} COLOR: {boeing_plane.color}')

daf_truck = Truck('DAF 500', 2020,
                  'red', 0, 50000)
print(f'MODEL: {daf_truck.model} YEAR: {daf_truck.year} COLOR: {daf_truck.color} '
      f'PENALTIES: {daf_truck.penalties} LOAD CAPACITY: {daf_truck.load_capacity}')
daf_truck.load_cargo(60000, 'apples')
daf_truck.load_cargo(45000, 'potatoes')
daf_truck.drive('Tokmok')

print(f'Factory TRUCK produced {Truck.counter} trucks.')

print('End of program')
