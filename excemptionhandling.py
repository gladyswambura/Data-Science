# Exception Handling (try, except, else, finally):

# Exception handling allows you to handle errors and exceptions gracefully in your code.

# try blocks contain the code that may raise an exception.
# except blocks define how to handle specific exceptions that may occur within the try block.
# else blocks are executed if no exceptions were raised.
# finally blocks contain code that is always executed, regardless of whether an exception occurred.

try:
    result = 10 / 0  # Division by zero will raise an exception
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print("Result:", result)
finally:
    print("Execution completed.")
