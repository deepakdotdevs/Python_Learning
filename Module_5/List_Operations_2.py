# List Operations - extend(), remove(), pop() : 

# extend() : also add element at the end of the list. But it can add multiple items at a time, whereas append() adds only add one element at a time in the end of the list
fruits = ['Apple', 'Mango', 'Orange']
# fruits.append('Banana', 'Pineapple') # not workable, as we give 2 items to add at a time
print(fruits)
fruits.extend(['Banana', 'Pineapple']) # we don't give commas seperated values, we give it list of values to be added
print(fruits)

# remove() : removes certain elements from the list
fruits = ['Mango', 'Apple', 'Orange']
print(fruits)
fruits.remove('Mango')
print(fruits)
# fruits.remove('Banana') # gives value error as Banana is not exists and not a valid operation
fruits.insert(0, 'Mango')
fruits.insert(4, 'Mango')
print(fruits)
fruits.remove('Mango') # only remove first one mango not all present in list
print(fruits)

# pop() : removing items with their index no. : 
fruits.append('Mango')
print(fruits)
fruits.pop(1) # positve index
print(fruits)
fruits.pop(-1) # negative index
print(fruits)
fruits.pop() # by default last element delete from the list
print(fruits)
