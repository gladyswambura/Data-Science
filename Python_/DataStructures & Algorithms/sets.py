# A set is a collection of unique values that are unordered and unindexed. Sets are defined using curly braces { }.
# Here's an example of creating a set:

fruits = {"apple", "banana", "cherry"}

# Set methods

# add(): adds an item to the set.
# remove(): removes the specified item from the set.
# discard(): removes the specified item from the set, but does not raise an error if the item is not in the set.
# pop(): removes an arbitrary item from the set, and returns it.
# clear(): removes all items from the set.
# union(): returns a set containing the union of two or more sets.
# intersection(): returns a set containing the intersection of two or more sets.
# difference(): returns a set containing the difference between two sets.
# symmetric_difference(): returns a set containing the symmetric difference between two sets.


# Create two sets
fruits1 = {"apple", "banana", "cherry"}
fruits2 = {"banana", "orange", "pineapple"}

# Add an item to a set
fruits1.add("mango")
print(fruits1)    # prints {"apple", "banana", "cherry", "mango"}

# Remove an item from a set
fruits1.remove("banana")
print(fruits1)    # prints {"apple", "cherry", "mango"}

# Remove an item from a set using discard(), which doesn't raise an error if the item isn't in the set
fruits1.discard("banana")
print(fruits1)    # prints {"apple", "cherry", "mango"}

# Remove an arbitrary item from a set using pop()
item = fruits1.pop()
print(item)       # prints "apple"
print(fruits1)    # prints {"cherry", "mango"}

# Clear all items from a set
fruits1.clear()
print(fruits1)    # prints set()

# Get the union of two sets
all_fruits = fruits1.union(fruits2)
print(all_fruits)    # prints {"banana", "cherry", "mango", "orange", "pineapple"}

# Get the intersection of two sets
common_fruits = fruits1.intersection(fruits2)
print(common_fruits)    # prints set()

# Get the difference between two sets
diff_fruits = fruits1.difference(fruits2)
print(diff_fruits)    # prints set()

# Get the symmetric difference between two sets
sym_diff_fruits = fruits1.symmetric_difference(fruits2)
print(sym_diff_fruits)    # prints {"banana", "cherry", "mango", "orange", "pineapple"}