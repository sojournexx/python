#Andrew Tan, 3/7, Section 010, Custom Number Range

#Ask user for input and check validity
while True:
    start = int(input("Start number: "))
    end = int(input("End number: "))
    if start <= 0 or end <= 0:
        print("Start and end must be positive")
        continue
    elif end <= start:
        print("End number must be greater than start number")
        continue
    else:
        break

count = 1

#Iterate numerator
for num in range(start, end+1):
    if num == 2:
        print(format(num, ">5d"), end="")

    #Iterate divisor
    for div in range(2, num):
        if num % div == 0:
            break
        if div == num-1:
            print(format(num, ">5d"), end="")
            count += 1

            #align 10 prime numbers per line
            if count % 10 == 0:
                print()
