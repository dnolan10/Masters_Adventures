# DSC 510
# Week 5
# Programming Assignment 5.1
# Author Doug Nolan
# 10/12/2025

def perform_calculation(args):
    """
    :param args: performs a calculation (+ - * / ) on two user provided numbers
    :return: calculated result
    """
    try:
        a = float(input("Please input the first number"))
        b = float(input("Please input the second number"))
        result = 0
        # if statements to handle all 4 operators
        if args == '+':
            result = a + b
        elif args == '-':
            result = a - b
        elif args == '*':
            result = a * b
        elif args == '/':
            if b == 0:
                print("Error: Divison by zero is not allowed")
                return None
            result = a / b
        else:
            print("Invalid operation.")
            return None

        return result
    except ValueError:
        print("Error: Please enter valid numeric values.")
    return None


def calculate_average():
    """
    :return: Get input from user and loop through all inputted numbers to calculate the average
    """
    try:
        n = int(input("How many number do you wish to input?"))
        if n <= 0:
            print("Please enter a number greater than zero.")
            return None
        total = 0
        number = 0
        for i in range(n):
            while True:
                try:
                    number = float(input(f"Enter number {i + 1}: "))
                    total = number + total
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
        average = total / n
        return average
    except ValueError:
        print("Invalid input. Please enter an integer next time.")
        return None

def main():
    """
    :return: place other functions into main function and use name = main to run them
    Ask the user if they want to do a calculation or average or quit
    """
while True:
    print("Welcome to Doug's Dazzling Python calculator")
    print("Choose an option below:")
    print("1. Perform a calculation (+, -, *, /)")
    print("2. Calculate an average")
    print("3. Quit")

    choice = input("Enter your choice (1, 2, or 3): ").strip()

    if choice == '1':
        operator = input("Enter the operator (+, -, *, /): ").strip()
        calculation = perform_calculation(operator)
        print(f"The result of you calculation is: {calculation:,.2f}")
        break

    elif choice == '2':
        avg = calculate_average()
        if avg is not None:
            print(f"The average of the numbers entered is: {avg:.2f}")
            break

    elif choice == '3':
        print("Thank you for using the calculator. Goodbye")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
