# Tuple : Similar to list, they are comma-seperated elements enclosed within brackets. 
# round brackets are used "()" or paranthesis not square "[]" as list
# sequence of items as a collection

# Major Difference b/w list and tuples : 
# We use append function in list remove, extend, insert, pop functions for adding and removing of elements
# But no modifications are allowed or we make in tuples

# Where Use of Tuples : list of week names, Month names means where modify's is not needed or no scope
# Where Use of Lists : Where modification is may be used or somewhere it's scope is there. We use list on that place.

# t1=('python', 10,1.5, [1,2,3], (10,20), True)
# print(t1)
# print(len(t1))

# # accessing items of a tuple - using indexing
# print(t1[0])
# print(t1[-1])

# # slicing :
# print(t1[1:4:1])
# print(t1[1:4:2])

# we create tuple without () too :
# t2 = 10,20,30
# print(type(t2))

# list into tuple using typecasting:
# l1 = [1,2,3]
# print(l1, type(l1))
# t1=tuple(l1)
# print(t1, type(t1))

# tuple into list using typecasting:
t1=(10,20,30)
print(t1, type(t1))
l1 = list(t1)
print(l1, type(l1))
