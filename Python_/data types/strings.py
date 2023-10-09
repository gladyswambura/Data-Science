#Example 1:
language = "Python"

#Example 2:
multiline_str = '''
one
per
line'''  

#Example 3, escape characters:
escape_str = "She said: \"Python is great!\""
print(escape_str) # She said: "Python is great!"  

# Example 4, concatenate strings:
one = "Lux"
two = "Academy"
print(one + " " + two) # Lux Academy 

# Example 5: interpolation.
# method 1
first_name = "Lux"
last_name = "Academy"
greet = f"Welcome at {first_name} {last_name}!" 
print(greet)  # Welcome at Lux Tech Academy!

# method 2
first_name = "Lux"
last_name = "Academy"
greet = 'Welcome at {} {}!'.format(first_name, last_name)
print(greet)  # Welcome at Lux Tech Academy!

# method 3
first_name = "Lux"
last_name = "Academy"
greet = 'Welcome at{first} {last} !'.format( first=first_name, last=last_name) 
print(greet)  # Welcome at Lux Tech Academy!

#Example 6, extract substrings
name = "Monty Python"
print(name[6:9]) # Pyt
print(name[6:]) # Python
print(name[:5]) # Monty