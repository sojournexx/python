#Andrew Tan, 2/16, Section 010, Arrows

#Define right()
def right():    
    #Define variables
    trow = tcol + tcol - 1
    row = 1

    #Top half
    while row <= tcol:
        rep = 1
        while rep < row:
            print(" ", end="")
            rep += 1
        print("*")
        row += 1
        
    #Bottom half
    while row <= trow:
        rep = trow - row
        while rep > 0:
            print(" ", end="")
            rep -= 1
        print("*")
        row += 1

    return

#Define left
def left():
    #Define variables
    trow = tcol + tcol - 1
    row = 1

    #Top half
    while row <= tcol:
        rep = tcol - row
        while rep > 0:
            print(" ", end="")
            rep -= 1
        print("*")
        row += 1
                
    #Bottom half
    while row <= trow:
        rep = 1
        while rep < row - tcol + 1:
            print(" ", end="")
            rep += 1
        print("*")
        row += 1

    return

#Check for valid number of columns and valid direction
while True:
    tcol = int(input("How many columns? "))
    if tcol < 0:
        print("Invalid entry, try again!")
        continue
    direction = input("Direction? (l)eft or (r)ight: ")
    if direction != "l" and direction != "r":
        print("Invalid entry, try again!")
        continue
    break

#Run program
if direction == "r":
    right()
elif direction == "l":
    left()
