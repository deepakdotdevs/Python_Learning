# def func():
#     '''
#     This is a docstring
#     We can write what the function does here
#     :return: None
#     '''
#     return None
# func()
# # we can print docstring using help()
# print(help(func))

# Program 2 : 
def divide(num1, num2):
    """
    num1: A number to be divided (numerator)
    num2: A number that divide num1 (denominator)
    :return: float (if num2 is non-zero) OR str (if num2 is 0)
    """
    if num2==0:
        return "Cannot divide as denominator is 0!"
    result = num1/num2
    return result
help(divide)
print(divide(10,0))
print(divide(10,4))

# It can provide information about what the function does, what are the arguments that it can have,
# what are the values that it returns, and so on and so forth.
# anything that it should be conveyed as the message or as the explanation or the documentation of your
# function can be written here.