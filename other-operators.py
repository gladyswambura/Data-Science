# Comparison: ==, !=, <, >, <=, >=
# Logical: and, or, not
# Conditionals: if, else, elif


# logical operators:
laundry_day = "Monday"
today = "Tuesday"
on_vacation = False
if today is laundry_day and today is not "Sunday" and on_vacation is False:
  print("It's laundry day!")
else:
  print("The laundry can wait!")


# comparison operators:
age = 21
if age >= 21:
  print("You can drive a trailer")
elif age >= 16:
  print("You can drive a car")
else:
  print("You can ride a bike")