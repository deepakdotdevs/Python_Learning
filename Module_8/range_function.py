# range() function in python and how it can be used with for loop.
# The range() function is used to generate a sequence of numbers, commonly used with for loops.
# it is built-in function used to generate integers. Generate may be sequence of integers in a given interval
# Syntax :
# range(start, stop, step) stop is not included 
# for i in range(start, stop, step):
#     statements

for i in range(1,10,1):
    print(i)

# generate even numbers b/w 1 and 10. 10 is excluded:
for p in range(2,10,2):
    print(p)

# generate reverse order => 20 to 10 (10 is excluding)
for i in range(20,10,-1):
    print(i)

# generate reverse order only even nos => 20 to 10 (10 is excluding)
for i in range(20,10, -2):
    print(i)

# Countdown from 10 to 1 (1 included) :
for i in range(10,0,-1):
    print(i)
print("Happy New Year !!!")

# -------------------------------------------------------------------------

print("-----------------------------")

# range 2nd Syntax : range(start, stop) # step is 1 by default : 
for i in range(1,5): # step => 1
    print(i)

# range(stop) => 0 to stop-1 with a step of 1, start = 1 by default
for i in range(5): # start is 0 and stop is 5
    print(i)

print("-----------------------------")
# -------------------------------------------------------------------------

# Use case : 
groceries = ['salt', 'milk', 'sugar']
for items in groceries:
    print(items)
# How to fetch indexes too using for loop
for index in range(len(groceries)):
    print(index)

print("-----------------------------")
# ----------------------------------------------------------------------

profits = [9,11,6,10]
# You have to do this : 
# Profit of quarted 1 is 9
# Profit of quarted 2 is 11
# Profit of quarted 3 is 6
# Profit of quarted 4 is 10
for quarter in range(len(profits)):
    print(f"Profit of quarter {quarter+1} is {profits[quarter]}")