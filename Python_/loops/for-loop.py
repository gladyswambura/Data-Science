# for loops allow you to iterate over a sequence (such as a list, tuple, string, or range) or other iterable objects. They execute a block of code for each item in the iterable.

# foor loop
for x in range(0, 3):
  print(x)

# loop through list
for x in ["Python", "Go", "Java"]:
  print(x)

# loop through dictionary
language_creators = {
  "Python" : "Guido van Rossum",
  "C" : "Dennis Ritchie",
  "Java" : "James Gosling",
}
for key, value in language_creators.items():
  print("Language: {}; Creator: {}".format(key, value))

#example 1
for i in range(10):
    print(i)
    print(i**2)

# example 2
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)


# example 3
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i])

# example 4
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(i)
    print(numbers[i])

# example 5
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(i)
    print(numbers[i])
    print(i**2)

