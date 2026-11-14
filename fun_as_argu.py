# In python, we can pass a function as argument of another function
# We have to do it, take user input, add 1 to it and then square it

def add_1(number):
    return number+1
print(add_1(10))

def square(number):
    return number**2

num= int(input("Enter a number: "))
# On place of these two variables, we use res (result) in which function in function 
# res_1 = add_1(num)
# res_2 = square(res_1)
res = square(add_1(num))
print(f"Output is: {res}")
