# Program for a Simple Calculator in Python
while True:
    # Options
    print(
        "Enter 1 to ADD Two Numbers:\n" \
        "Enter 2 to SUBTRACT Two Numbers:\n" \
        "Enter 3 to MULTIPLY Two Numbers:\n" \
        "Enter 4 to DIVIDE Two Numbers:\n" \
        "Enter q or Q to Exit")

    # Operation to be performed
    operation = input()

    # Exit Condition for Calculator
    if operation == 'q' or operation == 'Q':
        break

    # Take the numbers as input
    num_1 = float(input("Enter the First Number: "))
    num_2 = float(input("Enter the Second Number: "))
    operation = int(operation)
    print()

    # Addition
    if operation == 1:
        result = num_1 + num_2
        print(f"{num_1} + {num_2} = {result}\n")

    # Subtraction
    elif operation == 2:
        result = num_1 - num_2
        print(f"{num_1} - {num_2} = {result}\n")

    # Multiplication
    elif operation == 3:
        result = num_1 * num_2
        print(f"{num_1} X {num_2} = {result}\n")

    # Division
    elif operation == 4:
        # Division by Zero Error
        if num_2 == 0:
            print("ERROR DIVISION BY ZERO!!!\n")
            continue
        result = num_1 / num_2
        print(f"{num_1} / {num_2} = {result}\n")

    # Invalid Input
    else:
        print("Enter a Valid Option!!!\n")