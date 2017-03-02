from random import randint 

num1 = int(input("Number from 1 to 10: "))
num2 = randint(1,10)

while num1 != num2:
    
    if num1 > num2:
        print("Number is too large, try again")
        num1 = int(input("Number from 1 to 10: "))
    else:
        print("Number is too small, try again")
        num1 = int(input("Number from 1 to 10: "))

print("You win, game over")
