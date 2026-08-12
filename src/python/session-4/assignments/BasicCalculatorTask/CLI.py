'''
this file responce for Calculation Display  
'''


def display_menu():
    print("Welcome to the Simple Calculator!")
    print("Select an Operation:")
    print("1. Addition (+)\n"
          "2. Subtraction (-)\n"
          "3. Multiplication (*)\n"
          "4. Division (/)")


def get_user_choice():
    while True:
        user_input = input(
            "Enter your Choice (1/2/3/4) or 'exit' to quit: "
        )

        if user_input.lower() == 'exit':
            return 'exit'

        elif user_input not in ['1', '2', '3', '4']:
            print("Invalid Choice")
            continue

        return user_input


def get_numbers():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2

        except ValueError:
            print("Invalid input. Please enter numbers only.")


def display_result(num1, num2, operation, result):
    if operation == '1':
        print(f"{num1} + {num2} = {result}")

    elif operation == '2':
        print(f"{num1} - {num2} = {result}")

    elif operation == '3':
        print(f"{num1} * {num2} = {result}")

    elif operation == '4':
        if result is None:
            print("Can't Divide by Zero")
        else:
            print(f"{num1} / {num2} = {result}")


def ask_to_continue():
    while True:
        answer = input(
            "Do you want to perform another calculation? (yes/no): "
        ).lower()

        if answer in ['yes', 'no']:
            return answer

        print("Invalid choice. Please enter yes or no.")