import time
from random import choice
from colorama import init, Fore
import os
import sys

init(autoreset=True)


def entering_names(users_num, users_name):
    if users_num <= 0:
        print(Fore.RED + "No one is joining for the party!")
        while 1:
            os.system("python dinnerparty.py")
            exit()
    print(Fore.BLUE + "Enter the name of every friend (including you), each on a new line:")
    for i in range(users_num):
        users_name.append(str(input()))
    print(Fore.BLUE + "Friends:")
    for i in range(len(users_name)):
        print(users_name[i])


def luck_process(user_choice, users_name, amount, users_num, money):
    while user_choice != "Exit":
        if user_choice == "YES":
            happy = choice(users_name)
            print(happy + " is the lucky one! ")
            new_price = amount / (users_num - 1)
            money = dict.fromkeys(users_name, new_price)
            money[happy] = 0
            print(money)
            print(Fore.RED + "Thank you for using our program!")
            time.sleep(5)
            sys.exit("Goodbye!")
            pass
        elif user_choice == "NO":
            print(Fore.RED + "No one is going to be lucky :(")
            print(Fore.RED + "Thank you for using our program!")
            print(money)
            time.sleep(5)
            sys.exit("Goodbye!")
            pass
        else:
            print(Fore.RED + "Invalid Choice!")

        luck_choice()
        user_choice = input(Fore.GREEN + "Enter your choice:")


def luck_choice():
    print(Fore.GREEN + "Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
    print(Fore.GREEN + "[YES]")
    print(Fore.GREEN + "[NO]")


def counting_process():
    users_name = []
    print(Fore.BLUE + "Enter the number of friends joining (including you):")
    users_num = int(input(">"))
    entering_names(users_num, users_name)
    money = dict.fromkeys(users_name, 0)
    print(money)
    print("Enter the total amount:")
    amount = float(input(">"))
    price = amount / users_num
    money = dict.fromkeys(users_name, price)
    print(money)
    luck_choice()
    user_choice = input(Fore.GREEN + "Enter your choice:")
    luck_process(user_choice, users_name, amount, users_num, money)


def menu():
    print(Fore.GREEN + "SHARING OF COMMON COSTS")
    print(Fore.GREEN + "[1] ENTER PARTICIPANTS!")
    print(Fore.GREEN + "[2] EXIT")


menu()
player_choice = int(input(Fore.GREEN + "Enter your choice:"))
while player_choice != 0:
    if player_choice == 1:
        counting_process()
        pass
    elif player_choice == 2:
        sys.exit("Goodbye!")
        pass
    else:
        print(Fore.RED + "Invalid Choice!")

    menu()
    player_choice = int(input(Fore.GREEN + "Enter your choice:"))
