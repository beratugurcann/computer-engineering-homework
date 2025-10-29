import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def result(a, b, operator):
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return subtract(a, b)
    elif operator == "*":
        return multiply(a, b)
    elif operator == "/":
        return divide(a, b)
    else:
        return "Invalid operation!"
    
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b!=0:
        return a/b
    else:
        print("Cannot divide by zero!!")
        return None
    
while True:
    select = input("enter: process,'C': clear,'Q': exit").lower()

    if select =='c':
        clear()
        continue
    elif select == 'q':
        print("exiting...")
        break

    try:
        first_value = float(input("Enter a number:"))
        process = input("Performed process (+, -, *, /):")
        second_value = float(input("Enter the second number:"))
        print("Result:",result(first_value,second_value,process))
    except ValueError:
        print("Please enter a valid number!!")
