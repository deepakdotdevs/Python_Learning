# Program 1 :

# Without return:
# def even_odd(num):
#     if num%2==0:
#         print("Even")
#     else:
#         print("Odd")
# result = even_odd(9)
# print(result) # returns None as no return value in the even_odd function

# With return:
# def even_odd(num):
#     if num%2==0:
#         return "Even"
#     else:
#         return "Odd"
# result = even_odd(10)
# print(result)

# Program 2 : 

# With return :
# def add(a,b):
#     result = a+b
#     return result
# val_1= int(input("Enter 1st number: "))
# val_2= int(input("Enter 2nd number: "))
# val = add(val_1, val_2)
# print(f"Sum of {val_1} + {val_2} = {val}")

# Is it possible returning multiple values - Yes !! Program as Follow : 
def arithmetic(num1, num2):
    add = num1+num2
    sub = num1-num2
    mul = num1*num2
    return add, sub, mul
val_1 = int(input("Enter 1st number: "))
val_2 = int(input("Enter 2nd number: "))
res1, res2, res3 = arithmetic(val_1, val_2)
print(f"Addition of {val_1} and {val_2} is {res1}")
print(f"Subtract of {val_1} and {val_2} is {res2}")
print(f"Multiple of {val_1} and {val_2} is {res3}")