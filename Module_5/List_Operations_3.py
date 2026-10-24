# List Operations - reverse(), sort(), count(), membership operations : 

# reverse() : 
days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print(days_of_week)
# reverse() : it changes the list itself
days_of_week.reverse()
print(days_of_week)

# sort() : sort in ascending order
nums = [4,5,6,3,2,1]
print(nums)
nums.sort()
print(f"Sorted Ascending list is: {nums}")
nums.sort(reverse=True) # Use for sorting in descending order
print(f"Sorted Descending list is: {nums}")

# coun() : counts a particular element in the list, how many times it occurred : 
# nos = [0,1,2,3,4,0,6,5,4,4,0,7, 0 , 0]
# print(f"The List is: {nos}")
# item_to_count = int(input("Enter the number to be counted: "))
# print(nos.count(item_to_count))
# # SAME as for STRING
# nos = ['Python', 'Java', 'C++', 'C', 'Python']
# print(f"The List is: {nos}")
# item_to_count = input("Enter the number to be counted: ")
# print(nos.count(item_to_count))


# Membership operators or membership operations in list : 
# in is membership operator : in checks if a particular element or item is present in the list or not.
# Output is in Boolean : True or False
language = ['Python', 'Java', 'C++', 'C', 'Python']
print('Python' in language)
print('python' in language)

# not in (also a membership operator) :
print('Python' not in language)
print('python' not in language)
print('Python ' not in language)