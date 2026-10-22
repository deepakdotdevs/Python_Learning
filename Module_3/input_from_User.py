# input() is used to take an input from the user, it returns string always btw we can typecast it
name = "Deepak" # it's known as hard coding

# # input() : 
# first_name = input()
# print(first_name)

# age = input()
# print(age)

# # input()  - 2 : 
# first_name = input("Enter Your Name: ")
# print(first_name)
# age = input("How old are you? ")
# print(age)

# # input() - 3 : # Output is string
# num1 = input("Enter a no. : ")
# num2 = input("Enter another no. : ")
# result = num1+num2
# print(result)

# # input() 3.1 : # Now output is calculated as per the expection as we convert nos from string to integer for calculation
# num1 = int(input("Enter a no. : "))
# num2 = int(input("Enter another no. : "))
# result  = num1+num2
# print(result)

# input() 4 : 
# year = int(input("What is the current year? "))
# age= int(input("What is your age? "))
# print("You were born in the year: ", (year-age))

# OR : 

year = input("What is the current year? ")
age = input("What is you age? ")
born_year = int(year)-int(age)
print("You were born in ", born_year)

