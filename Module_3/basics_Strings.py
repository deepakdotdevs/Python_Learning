# How to find the length of the string?
# What is indexing?
# How to join string together? 

s1 = "Hello World !!"
print(type(s1))

s2 = "We are learning python"

s3 = """Hlo, there.
How are you?
Where are you from?
How can i help you??"""

s4 = "python"
print(len(s4))

print(len(s1))


# Indexing - Every character in python string has its own position, which is called index. Starts from 0 
# Indexing means the process of fetching a particular character using it's index or position.
# Indexing is done by using square brackers

s5 = "DEEPAK"
print(s5[0])
print(s5[3])
print(s5[5])
# print(s5[6]) # give error as index out of range

# To print the last character, length of that string - 1
s6 = "Hello world"
print(len(s6))
print(s6[10])

# print last character using negative indexing which is starts from -1 from the end
s7 = "Deepak Jangid"
print(s7[-1])
print(s7[-2])
print(s7[-3])

# Joining of two strings is done by + operator. This is called concatenation of strings
a1 = "My name is Deepak"
a2 = "I'm from India"
print(a1+" "+a2)