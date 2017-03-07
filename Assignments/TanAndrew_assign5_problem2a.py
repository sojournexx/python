#Andrew Tan, 3/7, Section 010, Prime Number Finder

#Ask user for input and check validity
while True:
    num = int(input("Enter a positive number to test: "))
    if num > 0:
        print()
        break
    else:
        print("Sorry, that's not a positive number. Try again.\n")
        continue

#Check for divisiblity and display output
for i in range(2, num):
    if num % i != 0:
        print("%d is NOT a divisor of %d ... continuing" %(i, num))
    else:
        print("%d is a divisor of %d ... stopping" %(i, num))
        break

#Display conclusion
if num == 1:
    print("%d is not a prime number." %(num))
elif num == 2 or num == i+1:
    print("\n%d is a prime number!" %(num))
else:
    print("\n%d is not a prime number." %(num))
            
