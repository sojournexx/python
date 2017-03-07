#Andrew Tan, 2/16, Section 010, Roll the Dice

from random import randint

result = False

while result == False:
    s = int(input("How many sides on your dice? "))

    #Check for valid data
    if s < 3:
        print("Sorry, that's not a valid size value. Please choose a positive number.")
        continue

    #Roll the dice and display roll result
    else:
        print()
        print("Thanks! Here we go ...")
        print()
        counter = 0
        doubles = 0
        t1 = 0
        t2 = 0
        while result == False:
            counter += 1
            d1 = randint(1, s)
            d2 = randint(1, s)
            t1 = t1 + d1
            t2 = t2 + d2
            print("%d. die number 1 is %d and die number 2 is %d." %(counter, d1, d2))
            #Check for doubles
            if d1 != d2:
                continue
            else:
                doubles += 1
                #Check for snake eyes
                if d1 != 1 and d2 != 1:
                    continue                    
                else:
                    print()
                    print("You got snake eyes! Finally! On try number %d!" %(counter))
                    print("Along the way you rolled doubles %d times" %(doubles))
                    print("The average roll for die #1 was %.2f" %(t1 / counter))
                    print("The average roll for die #2 was %.2f" %(t2 / counter))
                    result = True

        
        
