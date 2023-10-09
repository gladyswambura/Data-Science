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


