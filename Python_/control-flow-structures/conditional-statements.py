# Control flow structures in Python are constructs that allow you to control the order in which statements are executed in your code based on certain conditions. These structures help you make decisions, loop through code multiple times, and handle exceptional cases. Python supports the following control flow structures:

# Conditional Statements (if, elif, else):
# Loops (for and while):
# Control Statements (break, continue, pass):


# if statements allow you to execute a block of code if a specified condition is True.
# elif (short for "else if") statements are used to check additional conditions if the initial if condition is False.
# else statements provide a fallback block of code to execute if none of the preceding conditions are met.

age = 20
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


