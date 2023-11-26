# In Python, a list is like a collection of things. These items are organized in a specific order, starting from zero. So, the first item is at position 0, the second at position 1, and so on. To tell Python that you're making a list, you put square brackets [] around your items. This helps Python understand that you're working with a list of things.

# Lists are mutable, meaning that you can change or modify the items in a list. You can also add new items to a list.

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

# Here are some common methods that you can use with lists:

# append(): adds an item to the end of the list.
# insert(): adds an item at a specified position in the list.
# remove(): removes the first occurrence of an item from the list.
# pop(): removes the item at a specified position in the list, and returns it.
# clear(): removes all items from the list.
# index(): returns the index of the first occurrence of an item in the list.
# count(): returns the number of times an item appears in the list.
# sort(): sorts the items in the list.
# reverse(): reverses the order of the items in the list.

# favourite_foods = ["rosti", "pasta", "pizza", "french fries"]
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


# List comprehension
# List comprehension is a way of creating a new list by iterating over an existing list and applying an operation to each item. Here's an example:

fruits = ["apple", "banana", "cherry"]

new_fruits = [fruit.upper() for fruit in fruits]
print(new_fruits)    # prints ["APPLE", "BANANA", "CHERRY"]
