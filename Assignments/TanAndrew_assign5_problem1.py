#Andrew Tan, 3/7, Section 010, 99 Bottles of Beer on the Wall

#Ask user for input and check validity of number of beer bottles
while True:
    beer = int(input("How many bottles of beer on the wall? "))
    if beer > 0:
        print("\nOK, here we go!\n")
        break
    else:
        print("Sorry, that's not a valid number of bottles. Try again.\n")
        continue

#Display output
for i in range(beer, 1, -1):
    print("%d bottles of beer on the wall, %d  bottles of beer." %(i, i))
    print("Take one down, pass it around, %d bottles of beer on the wall.\n" %(i-1))

print("1 bottle of beer on the wall, 1 bottle of beer.")
print("Take it down, pass it around, no more bottles of beer on the wall!")
