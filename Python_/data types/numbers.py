# Python supports three numeric data types: int, float, and complex. They are inferred, so need not be specified.

#  "inferred" means that Python can figure out or understand what kind of number you're using without you having to explicitly tell it.


age = 18 # int
pi = 3.14 # float
total = age + pi # float
print(type(age), type(pi), type(total)) # <class 'int'> <class 'float'> <class 'float'>

# You can also use the "type" function to determine the type of an object.
print(type(18)) # <class 'int'>
print(type(3.14)) # <class 'float'>
print(type(18.0)) # <class 'float'>
print(type(18 + 3.14)) # <class 'float'>
print(type("18")) # <class'str'>

