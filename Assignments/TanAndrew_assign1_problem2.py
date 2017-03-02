#Andrew Tan, 1/31, Section 010, Using the print function

#Ask user for 3 names
name1 = input("Please enter name #1: ")
name2 = input("Please enter name #2: ")
name3 = input("Please enter name #3: ")

#Printing all possible combinations
print("\nHere are your names in every possible order:", "--------------------------------------------", sep="\n")
print("\n1. ", name1, ", ", name2, ", ", name3, sep="")
print("\n2. ", name1, ", ", name3, ", ", name2, sep="")
print("\n3. ", name2, ", ", name1, ", ", name3, sep="")
print("\n4. ", name2, "\n", name3, "\n", name1, sep="")
print("\n5. ", name3, "\n", name2, "\n", name1, sep="")
print("\n6. ", name3, "\n", name1, "\n", name2, sep="")

