# Tuples are just like lists, but immutable (cannot be modified). They are surrounded by parenthesis--().

new_tuple = ("a", "b", "c", "d")
print(len(new_tuple)) # 4
print(new_tuple[1]) # b
print(new_tuple[1:4]) # ('b', 'c', 'd')

# new_tuple[1] = "x" # TypeError: 'tuple' object does not support item assignment

new_tuple = ("a", "b", "c", "d")
print(new_tuple) # ('a', 'b', 'c', 'd')
print(new_tuple[1:]) # ('b', 'c', 'd')
print(new_tuple[:3]) # ('a', 'b', 'c')
print(new_tuple[2:]) # ('c', 'd')
