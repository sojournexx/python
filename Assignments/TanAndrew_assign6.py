#Andrew Tan, 3/25, Section 010

import myfunctions
import random

#Ask user for inputs and check validity
while True:
    qns = int(input("How many problems would you like to attempt? "))
    if qns <= 0:
        print("Invalid number, try again\n")
        continue
    else:
        break

while True:
    width = int(input("How wide do you want your digits to be? 5-10: "))
    if width < 5 or width > 10:
        print("Invalid width, try again\n")
        continue
    else:
        break

while True:
    drill = str.lower(input("Would you like to activate 'drill' mode? yes or no: "))
    if drill != "yes" and drill != "no":
        print("Invalid response, try again\n")
        continue
    else:
        break
    
print("\nHere we go!")

#Define variables to track score and statistics
tscore = 0
addition = 0
subtraction = 0
multiplication = 0
division = 0
addition_score = 0
subtraction_score = 0
multiplication_score = 0
division_score = 0

#Set number of questions
for i in range(qns):
    print("\nWhat is .....\n")

    #Define parameters
    x = random.randint(0, 9)
    op = random.randint(1, 4)
    y = random.randint(0, 9)

    #Check for valid division equation
    if op == 4:
        if y == 0:
            y = random.randint(1, 9)
        while x % y != 0:
            x = random.randint(0, 9)
            y = random.randint(1, 9)
        
#Display first number
    if x == 0:
        myfunctions.number_0(width)
    elif x == 1:
        myfunctions.number_1(width)
    elif x == 2:
        myfunctions.number_2(width)
    elif x == 3:
        myfunctions.number_3(width)
    elif x == 4:
        myfunctions.number_4(width)
    elif x == 5:
        myfunctions.number_5(width)
    elif x == 6:
        myfunctions.number_6(width)
    elif x == 7:
        myfunctions.number_7(width)
    elif x == 8:
        myfunctions.number_8(width)
    elif x == 9:
        myfunctions.number_9(width)

#Display operator
    if op == 1:
        op = "+"
        myfunctions.plus(width)
        addition += 1
    elif op == 2:
        op = "-"
        myfunctions.minus(width)
        subtraction += 1
    elif op == 3:
        op = "*"
        myfunctions.multiply(width)
        multiplication += 1
    elif op == 4:
        op = "/"
        myfunctions.divide(width)
        division += 1

#Display second number
    if y == 0:
        myfunctions.number_0(width)
    elif y == 1:
        myfunctions.number_1(width)
    elif y == 2:
        myfunctions.number_2(width)
    elif y == 3:
        myfunctions.number_3(width)
    elif y == 4:
        myfunctions.number_4(width)
    elif y == 5:
        myfunctions.number_5(width)
    elif y == 6:
        myfunctions.number_6(width)
    elif y == 7:
        myfunctions.number_7(width)
    elif y == 8:
        myfunctions.number_8(width)
    elif y == 9:
        myfunctions.number_9(width)

#Ask user for answer and check answer
    if drill == "no":
        z = int(input("= "))
        if myfunctions.check_answer(x, y, z, op) == True:
            print("Correct!")
            tscore += 1
            if op == "+":
                addition_score += 1
            if op == "-":
                subtraction_score += 1
            if op == "*":
                multiplication_score += 1
            if op == "/":
                division_score += 1
        else:
            print("Sorry, that's not correct.")
            
    elif drill == "yes":
        while True:
            z = int(input("= "))
            if myfunctions.check_answer(x, y, z, op) == False:
                print("Sorry, that's not correct.")
                if op == "+":
                    addition_score += 1
                if op == "-":
                    subtraction_score += 1
                if op == "*":
                    multiplication_score += 1
                if op == "/":
                    division_score += 1
                continue
            else:
                print("Correct!")
                break
#Display score
if drill == "no":
    print("\nYou got %d out of %d correct!" %(tscore, qns))

    for operator, count, score in zip(["addition", "subtraction", "multiplication", "division"], [addition, subtraction, multiplication, division], [addition_score, subtraction_score, multiplication_score, division_score]):
        if count == 0:
            print("\nNo %s problems presented" %(operator))
        else:
            print("\nTotal %s problems presented: %d" %(operator, count))
            print("Correct %s problems: %d (%s)" %(operator, score, format(score/count, ".1%")))
elif drill == "yes":
    for operator, count, score in zip(["addition", "subtraction", "multiplication", "division"], [addition, subtraction, multiplication, division], [addition_score, subtraction_score, multiplication_score, division_score]):
        if score == 0:
            praise = "(perfect!)"
        else:
            praise = ""
        if count == 0:
            print("\nNo %s problems presented" %(operator))
        else:
            print("\nTotal %s problems presented: %d" %(operator, count))
            print("# of extra attempts needed: %d %s" %(score, praise))
