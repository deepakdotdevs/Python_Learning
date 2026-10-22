# Operator precedence determines which operator is evaluated first in an expression.
# It is the priority in which operations are performed in python
  
# and has the highter priority then or
name = "Deepak"
age = 21
print(name=='Deepak' or name=='Ramesh' and age<18)
print((name=='Deepak' or name=='Ramesh') and age<18)

print(5+10*6)
print((5+10)*6)

# Here is comes the concept for associativity :
# Associativity determines the order in which operators of the same precedence are evaluated in an expression.
print(100/10*10) # associativity is left to right
print(10*10/100) # associativity is left to right
print(2**1**3) # associativity is right to left

# Classifications of operators based on the number of operands :

# Unary Operator : If an operator operates on only one operand, it is called unary operator
# eg; - (-10), not True

# Binary Operator : Operates on two operands
# eg; a + b, a > b, True or False

# Ternary Operator : Uses three parts: a condition and two expressions
