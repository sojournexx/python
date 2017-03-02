#Andrew Tan, 2/15, Section 010, Valid Triangle Tester

print("Valid Triangle Tester")

#Ask user for 3 points on a standard Cartesian plane
x1 = int(input("Enter Point #1 - x position: "))
y1 = int(input("Enter Point #1 - y position: "))
x2 = int(input("Enter Point #2 - x position: "))
y2 = int(input("Enter Point #2 - y position: "))
x3 = int(input("Enter Point #3 - x position: "))
y3 = int(input("Enter Point #3 - y position: "))

print()

#Calculate length of sides
s1 = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
s2 = ((x2 - x3)**2 + (y2 - y3)**2)**0.5
s3 = ((x3 - x1)**2 + (y3 - y1)**2)**0.5

#Display length of sides in output
print("The length of each side of your test shape is:")
print("Side 1: %.2f" %(s1))
print("Side 2: %.2f" %(s2))
print("Side 3: %.2f" %(s3))

print()

#Check for a valid triangle
if s1 + s2 > s3 and s2 + s3 > s1 and s3 + s1 > s2:
    print("This is a valid triangle!")
else:
    print("This is not a valid triangle")
