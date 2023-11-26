# Modules are files containing Python code. They can define functions, classes, and variables, and can be imported into other Python scripts.

# Common python modules include: math, random, datetime

# To use a module in your code, you need to import it using the import keyword

import math
print(math.sqrt(16))
print(math.pi)

# You can also import specific functions or classes from a module.

from math import sqrt
print(sqrt(16))

# The random module provides functions to generate random numbers

import random
print(random.randint(1, 6))  # Simulate a dice roll

# The datetime module provides functions and classes to work with dates and times.

import datetime
today = datetime.date.today()
print(today)

now = datetime.datetime.now()
print(now)