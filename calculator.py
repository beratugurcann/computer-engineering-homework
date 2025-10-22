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
        print("Result:",result(first_value,process,second_value))
    except ValueError:
        print("Please enter a valid number!!")


    import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

    import os 
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