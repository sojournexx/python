#Andrew Tan, 2/15, Section 010, Guess the Number Game

from random import randint 

#Assign random value to secret number
print("I'm thinking of a number between 1 and 10!")
num2 = randint(1,10)
x = 1

#Check if number guessed is less than, equal to, or greater than secret number
while x <= 3:
    num1 = int(input("What's your guess? "))    
    if num1 > num2:
        print("Too high, try again.")
        x += 1
    elif num1 < num2:
        print("Too small, try again.")
        x += 1
    else:
        print("You got it!")
        print("The secret number was %d." %(num2))
        if x == 1:
            print("It took you %d try to guess the number." %(x))
        else:
            print("It took you %d tries to guess the number." %(x))
        break

#Stop game after 3 unsuccessful tries
if x == 4:
    print("The secret number was %d." %(num2))
    print("You didn't guess the number.")

