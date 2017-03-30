#Andrew Tan, 3/30, Section 010, Part 2a

#Ask user for input
name = str.lower(input("Name: "))

#Clean up user input
index = 0
for i in name:
    if ord(i) < 97 or ord(i) > 122:
        name = name.replace(name[index], "", 1)
    else:
        index += 1

#Calculate reduction value
reduction = 0
for i in name:
    reduction = reduction + ord(i) - 96

print("Your 'cleaned up' name is : %s" %(name))
print("Reduction: %d" %(reduction))

