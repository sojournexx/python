#Andrew Tan, 4/12, Section 010, Part 1

#Create a list containing 1000 zeros
mylist = [0]
mylist *= 1000

mylist[0] = mylist[1] = 1

#Set list elements with index corresponding to prime numbers to one
for div in range(2, 1000):
    if mylist[div] == 1:
            continue
    for num in range(div*2, 1000):
        if num % div == 0:
            mylist[num] = 1

#Print output list of prime numbers
index = 0
counter = 0
for i in mylist:
    if i == 0:
        print("{:<4d}".format(index), end="")
        counter += 1
        if counter % 10 == 0 and counter != 0:
            print()
    index += 1
