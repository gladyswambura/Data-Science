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

# example 2
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number.")
finally:
    print("Thanks for playing!")

# Raising exceptions:
# You can also raise your own exceptions in Python using the raise keyword. Here's an example

x = input("Enter a number: ")
if not x.isdigit():
    raise ValueError("That's not a valid number.")

# File I/O
# File I/O is used to read from and write to files on your computer.

# Opening and closing files
# In Python, you can open a file using the open() function. Here's an example

file = open("data/example.txt", "r")

# By default, files are opened in read mode ("r"). You can also open files in write mode ("w") or append mode ("a"). Once you're done with a file, you should close it using the close() method:

file.close()

# Reading and writing to files
# Once you've opened a file, you can read from or write to it using the read() and write() methods, respectively. Here's an example:

file = open("data/example.txt", "w")
file.write("Hello, world!")
file.close()

file = open("data/example.txt", "r")
print(file.read())
file.close()
