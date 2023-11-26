# Functions are blocks of reusable code that encapsulate a specific set of tasks or operations. Functions make code more organized, modular, and easier to understand, maintain, and reuse.

# To define a function in Python, you use the def keyword, followed by the function name and a pair of parentheses. Any input parameters (arguments) that the function requires are placed inside these parentheses. The colon: indicates the start of the function block. 

# Functions can return values using the return keyword.

# def function_name(parameter1, parameter2, ...):# Function code here

# Function to add two numbers and return the result
def add_numbers(a, b):
    result = a + b
    return result

# Calling the add_numbers function and printing the result
sum_result = add_numbers(5, 3)
print(sum_result)  # Output: 8

# Function to multiply two numbers and return the result
def multiply(a, b):
    result = a * b
    return result

# Global variable declaration
global_var = 10  # This is a global variable

# Function that adds a local variable to a global variable
def my_function():
    local_var = 5  # This is a local variable
    return global_var + local_var

# Calling my_function and printing the result
result = my_function()
print(result)  # Output: 15

# Function with a docstring explaining its purpose
def my_function(parameter):
    """
    This is a docstring.
    It explains what the function does.
    """
    # Function code here

# functions
def allowed_to_drive(age):
  if age >= 21:
    return True
  else:
    return False

print(allowed_to_drive(42)) # True
print(allowed_to_drive(12)) # False


# Default values for arguments may also be defined.
   
def is_laundry_day(today, laundry_day = "Monday", on_vacation = False):
  if today is laundry_day and today is not "Sunday" and on_vacation is False:
    return True
  else:
    return False

print(is_laundry_day("Tuesday")) # False
print(is_laundry_day("Tuesday", "Tuesday")) # True
print(is_laundry_day("Friday", "Friday", True)) # False