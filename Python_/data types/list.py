# In Python, a list is like a collection of things. You can think of it as a box where you can put different types of stuff inside. These items are organized in a specific order, starting from zero. So, the first item is at position 0, the second at position 1, and so on. To tell Python that you're making a list, you put square brackets [] around your items. This helps Python understand that you're working with a list of things.

# Lists are mutable, meaning that you can change the items in a list. You can also add new items to a list.

# can store any data type
multiple_types = [True, 3.7, "Python", 15]

# access and modify
favourite_foods = ["pasta", "pizza", "french fries"]
print(favourite_foods[1]) # pizza

favourite_foods[0] = "rösti"
print(favourite_foods[0]) # rösti

# favourite_foods = ["rosti", "pasta", "pizza", "french fries"]

# subsets
print(favourite_foods[1:3]) # ['pizza', 'french fries']
print(favourite_foods[2:]) # ['french fries']
print(favourite_foods[0:2]) # ['rösti', 'pizza']

# append
favourite_foods.append("paella")

# insert at index
favourite_foods.insert(1, "soup")
print(favourite_foods)

# remove
favourite_foods.remove("soup")

# get length
print(len(favourite_foods)) # 4

# get subset (the original list is not modified)
print(favourite_foods[1:3]) # ['pizza', 'french fries']

# lists inside lists
favourite_drinks = ["water", "wine", "juice"]
favourites = [favourite_foods, favourite_drinks]
print(favourites)
print(favourites[1][1]) # wine



