# Lists are mutable and Tuples are not.
# Concept of mutability and Immutability

# Mutability is the ability of a value for data to be modified or changed and immutability is the reverse of that.
# lists are mutable
# tuple and strings are immutable

s1 ='python is fun'
s1.replace('python', 'java')
print(s1) # no change in output as string is immutable
s2 = s1.replace('python', 'java') # but we can store changes into a new string or variable
print(s2)

# Similarly, in case of tuples : can't be modified
# t1 =('mango', 'orange', 'apple')
# t1.append('banana')
# print(t1)

# memory address :
l1 =['mango', 'orange', 'apple']
print(id(l1))
l1.append('banana')
print(l1)
print(id(l1))

l1 = ['mango', 'orange', 'aple']
print(l1)
print(id(l1))
l1[-1] = 'apple'
print(l1)
print(id(l1))

# but in tuple : provides error as tuples no changes are allowed
# l1 = ('mango', 'orange', 'aple')
# l1[-1] = 'apple'
# print(l1)

# In string :
s4="Python"
print(s4)
s4[0]='p'
print(s4)
