#Andrew Tan, 2/15, Section 010, NYU Calendar

#Ask user to input month and date
m = int(input("Enter a month (1-12): "))
d = int(input("Enter a day (1-31): "))

#Convert month format
if m == 1:
    month = "January"
elif m == 2:
    month = "Feburary"
elif m == 3:
    month = "March"
elif m == 4:
    month = "April"
elif m == 5:
    month = "May"
elif m == 6:
    month = "June"
elif m == 7:
    month = "July"
elif m == 8:
    month = "August"
elif m == 9:
    month = "September"
elif m == 10:
    month = "October"
elif m == 11:
    month = "November"
elif m == 12:
    month = "December"

#Check if date is valid
if m < 1 or m > 12 or d < 1: 
    print("That's not a valid date!")
elif m % 2 == 0 and d > 30 and m <= 7:
    print("That's not a valid date!")
elif m % 2 != 0 and d > 31 and m <= 7:
    print("That's not a valid date!")
elif m % 2 == 0 and d > 31 and m >= 8:
    print("That's not a valid date!")
elif m % 2 != 0 and d > 30 and m >= 8:
    print("That's not a valid date!")
elif m == 2 and d > 28:
    print("That's not a valid date!")

#Check if date is within spring semester
elif m <= 1 and d < 23:
    print("%s %d is before the start of the Spring 2017 term." %(month, d))
elif m >= 5 and d > 8:
    print("%s %d is after the end of the Spring 2017 term." %(month, d))

#Check if date is a holiday
elif m == 2 and d == 20:
    print("%s %d is President's day. NYU is not open on this day." %(month, d))
elif m == 3 and d >= 13 and d <= 19:
    print("%s %d is Spring Break. NYU is not open on this day." %(month, d))
else:
    print("%s %d is not a holiday at NYU. The university is open." %(month, d))


