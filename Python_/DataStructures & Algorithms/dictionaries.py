# Dictionaries are key-value pairs. like special containers in Python where you can store things in pairs, like a matching game. Each pair consists of a "key" and a "value." 

# They are surrounded by {} and are similar to objects in JavaScript. The values can have any data type.

language_creators = {
  "Python" : "Guido van Rossum",
  "C" : "Dennis Ritchie",
  "Java" : "James Gosling",
  "Go": "Robert Griesemer",
  "Perl" : "Larry Wall"
}

# access, modify, delete
print(language_creators["Python"]) # Guido van Rossum

language_creators["C"] = "Dennis Ritchie"
print(language_creators["C"]) # Dennis Ritchie

language_creators["Java"] = "James Gosling"
print(language_creators["Java"]) # James Gosling

language_creators["Go"] = "Robert Griesemer"
print(language_creators["Go"]) # Robert Griesemer

language_creators["Perl"] = "Larry Wall"
print(language_creators["Perl"]) # Larry Wall


language_creators["Go"] = ["Robert Griesemer", "Rob Pike", "Ken Thompson"]
print(language_creators["Go"]) # ['Robert Griesemer', 'Rob Pike', 'Ken Thompson']

print(len(language_creators)) # 5

print(language_creators)

del language_creators["Perl"]
print(len(language_creators)) # 4

# print keys and values
print(language_creators.keys())
print(language_creators.values())

# print all pairs
print(language_creators.items())

# print all keys
print(language_creators.keys())

# print all values
print(language_creators.values())



