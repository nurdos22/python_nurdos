from enum import Enum


class Color(Enum):
    RED = '\33[31m'
    BLUE = '\33[34m'
    GREEN = '\33[32m'


class Car:
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        if type(color) == Color:
            self.__color = color

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def drive(self):
        print(f'Car {self.__model} is driving')

    def __str__(self):
        return (f'Model: {self.__model}, Year: {self.__year}, '
                f'Color: {self.__color.value}{self.__color.name}' + '\33[0m')

    def __lt__(self, other):
        return self.__year < other.__year

    def __gt__(self, other):
        return self.__year > other.__year

    def __eq__(self, other):
        return self.__year == other.__year

    def __ne__(self, other):
        return self.__year != other.__year

    def __le__(self, other):
        return self.__year <= other.__year

    def __ge__(self, other):
        return self.__year >= other.__year


# some_car = Car('Subaru Outback', '2022', 'red')
# print(some_car)

class FuelCar(Car):
    __total_fuel = 0

    @staticmethod
    def get_fuel_type():
        return 'AI 95'

    @classmethod
    def buy_fuel(cls, amount):
        cls.__total_fuel += amount
        cls.show_fuel_remain()

    @classmethod
    def show_fuel_remain(cls):
        print(f'Factory FUEL_CAR has {cls.__total_fuel} litter of fuel.')

    def __init__(self, model, year, color, fuel_bank):
        # super().__init__(model, year, color)
        # super(FuelCar, self).__init__(model, year, color)
        Car.__init__(self, model, year, color)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel -= fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def drive(self):
        print(f'Car {self.model} is driving by fuel')

    def __str__(self):
        return super().__str__() + f', Fuel Bank: {self.__fuel_bank}'

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank


class ElectricCar(Car):
    def __init__(self, model, year, color, battery):
        Car.__init__(self, model, year, color)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f'Car {self.model} is driving by electricity')

    def __str__(self):
        return super().__str__() + f', Battery: {self.__battery}'


class HybridCar(ElectricCar, FuelCar):
    def __init__(self, model, year, color, fuel_bank, battery):
        FuelCar.__init__(self, model, year, color, fuel_bank)
        ElectricCar.__init__(self, model, year, color, battery)

    def drive(self):
        print(f'Car {self.model} is driving by fuel or electricity')


FuelCar.buy_fuel(1000)

honda_car = FuelCar('Honda CR-V', 2009, Color.BLUE, 80)
print(honda_car)

tesla_car = ElectricCar('Tesla Model X', 2022, Color.RED, 1500)
print(tesla_car)

toyota_car = HybridCar('Toyota Prius', 2010,
                       Color.GREEN, 70, 1000)
print(toyota_car)
toyota_car.drive()
print(HybridCar.mro())

number_1, number_2 = 2, 5
print(f'Number one is bigger than number two: {number_1 > number_2}')
print(f'Number one is smaller than number two: {number_1 < number_2}')
print(f'Price of Tesla car is smaller than price of Toyota car: {tesla_car < toyota_car}')
print(f'Price of Honda car is the same with price of Toyota car: '
      f'{tesla_car == toyota_car}')
print(f'Sum of two numbers: {number_1 + number_2}')
print(f'Sum of fuel banks: {honda_car + toyota_car}')

# FuelCar.total_fuel -= 100
FuelCar.show_fuel_remain()
print(f'Factory FUEL_CAR uses for test drives {FuelCar.get_fuel_type()} of fuel.')

if tesla_car.model == 'Tesla Model-X':
    print('This car is cool')

if tesla_car.color == Color.RED:
    print('This car is beautiful')