import sys


def add(num1, num2):
    result1 = num1 + num2
    print(f"The result is: {result1}")


def subtract(num3, num4):
    result2 = num3 - num4
    print(f"The result is: {result2}")


def divide(num5, num6):
    result3 = num5 / num6
    print(f"The result is: {result3}")


def multiply(num7, num8):
    result4 = num7 * num8
    print(f"The result is: {result4}")


while True:
    print("1. If you want to add two numbers")
    print("2. If you want to subtract two numbers")
    print("3. If you want to divide two numbers")
    print("4 .If you want to multiply two numbers")
    print("5. If you want to end the program, please type 'quit'")
    choice = input("Enter choice (1, 2, 3, 4): ")

    if choice in '1234':
        num = float(input("Please enter a number: "))
        num2 = float(input("Please enter another number: "))

        if choice == '1':
            add(num, num2)
        elif choice == '2':
            subtract(num, num2)
        elif choice == '3':
            divide(num, num2)
        elif choice == '4':
            multiply(num, num2)

    elif choice == "quit":
        sys.exit("Quit")
