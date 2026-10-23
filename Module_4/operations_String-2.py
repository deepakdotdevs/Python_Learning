# Operations on String - count, cases, start, end etc 

# count() - counting substring from a string 
# s1 = "we are learning Python. Python is fine."
# s2 = "Python"
# print(s1.count(s2))
# print(f"Occuerrances of {s2} is {s1.count(s2)}")
# s3 = 'e'
# print(f"Occurrances of {s3} is {s1.count(s3)}")
# s4 = 'learn'
# print(f"Occurrances of is {s1.count(s4)}")
# s5 = ' '
# print(f"Occurrances of space is {s1.count(s5)}")

# Cases : Changing case of a string : 
# upper(), lower(), title(), capatilize()

s1 = "Python3.13.3"
print(s1.upper())
print(s1.lower())
s2 = "we are learning python"
print(s2.upper())
print(s2.lower())

# title() : All first alphabets of every word or complete string, make them capital
s3 = "we are learning python"
print(s3.title())

# capitalize() : Make capital letter of entire string and all small. 
s4 = "my name is DEEPAK"
print(s4.capitalize())

print("------------------------------")

# startswith() - checks if or whether a string is starting with another substring or not.
# endswith() - checks if or whether a string is ending with another substring or not.
# Output is in boolean

s6 = "We are learning python."
print(s6.startswith('w'))
print(s6.startswith('W'))
print(s6.startswith('we are'))
print(s6.startswith('We are le'))
print(s6.startswith('are'))

# endswith() : 
s7 = "We are learning python."
print(s6.endswith('n.'))
print(s6.endswith(' python.'))
print(s6.endswith('we are'))
print(s6.endswith('thon.'))
print(s6.endswith('are'))