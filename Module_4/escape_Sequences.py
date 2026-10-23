# Escape sequences are special character combinations that begin with a backslash (\) and are used to perform special actions inside strings.
# Basically these are used when we need to include
# certain special characters in a string which we cannot otherwise include or it is difficult to include
# in the string or directly type.

# \n - new/next line
# \t - tab
# \\ - backslast
# /' - inserts a single quote inside a single-quoted string

# \n : 
print("Hello everyone.\nHow are you?")

# \t : 
print("Deepak\t21")

# \\ : 
print("new\old") # we can't print with "\" symbol
print("new\\old") # So, we use \\ to print \ one time
print("yes\\no")

# \' : 
# print('This is Python's class') # Gives error
print('This is Python\'s class') # It's workable
print("This is Python's class") # It's too workable

# \" : what if we want double quotes to print in our output
# print("He says, "we are learning Python"") # Not Workable, output is error
print("He says, \"we are learning Python\"")

