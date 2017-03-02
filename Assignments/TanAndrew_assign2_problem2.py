#Andrew Tan, 2/2, Section 010, Grade Calculator

#Ask user for name and class
name = input("What is your name? ")
course = input("What class are you in? ")

print()

#Ask user for weightage and test scores
weight_test = float(input("How much are tests worth in this class (i.e. 0.40 for 40%): "))
test1 = float(input("Enter test score #1: "))
test2 = float(input("Enter test score #2: "))
test3 = float(input("Enter test score #3: "))

print()

#Calculate and display test avg
test_avg = (test1 + test2 + test3) / 3
print("Your test average is: %.2f" %(test_avg))

print()

#Ask user for weightage and hw scores
weight_hw = float(input("How much are homework assignments worth in this class (i.e. 0.60 for 60%): "))
hw1 = float(input("Enter homework score #1: "))
hw2 = float(input("Enter homework score #2: "))
hw3 = float(input("Enter homework score #3: "))

print()

#Calculate and display hw avg
hw_avg = (hw1 + hw2 + hw3) / 3
print("Your homework average is: %.1f" %(hw_avg))

print()

#Calculate and display final score
total = hw_avg * weight_hw + test_avg * weight_test
print("Thanks, %s. Your final score in %s is %.2f" %(name, course, total))
