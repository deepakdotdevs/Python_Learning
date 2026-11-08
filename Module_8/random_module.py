# Modules - are python files that have some python code written in it. We can create our own modules by writing some programs.
# import is the keyword to import a module.

import random

# random() - returns random flot between 0.0 and 1.0 (excluded)
print(random.random())

# randint(a, b) - returns random int between a and b (both are included)
print(random.randint(10,15))

# choice(sequence) - takes a sequence as an argument, returns a random item from the sequence
nums =[10,4,1,8,4,3]
print(random.choice(nums))

# shuffle(sequence) - returns the elements shuffled in random order
fruits = ['apple','mango','orange']
random.shuffle(fruits)
print(fruits)