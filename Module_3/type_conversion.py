# Type casting - Converting the data type from one to another 
# int, float, str

num1=100
print(type(num1))
print(num1)
# convert this from int to float
up = float(num1)
print(up)
print(type(up))

num1 = float(num1)
print(num1)
print(type(num1))

# Similarly a float can be converted into an integer
num3=52.36
print(type(num3))
# into an integer
num3 = int(num3)
print(num3)
print(type(num3))

# string :
num4=1000
print(type(num4))
num4=str(num4)
print(num4)
print(type(num4))

# NOTe : but we can't convert string into an numeric value

s2 = "12345"
s2 = int(s2)
print(type(s2))

s4 = '52.34'
s4=float(s4)
print(type(s4))

# Concatenation of String and Integer : 
language = "Python"
version = 3.13
# print(language+version) # gives error
print(language+" "+str(version))

str1 = '100'
str2 = '100'
print(str1+str2)
print(int(str1)+int(str2))