from day10_calculator_art import logo
import os


def clear():
    os.system("cls")


def get_operation():
    print("+\n-\n*\n/")
    return input("Pick an operation: ")


def get_first_number():
    return float(input("What's the first number?: "))


def get_next_number():
    return float(input("What's the next number?: "))


def start_calculation():
    print(logo)
    calculating = True
    current_calc = get_first_number()

    while calculating:
        oper = get_operation()
        if oper not in "+-*/":
            print("Invalid operation!")
            continue

        next_num = get_next_number()
        if oper == "+":
            print(f"{current_calc} + {next_num} = {current_calc + next_num}")
            current_calc += next_num
        elif oper == "-":
            print(f"{current_calc} - {next_num} = {current_calc - next_num}")
            current_calc -= next_num
        elif oper == "*":
            print(f"{current_calc} * {next_num} = {current_calc * next_num}")
            current_calc *= next_num
        elif oper == "/":
            print(f"{current_calc} / {next_num} = {current_calc / next_num}")
            current_calc /= next_num

        calc_prompt = input(
            f"Type 'y' to continue calculating with {current_calc}, or type 'n' to start a new calculation: ").lower()

        if calc_prompt == "n":
            calculating = False
            clear()
            start_calculation()
        elif calc_prompt != "y":
            print("Invalid input! Exiting...")
            calculating = False


def main():
    start_calculation()


main()
