#Define functions to draw basic lines making up digits 0-9
def horizontal_line(width):
    for i in range(width):
        print("*", end="")
    print()
    return

def vertical_line(shift, height):
    for x in range(height):
        for y in range(shift):
            print(" ", end="")
        print("*")
    return

def two_vertical_lines(height, width):
    for x in range(height):
        print("*", end="")
        for y in range(width-2):
            print(" ", end="")
        print("*")
    return

#Define functions for displaying digits 0-9
def number_0(width):
    horizontal_line(width)
    two_vertical_lines(3, width)
    horizontal_line(width)
    print()
    return

def number_1(width):
    vertical_line(width-1, 5)
    print()
    return

def number_2(width):
    horizontal_line(width)
    vertical_line(width-1, 1)
    horizontal_line(width)
    vertical_line(0, 1)
    horizontal_line(width)
    print()
    return

def number_3(width):
    horizontal_line(width)
    vertical_line(width-1, 1)
    horizontal_line(width)
    vertical_line(width-1, 1)
    horizontal_line(width)
    print()
    return

def number_4(width):
    two_vertical_lines(2, width)
    horizontal_line(width)
    vertical_line(width-1, 2)
    print()
    return

def number_5(width):
    horizontal_line(width)
    vertical_line(0, 1)
    horizontal_line(width)
    vertical_line(width-1, 1)
    horizontal_line(width)
    print()
    return

def number_6(width):
    horizontal_line(width)
    vertical_line(0, 1)
    horizontal_line(width)
    two_vertical_lines(1, width)
    horizontal_line(width)
    print()
    return

def number_7(width):
    horizontal_line(width)
    vertical_line(width-1, 4)
    print()
    return

def number_8(width):
    horizontal_line(width)
    two_vertical_lines(1, width)
    horizontal_line(width)
    two_vertical_lines(1, width)
    horizontal_line(width)
    print()
    return

def number_9(width):
    horizontal_line(width)
    two_vertical_lines(1, width)
    horizontal_line(width)
    vertical_line(width-1, 1)
    horizontal_line(width)
    print()
    return

#Define functions to display operators
def plus(width):
    vertical_line(int(width/2), 2)
    horizontal_line(width)
    vertical_line(int(width/2), 2)
    print()
    return

def minus(width):
    horizontal_line(width)
    print()
    return

def multiply(width):
    two_vertical_lines(2, width)
    vertical_line(int(width/2), 1)
    two_vertical_lines(2, width)
    print()
    return

def divide(width):
    vertical_line(int(width/2), 1)
    print()
    horizontal_line(width)
    print()
    vertical_line(int(width/2), 1)
    print()
    return

#Define function to check answer
def check_answer(num1, num2, num3, op):
    correct = False
    if op == "+":
        if num1 + num2 == num3:
            correct = True        
    elif op == "-":
        if num1 - num2 == num3:
            correct = True       
    elif op == "*":
        if num1 * num2 == num3:
            correct = True        
    elif op == "/":
        if num1 / num2 == num3:
            correct = True
    return correct
    
