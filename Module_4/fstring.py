# fstrings is a way to format strings in python
# An f-string (formatted string literal) is used to insert variables and expressions directly inside a string using {}.

# Eg 1: 

# name = 'John'
# age = 21

# # John is 20 years old.
# print(name, "is", age, "years old.") # without fstring
# print(f"{name} is {age} years old.") # with fstring

# Eg 2: 

# name = "Deepak"
# age= 21
# language ="Python"
# hours=3
# # to print (Deepak is 20 years old. He studies Python 3 hours a day.) using fstring
# print(f"{name} is {age} years old. He studies {language} {hours} hours a day")

# Eg 3: 

name = "Deepak"
sub1 = 78
sub2 = 87
sub3 = 83

print(f"{name} scored {sub1+sub2+sub3} marks in total.")
percent = (sub1+sub2+sub3)/3
print(f"{name} got {percent}%")
print(f"{name} got {round(percent, 2)}%")
