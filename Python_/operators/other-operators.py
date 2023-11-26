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
age = 22
if age >= 21:    # 21++
  print("You can drive a trailer")
elif age >= 16:  # 16-20
  print("You can drive a car")
else:            # less than 16
  print("You can ride a bike")