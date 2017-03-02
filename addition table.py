print("Addition Table Generator")
first = int(input("First number: "))
last = int(input("Last number: "))

for base in range(first, last+1):
    print()
    print("Addition Table for %d" %(base))
    for i in range(1, 11):
        print("%d plus %d is %d" %(base, i, i+5))
