from email.policy import default
from random import randint, choice as select_random_element
import utilities.calculator as calc
from utilities.templates import Person
from termcolor import cprint
from decouple import config

print(randint(1, 10))
print(select_random_element([1, 4, 5, 6, 7]))

print(calc.multiplication(2, 5))

friend = Person('Daniel', 16)
print(friend)
cprint("Hello, World!", "green", "on_red")
print(config('DATABASE_URL'))
commented = config('COMMENTED', default=0, cast=int)
print(commented*2)


# End of program