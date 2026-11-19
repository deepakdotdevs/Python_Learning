# Module - is a file containing definitions and statements
# Mostly functions that are defined in a python file
# Any python file having python code in it with the extesion of .py file is a module
# A Module can also contain executable code or runnable code 

# Why use Modules in python ?
# similar type of tasks or functions can be made part of the single file so that it can be grouped
# together so that the code or the project is easier to read.
# Two types of modules in Python :- built-in modules & user-defined modules

# Built-In Modules :are the modules which are available when we install python in our system.
# We have to do import and use that module
# math, random, datetime, ....


# How to import a module in Python
# Syntax: import module_name
# Syntax for importing only few functions/variables: from module_name import f1, f2, f3

# math module : 
# import math
# # calculate square root of a number
# num = 100
# output= math.sqrt(num)
# print(f"Square root of {num} is {output}")

# # Calculate the area of a circle => Pi.r^2 (pi = 3.14)
# radius = 5
# area_of_circle = math.pi*(radius**2)
# print(f"Area of circle with radius {radius} is {area_of_circle}")
# print(math.pi)

# random module : without importing random completely, Here we just import a function
# throw a die
# from random import randint
# value = randint(1,6)
# print(value)

# --------------------------------------------------------

# Syntax to create an alias for the module that is imported: import module_name as alias_name

import datetime as dt # any alias we use
t=dt.time(0,43,51)
print(t)