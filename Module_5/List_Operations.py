# List Operations - slicing, concat, repeat, append, insert

# slicing of lists
l1 = [3,4,2,5,6,7,8,9]
print(len(l1))
print(l1[1:6:1])
print(l1[1:6:2])

# Concatenation of lists : 
l1 = [1,7,2]
l2 = [0,5]
print(l1+l2)
print(l2+l1)

# repetition of lists : 
l1 = [1,7,2]
l2 = [0,5]
print(l2*3)

# Some of functions or methods that will be use with lists : 

# append() : adds an item to the end of the list
fruits = ['Mango', 'Apple', 'Orange']
print(fruits)
fruits.append('Banana')
print(fruits)
print(fruits.append('Pineapple')) # Output is None (as append make changes in original list not create new list)
fruits.append('Pineapple')
print(fruits)

# If we want to add something at front or specified where it needs to be added : 
# function called insert() - adds an element before the specified index
# Syntax - list.insert(index, item)
fruits = ['Mango', 'Apple', 'Orange']
fruits.insert(0, 'Banana')
fruits.insert(2, ' Pineapple')
print(fruits)
