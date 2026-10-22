# Comparison Operators : it will compare two operands or two values
# ==, !=, >, <, >=, <=

a = 100
b = 90
c = 90

# == Operator :
print(b==c) # True
print(a==b) # False
print('python'=='python') # True
print('python'=="python") # True
print('Python'=='python') # False

print("----------------------")
# != Operator : 
print(a!=b)
print(b!=c)

print("----------------------")
# > - Greater than Operator : 
print(a>b)
print(b>c)

print("----------------------")
# < - Less than Operator : 
print(a<b)
print(b<c)
print(b<a)

print("----------------------")
# >= Greater than equal to operator : 
num4=90
print(a>=b)
print(b>=c)

print("----------------------")
# <= Less than equal to operator : 
num4=90
print(a<=b)
print(b<=c)
print("\n")
print("----------------------")
print("\n")

# Logical Operators : 

# and : True if both conditions are true
a = 5
b = 10
c = 5
print(a>=c and b>c)
print(a>c and b>c)

print("----------------------")
# or : True if any one conditions are true
print(a>c or b>c)
print(a>b or c>b)

print("----------------------")
# not : returns true if the operand is false and it returns false if the operand is true
print(not(a>=5))
print(not(a>5))

print("----------------------")

name='Deepak'
age = 21
print(name=='Deepak' and age>=18)
print(name=='Deepak' and age==18)

print(name=='Deepak' or age==18)
