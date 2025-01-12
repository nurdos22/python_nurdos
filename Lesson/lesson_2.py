

class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__was_born()

    def __was_born(self):
        print(f'Animal {self.__name} was born')

    def set_age(self, age):
        if type(age) != int or age <= 0:
            raise ValueError("age must be greater than zero")
        else:
            self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def info(self):
        return (f'{self.__name} is {self.__age} years old. '
                f'Birth year: {2025 - self.__age}.')

    def make_voice(self):
        pass

# some_animal = Animal('Anim', 2)
# some_animal.set_age(3)
# some_animal.set_name('Bobik')
# print(some_animal.get_name())
# print(some_animal.info())

class Fish(Animal):
    def __init__(self, name, age):
        # super().__init__(name, age)
        super(Fish, self).__init__(name, age)


class Cat(Animal):
    def __init__(self, name, age):
        # super().__init__(name, age)
        super(Cat, self).__init__(name, age)

    def make_voice(self):
        print('Meow')


class Dog(Animal):
    def __init__(self, name, age, commands):
        super(Dog, self).__init__(name, age)
        self.__commands = commands

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    def info(self):
        return super().info() + f' commands: {self.__commands}'

    def make_voice(self):
        print('Wouf')


class FightingDog(Dog):
    def __init__(self, name, age, commands, wins):
        super(FightingDog, self).__init__(name, age, commands)
        self.__wins = wins

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        self.__wins = value

    def fight(self):
        print(f'Dog {self.get_name()} is fighting.')

    def info(self):
        return super().info() + f', wins: {self.__wins}'

    def make_voice(self):
        print('Rrrr wouf')


cat = Cat('Kitty', 2)
# print(cat.get_name())
cat.set_age(3)

dog = Dog('Sharik', 8, 'Sit')
dog.commands = 'Sit, run'
# print(dog.commands)

fighting_dog = FightingDog('Borzik', 1, 'fight', 20)

fish = Fish('Nemo', 3)

animals_list = [cat, fish, dog, fighting_dog]
for animal in animals_list:
    print(animal.info())
    animal.make_voice()
