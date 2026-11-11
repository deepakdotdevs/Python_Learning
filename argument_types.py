def add(a,b):
    return a+b

# Positional arguments - passing the arguments in order of their position
result = add(10,5)
print(result)

# ---------------------------

# Default arguments : Provide default values
def add(a=21,b=7):
    return a+b
result1 = add()
result2 = add(10,5)
print(result1)
print(result2)

# Prg 2 : 
def add(a, c, b=10):
    print(f"a: {a}, b: {b}, c: {c}")
    return a+b+c
result1 = add(40, 40,20)
result2 = add(40, 40) # takes by default value of b
print(result1)
print(result2)

# Prg 3 : What if we specify the only 1st and 3rd argument : 
def add(a, b=10,c=10):
    print(f"a: {a}, b: {b}, c: {c}")
    return a+b+c
# This known as keyword argument
result1 = add(a=40, c=50) # b=9 (we can change order too using keyword argument)
print(result1)