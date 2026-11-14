# anonymous function - is when a function doesn't contain any name so those kind of functions are known as anonymous function or lambda functions
'''
# Without lambda expression:
def add(a,b):
    return a+b
res = add(1,2)
print(res)
'''

# Syntax of it:
# lambda  argument : expression

# With lambda expression
fun = lambda a,b : a+b
res = fun(3, 2)
print(res)