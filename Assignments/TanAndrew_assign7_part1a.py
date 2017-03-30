#Andrew Tan, 3/30, Section 010, Part 1a

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
        print("Your username is valid!\n")
        break


            
