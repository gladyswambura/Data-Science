# Control Statements (break, continue, pass):

# break terminates a loop prematurely if a certain condition is met, allowing you to exit the loop early.
# continue skips the current iteration and proceeds to the next one within a loop.
# pass is a placeholder statement that does nothing. It's often used when a statement is syntactically required but doesn't need to execute any code.

# Example using break and continue:

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break  # Terminate the loop when num is 3
    elif num == 2:
        continue  # Skip the iteration when num is 2
    print(num)


