#Andrew Tan, 3/30, Section 010, Part 1b

#Ask user for username and validate
while True:
    username = str(input("Please enter a username: "))
    if len(username) < 8 or len(username) > 15:
        print("Username must be between 8 and 15 characters.\n")
        continue
    if username.isalnum() == False:
        print("Username must contain only alphanumeric characters.\n")
        continue
    if str.isnumeric(username[0])== True:
        print("The first character in your username cannot be a digit.\n")
        continue
    if username.islower() == True:
        print("Your username must contain at least one uppercase character.\n")
        continue
    if username.isupper() == True:
        print("Your username must contain at least one lowercase character.\n")
        continue
    if username.isalpha() == True:
        print("Your username must contain at least one digit.\n")
        continue
    else:
        print("Your username is valid!\n\n")
        break

#Ask user for password and validate
while True:
    #Define counters
    lower = 0
    upper = 0
    num = 0
    special = 0
    invalid = False
    
    password = str(input("Please enter a password: "))
    for i in password:
        if i.islower() == True:
            lower += 1
        elif i.isupper() == True:
            upper += 1
        elif i.isnumeric() == True:
            num += 1
        elif ord(i) >= 35 and ord(i) <= 38:
            special += 1
        else:
            invalid = True
    if len(password) < 8:
        print("Passwords must be at least 8 characters long.\n")
        continue
    if (username in password):
        print("You cannot use your username as part of your password.\n")
        continue
    if invalid == True:
        print("Your password contains at least one invalid character.\n")
        continue
    if num == 0:
        print("Your password must contain at least one digit.\n")
        continue
    if upper == 0:
        print("Your password must contain at least one uppercase character.\n")
        continue
    if lower == 0:
        print("Your password must contain at least one lowercase character.\n")
        continue
    if special == 0:
        print("Your password must contain at least one 'special' character.\n")
        continue
    else:
        print("Your password is valid!")
        break
    
    
    
                    
