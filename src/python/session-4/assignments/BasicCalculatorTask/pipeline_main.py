from CLI import (
    display_menu,
    get_user_choice,
    get_numbers,
    display_result,
    ask_to_continue
)

from logic import (
    add,
    subtract,
    multiply,
    divide
)


def main():
    display_menu()

    while True:
        operation = get_user_choice()

        if operation == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        num1, num2 = get_numbers()

        if operation == '1':
            result = add(num1, num2)

        elif operation == '2':
            result = subtract(num1, num2)

        elif operation == '3':
            result = multiply(num1, num2)

        elif operation == '4':
            result = divide(num1, num2)

        display_result(num1, num2, operation, result)

        answer = ask_to_continue()

        if answer == 'no':
            print("Exiting the calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()