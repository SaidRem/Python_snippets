# mistake #1
# Do not use mutable in const.

class House:
    cats = []

    def __init__(self):
        pass


my_house = House()
office = House()
my_house.cats.append('Tom')
print(my_house.cats)
# >> ['Tom']
print(office.cats)
# >> ['Tom']   # Tom in office!!! -> Do not use mutable  in const.


# How to make it right.

class House:
    cats: list = None   # use None for const.

    def __init__(self):
        self.cats = []


my_house = House()
office = House()
my_house.cats.append('Tom')
print(my_house.cats)
# >>> ['Tom']
print(office.cats)
# >>> []


# Mistake #2
# Using defaults in functions.
import time as tm
from datetime import datetime


def create_log_entry(user, action, time=datetime.now()):
    """This function will return the same time once the scripts run."""
    return f'{time}: {user} {action}'


print(create_log_entry('Sam', 'smoking'))
tm.sleep(3)
print(create_log_entry('Sam', 'walks away'))


# How to make it right.
# Move the function in body of the function.


def create_log_entry(user, action, time=None):
    time = datetime.now()
    return f'{time}: {user} {action}'


print(create_log_entry('Sam', 'smoking'))
tm.sleep(3)
print(create_log_entry('Sam', 'walks away'))


# Mistake #3
# Using int and bool in dict.
# To use True and False, bools and ints make them str.
Vacab = {
    'True': 'It is true',
    'False': 'It is false',
    '0': 'No',
    '1': 'Yes'
}


# Mistake #4
# Using set for fast calc sometimes inappropriate.

numbers = [i for i in range(10)]

# use in for fast search in lists.

if 5 in numbers:
    print('Five is here')
