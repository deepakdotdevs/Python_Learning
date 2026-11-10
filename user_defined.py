# Program 1 : 

# Without an argument :
def greeting_someone(): 
    print("Hello, good morning!")
    print("It's a beautiful day.")

# calling a function
greeting_someone()
greeting_someone()
greeting_someone()

# With a argument : 
def greeting_someone(name): 
    print(f"Hello {name}, good morning!")
    print(f"It's a beautiful day.")

# calling a function
greeting_someone("Deepak")
greeting_someone("Thakur Shab")
greeting_someone("Blank")

# Program 2 : 
def even_or_odd(number):
    if number%2==0:
        print(f"{number} is Even No.")
    else:
        print(f"{number} is Odd No.")

even_or_odd(20)
even_or_odd(21)
even_or_odd(23)
even_or_odd(24)

# Program 3 : 
def add(a,b):
    result = a+b
    print(result)
add(2,4)
add(2,48)
add(2,42)