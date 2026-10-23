# List : is a data structure or a data type in which we can store collection of data. Any type of data in a single variable or a single data type
# List are a collection of items or data within them which can store any type of data
# Square brackets are used
# List are ordered

name = "John"
age = 21
percent = 85.5

student = ['John', 21, 85.5]
print(type(student)) # Output is list
print(student)

# List are ordered
days_of_week = ['Monday', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# Indexing in list same as string, starts from 0 as it in ordered manner
print(days_of_week[0])
print(days_of_week[5])
print(f"Last day of week is {days_of_week[-1]}")

# Length of a list => the number of items/elements in the list
print(len(days_of_week)) # as 7 elements stored in the list

# print(days_of_week[8]) # error as list index out of range