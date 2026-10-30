# if-else are use together always, if can be used without an else
# But else has to be used with if
# Syntax:
# if condition:
#     # block of code to be executed when condition is true
# else:
#     # block of code to be executed when condition is false

# Example No. 1:

# age = int(input("Enter Your Age : "))
# if age>=18:
#     print("Congrats, You can Vote")
# else:
#     print("Sorry, You can't be Vote")
# print("Rest of Program")

# Example No. 2:
num = int(input("Enter the number : "))
if num % 2 == 0:
    print(f"{num} is Even No.")
else:
    print(f"{num} is Odd No.")