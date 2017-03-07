#Andrew Tan, 3/7, Section 010, Find all Prime Numbers between 1 and 1000

#Iterate numerator
for num in range(1, 1001):
    if num == 2:
        print("%d is a prime number!" %(num))

    #Iterate divisor
    for div in range(2, num):
        if num % div == 0:
            break
        if div == num-1:
            print("%d is a prime number!" %(num))
