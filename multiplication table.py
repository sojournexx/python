size = int(input("Enter the size of your multiplication table: "))

print()
print("Multiplication Table Generator")
print()
print("     ", end="")
for header in range(1, size+1):
    print(format(header, "<5d"), end="")

print()
for i in range(1, size*5+4+1):
    print("-", end="")

for y in range(1, size+1):
    print()
    print("%d |" %(y), end="  ")
    for x in range(1, size+1):
        print(format(x*y, "<5d"), end="")
