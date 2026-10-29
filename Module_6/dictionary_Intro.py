# A dictionary is a collection of key-value pairs. It stores data in the form of key: value and is written using curly braces {}.
# each key-value pair is seperated by colons.
# {key1:value1, key2:value2}
# A dictionary is used when we want to store related information in key-value pairs and access a value using its key.

groceries ={'milk':60, 'biscuits':20, 'rice':90, 'bread':30}
print(groceries)
print(type(groceries))
print(len(groceries)) # it calculates how many key-value pairs are there in the dictionary

# In dictionaries indexing also not work !!
# print(groceries[0]) # error output

# To fetch the value, using the key :
print(groceries['milk'])
print(groceries['rice'])

# Dictionaries are mutable

# to modify the value of a key :
groceries['milk']=65
print(groceries)

# print(groceries['eggs']) # give error as not in dictionary

# Added to a dictionary :
groceries['eggs'] = 10
print(groceries)