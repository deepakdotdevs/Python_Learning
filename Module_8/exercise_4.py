import random
num=1
print(" Welcome to the number guessing game we have a number that needs to be guessed we have 10 attempts")
print(" The security number is between one and 50")
attemps=10
is_guess_correct = False
secret_number= random.randint(1,50)

while num<=10:
    print(f"You have {attemps} attemps remaining")
    user_input = int(input("Enter your guess: "))
    if user_input==secret_number:
        print("Congrats, your guess is correct!")
        is_guess_correct = True
        break
    else:
        if user_input<secret_number:
            higher_or_lower = "higher"
        else :
            higher_or_lower = "lower"
        print(f"Your guess is wrong! Try {higher_or_lower}")
    num+=1
    attemps-=1
if not is_guess_correct: # or == False:
    print("Bad Luck!! You exhausted all your attemps couldn't guess the number")

print(f"The secret number was {secret_number}. GAME OVER")