#Andrew Tan, 3/30, Section 010, Part 2b

#Ask user for input
name = str.lower(input("Name: "))

#Clean up user input
index = 0
for i in name:
    if ord(i) < 97 or ord(i) > 122:
        name = name.replace(name[index], "", 1)
    else:
        index += 1
print("Your 'cleaned up' name is : %s" %(name))

#Create dictionary of traits
traits = {"0" : "emptiness",
          "1" : "independence",
          "2" : "quiet",
          "3" : "charming",
          "4" : "harmony",
          "5" : "new directions",
          "6" : "love",
          "7" : "spirituality",
          "8" : "organization",
          "9" : "romatic",
          "11" : "idealism",
          "12" : "perfectionist",
          "22" : "builder"}
          
#Calculate reduction value
reduction = 0
for i in name:
    reduction = reduction + ord(i) - 96
while reduction not in range(10) and reduction not in [11, 12, 22]:
    print("Reduction: %d" %(reduction))
    str_reduction = str(reduction)
    reduction = 0
    for i in str_reduction:
        reduction += int(i)
print("Reduction: %d" %(reduction))
print("Your name reduces to ... %d - %s!" %(reduction, str.capitalize(traits[str(reduction)])))
