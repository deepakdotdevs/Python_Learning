s1 = "Python is fun"
print(s1[0])
print(s1[-1])
print(len(s1))

language = "Python"
version = "3.13.3"
print(language+version)
# print(language-version) # not possible as it's a string
print(language*3) # workable
# in string, '*' is repetition operator

# Checking of membershiop or membershiop operation in string. 
# in operator is known as membershiop operator

s1 = 'Python is fun'
print("Python" in s1) # is the "Python" character is present in s1 (Boolean output)
print("i" in s1)
print("z" in s1)
print('Java' in s1)

# not in : opposite of in
s1 = 'Python is fun'
print("Python" not in s1)
print("i" not in s1)
print("z" not in s1)
print('Java' not in s1)

print("-------------------")

# Comparison of strings :
print('Python' == "Python")
print('Python ' == "Python")

# Removing spaces (unnecessary spaces only) from a string - function called - strip() : 

s1 = "          Python "
s2 = s1.strip()
print(s2)
print(s1.strip() == "Python")

# replace() function : replace function is used to replace a part of a string or a character from a string.

s1 = "We are learning Python"
# change Python into Java
print(s1)
print(s1.replace("Python", "Java"))
print(s1) # we not reassigning this, so the original output should be same as before
print(s1.replace('e', 'E')) # it replace all of characters present
# the way, in which we only replace one time or first time not all 
print(s1.replace('e', 'E', 1))
print(s1.replace('e', 'E', 2))
