# Working with keys & values : 

# when run there is an error : TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
# d1={[1,3,5]:9,[1,2,1]:4}
# print(d1)
d1={'Nine':9,'Four':4}
print(d1)

# keys can't be list
# not allowed - list, set
# allowed keys - str, float, booleat, tuple, int

# is intergers can be the keys : Yes as shown in below example
d1 = {1:True, 0:False}
print(d1)

# What about float as keys : Yes as shown in below example
d1 = {1.0:True, 0.0:False}
print(d1)

# Booleans as keys : Yes as shown in below example
d1 = {True:1, False:0}
print(d1)

# Tuple as keys : Yes as shown in below example
d1 = {(1,2,3):4, (1,2):3}
print(d1)

# Set as keys : Error as sets is also not allowed
# d1 = {{1,2,3}:4, {1,2}:3}
# print(d1)

# Can a dictionary be the dictionary of itself : Error means not allowed
# d1={{'a':1, 'b':2}:6}
# print(d1)

print("-----------------------")

# Why a dict keys not involve list, set and dict itself ?
# str, float, booleat, tuple, int => they are all immutable data types (we can reassign them, but can't change or update)

# Means keys of a dict can only be mutable datatypes!!

# Value can be any datatype - list, tuple, set, dict any : example as shown below
student1={'id':1001,'name':'John','marks':[89.5,71.5,81.5]}
print(student1)
# Now, how to fetch marks from this list :
print(student1['marks']) # all marks list
print(student1['marks'][1]) # from list

# same example as dict : 
student1={'id':1001,'name':'John','marks':{'eng':89.5,'maths':71.5,'bio':81.5}}
print(student1)
# Now, how to fetch marks from this list :
print(student1['marks']) # all marks dict
print(student1['marks']['eng']) # from dict

print("--------------------------------")

# functions to fetch keys and values : 
# Can we fetch key using value : Noo

# Can we fetch all the keys and only the keys : Yes
# function called keys()
print(student1.keys())

# Can we fetch all the values and only the values : Yes
# function called values()
print(student1.values())

# items() : Till now we fetch keys and values differ, but using it together : 
print(student1.items())