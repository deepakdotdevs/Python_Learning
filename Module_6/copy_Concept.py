# Shallow copy & Deep copy concept in python: 
# These concepts are for the mutable data types : - list, set, dictionaries

# In List : 
import copy
l1 =[1,2.5, [10,20,30], 'Python'] # there is 4 elements
# if we want to copy this list, method I using copy function
# another way using copy function of a module called copy

# shallow copy - means both l1 and l2 have different memory addresses
l2 = copy.copy(l1)
print(l2)
# confirmation of memory addresses
print(id(l1))
print(id(l2))
# now let's try to change 1st element of l1,  will l2 be change - NOo
l1[0]=100
print(l1)
print(l2) # bcoz memory addresses are differ of l1 & l2 both 
# now change inner list 10 into 50, it will make change in both l1 and l2
l2[2][0] = 50
print(l1)
print(l2)
# memory address of the items or elements are same, 1st is replacement or reassignment and 2nd is change which is also make in memory address and it will change l2 too

# Deep Copy : where inner element also store in differ memory location : 
l1 =[1,2.5, [10,20,30], 'Python']
l2 = copy.deepcopy(l1)
l1[0] = 5
l1[2][0] = 50
print(f"L1 -> {l1}", id(l1))
print(f"L1 -> {l2}", id(l2))

print("-------------------")

# In Dictionary : 
import copy
d1 = {'id':1111, 'name':'John', 'marks':{'eng':71.5, 'maths':91.5, 'bio':80.0}}
# deep copy
# d2 = copy.deepcopy(d1)
# d1['name'] = 'Dan'
# print(f"d1 -> {d1}", id(d1))
# print(f"d2 -> {d2}", id(d2))
# now let's change the inner element : 
d2 = copy.copy(d1)
d1['name'] = 'Dan'
d1['marks']['maths'] = 92.5
print(f"d1 -> {d1}", id(d1))
print(f"d2 -> {d2}", id(d2))