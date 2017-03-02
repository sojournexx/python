#Andrew Tan, 2/2, Section 010, Dynamic Tip Calculator

print("Hello! I'm here to help you calculate your tip.")

#Ask user for inputs
bill = float(input("How much was your bill? (enter as a number without dollar signs or commas): "))
tip_pct = float(input("How much tip would you like to leave? (enter just a number): "))

#Calculate tip amount and total bill
tip = tip_pct / 100 * bill
total = tip + bill

#Print outputs
print("Thanks!")
print("You need to leave $%.2f as a tip." %(tip))
print("Your total bill will be $%.2f" %(total))
