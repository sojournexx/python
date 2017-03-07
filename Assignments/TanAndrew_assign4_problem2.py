#Andrew Tan, 2/17, Section 010, Pick Up Sticks

player = 1

#Check for valid number of sticks
while True:
    sticks = int(input("How many sticks are on the table? (enter a number between 10 and 100): "))
    if sticks < 10 or sticks > 100:
        print("Invalid # of sticks, please try again.")
        continue
    break

#Display results of each turn
while True:
    print()
    print("There are %d sticks on the table." %(sticks))
    print("Turn: Player %d" %(player))
    #Check for valid number of sticks removed
    removed = int(input("How many sticks do you want to remove from the table? (1, 2 or 3): "))
    if removed < 1 or removed > 3 or removed > sticks:
        print("Invalid number of sticks, try again.")
        continue
    sticks = sticks - removed
    #End game when no sticks are left
    if sticks == 0:
        print("Player %d loses!" %(player))
        break
    #Proceed to the next turn
    if player < 2:
        player += 1
    else:
        player = 1
    
