# A set is a collection of unique elements. Sets are unordered, do not allow duplicate values, and are written using curly braces {}.
# It is non-sequential collection of items. Commas separated elements.

set1 = {10, 'Python', 2.5}
print(set1)
print(type(set1))

# cannot have indexing with sets
# print(set1[0]) # gives error

# length of a set : 
print(len(set1))

# No duplicate elements allowed : 
l1 = [10, 2.5, 10,30,10] # eg of list
print(l1, type(l1))
s1 = {10, 2.5, 10,30,10} # eg of set
print(s1, type(s1))

