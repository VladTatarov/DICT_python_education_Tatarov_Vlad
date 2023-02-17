"""Arithmetic test program"""

# LIBRARIES
import random
from operator import add, sub, mul

# DICTIONARY FOR WORKING WITH THE PROGRAM MENU
menu_options = {
    1: 'simple operations with numbers 2-9',
    2: 'integral squares of 11-29',
    0: 'Exit',
}


def print_menu():
    """GAP FILLING WITH SYMBOLS"""
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def saving(name: str, result: int, lvl: str):
    """
            FUNCTION FOR SAVING THE ENTERED DATA OF THE USER IN A SEPARATE TXT FILE
            Parameters:
            -------
                name (str): String.
                result (int): Int
                lvl (str): String
            -------
            THIS FUNCTION DOES NOT RETURN ANYTHING
        """
    with open('results.txt', 'w', encoding='utf-8') as my_file:
        my_file.write(f"\n{name}: {result}/5 in level {lvl}")


def simple_operations():
    """A FUNCTION THAT GENERATES SIMPLE ARITHMETIC PROBLEMS AND STORES THE NUMBER
    OF CORRECT ANSWERS. RETURNS AND SAVE THE RESULT, LEVEL AND USERNAME AS WANTED"""
    lvl = "1"
    total = 1
    correct = 0
    while total <= 5:
        ops = {'+': add, '-': sub, '*': mul}
        op = random.choice(list(ops.keys()))
        x = random.randint(2, 9)
        y = random.randint(2, 9)
        print("Question:", total)
        print("What is {} {} {}? ".format(x, op, y))
        answer = ops[op](x, y)
        user_input = input("Type your answer: ")
        try:
            user_input = int(user_input)
        except ValueError:
            print("Enter only numbers")
            continue
        total = total + 1
        if user_input == answer:
            correct = correct + 1
            print("Right!")
        else:
            print("Wrong!")
    print(f"Your mark is {correct}/5. Would you like to save the result? Enter yes or no.")
    while True:
        user_input = str(input(">"))
        if user_input == "yes" or user_input == "YES" or user_input == "Y" or user_input == "y" or user_input == "Yes":
            users_name = input("Enter your name:")
            saving(users_name, correct, lvl)
            break
        elif user_input == "no" or user_input == "n" or user_input == "No" or user_input == "NO":
            exit()
        else:
            print("Try again")


def square_number():
    """FUNCTION WHICH GENERATES NUMBERS WITH A REQUEST TO RADIATE TO THE SECOND POWER AND STORES THE NUMBER
     OF CORRECT ANSWERS. RETURNS AND SAVE THE RESULT, LEVEL AND USERNAME AS WANTED"""
    lvl = "2"
    total = 1
    correct = 0
    while total <= 5:
        x = random.randint(11, 29)
        print("Question:", total)
        print(f"What is the square of the number {x}")
        user_input = input("Type your answer: ")
        try:
            user_input = int(user_input)
        except ValueError:
            print("Enter only numbers")
            continue
        total = total + 1
        if user_input == pow(x, 2):
            correct = correct + 1
            print("Right!")
        else:
            print("Wrong!")
    print(f"Your mark is {correct}/5. Would you like to save the result? Enter yes or no.")
    while True:
        user_input = str(input(">"))
        if user_input == "yes" or user_input == "YES" or user_input == "Y" or user_input == "y" or user_input == "Yes":
            users_name = input("Enter your name:")
            saving(users_name, correct, lvl)
            break
        elif user_input == "no" or user_input == "n" or user_input == "No" or user_input == "NO":
            exit()
        else:
            print("Try again")


# PROGRAM MENU
if __name__ == '__main__':
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Which level do you want? Enter a number:'))
        except ValueError:
            print('Wrong input. Please enter a number ...')
        if option == 1:
            simple_operations()
        elif option == 2:
            square_number()
        elif option == 0:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number 1-2 or 0.')
