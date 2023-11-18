# for loops allow you to iterate over a sequence (such as a list, tuple, string, or range) or other iterable objects. They execute a block of code for each item in the iterable.

# for loop
for x in range(4, 10, 2):
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
    print(i, i**2)
 

# example 2
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)


# example 3
numbers = ['gladys', 'Sam',]
for i in range(len(numbers)):
    print(numbers[i])

# example 4
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(i, numbers[i])
   
num=[]
for i in range(5):
   num.append(i)
   print(num)


# example 5
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(i)    #prints the index of the numbers
    print(numbers[i])  # prints the list as they are
    print(i**2)        # prins the power of the lists

