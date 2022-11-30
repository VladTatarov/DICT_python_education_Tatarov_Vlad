from colorama import init, Fore
import sys

init(autoreset=True)


class CoffeeMachine:
    def __init__(self):
        """Basic resources of the coffee machine,ingredients for each type of coffee and the process of making coffee"""
        self.making_coffee = (Fore.BLUE + "Starting to make a coffee☕""\nGrinding coffee beans☕""\nBoiling water☕"
                                          "\nMixing boiled water with crushed coffee beans☕"
                                          "\nPouring coffee into the cup☕""\nPouring some milk into the cup☕"
                                          "\nCoffee is ready!☕")
        self.standard_equipment = {"water": 400, "milk": 540, "coffee_beans": 120,
                                   "disposable_cups": 9, "money": 550}

        self.coffee_menu = {
            '1': {
                "name": "espresso",
                "water": 250,
                "milk": 0,
                "coffee_beans": 16,
                "cost": 4
            },
            '2': {
                "name": "latte",
                "water": 350,
                "milk": 75,
                "coffee_beans": 20,
                "cost": 7
            },
            '3': {
                "name": "cappuccino",
                "water": 200,
                "milk": 100,
                "coffee_beans": 12,
                "cost": 6
            },
        }

    def take_action(self):
        """Function to collect money in the coffee machine"""
        print(Fore.BLUE + f"I gave you {self.standard_equipment['money']}💲")
        self.standard_equipment['money'] = 0

    def remaining_action(self):
        """Function to display the remaining ingredients in the coffee machine"""
        print(Fore.BLUE + "The coffee machine has:")
        print(Fore.BLUE + f"Water: {self.standard_equipment['water']}ml")
        print(Fore.BLUE + f"Milk: {self.standard_equipment['milk']}ml")
        print(Fore.BLUE + f"Coffee: {self.standard_equipment['coffee_beans']}g")
        print(Fore.BLUE + f"Disposable Cups: {self.standard_equipment['disposable_cups']} pieces")
        print(Fore.BLUE + f"Money: {self.standard_equipment['money']}$")

    def buy_action(self, how_many_cups, order_id):
        """Function to buy a specific coffee with a certain number of cups and check the availability of ingredients"""
        if 0 < how_many_cups < 100:
            print(Fore.BLUE + f"For {how_many_cups} cups of coffee you will need:")
            print(Fore.BLUE + f"{how_many_cups * self.coffee_menu[order_id]['water']}, ml of water")
            print(Fore.BLUE + f"{how_many_cups * self.coffee_menu[order_id]['milk']}, ml of milk")
            print(Fore.BLUE + f"{how_many_cups * self.coffee_menu[order_id]['coffee_beans']}, g of coffee beans")
        else:
            return Fore.RED + "Error!"
        if self.standard_equipment['water'] < how_many_cups * self.coffee_menu[order_id]['water']:
            return Fore.RED + f'Sorry, not enough {"water"}!💧'
        elif self.standard_equipment['milk'] < how_many_cups * self.coffee_menu[order_id]['milk']:
            return Fore.RED + f'Sorry, not enough {"milk"}!🥛'
        elif self.standard_equipment['coffee_beans'] < how_many_cups * self.coffee_menu[order_id]['coffee_beans']:
            return Fore.RED + f'Sorry, not enough {"coffee_beans"}!☕'
        elif self.standard_equipment['disposable_cups'] == 0:
            return Fore.RED + f'Sorry, not enough {"disposable_cups"}!🥤'

        self.standard_equipment['water'] -= how_many_cups * self.coffee_menu[order_id]['water']
        self.standard_equipment['milk'] -= how_many_cups * self.coffee_menu[order_id]['milk']
        self.standard_equipment['coffee_beans'] -= how_many_cups * self.coffee_menu[order_id]['coffee_beans']
        self.standard_equipment['disposable_cups'] -= how_many_cups
        self.standard_equipment['money'] += how_many_cups * self.coffee_menu[order_id]['cost']

        return Fore.YELLOW + "I have enough resources, making you a coffee" + "\n\n" + self.making_coffee

    def fill_action(self):
        """Function for filling the coffee machine with different ingredients"""
        self.standard_equipment['water'] += int(input(Fore.BLUE + "Write how many ml "
                                                                  "of water do you want to add\n->"))
        self.standard_equipment['milk'] += int(input(Fore.BLUE + "Write how many ml of milk do you want to add\n->"))
        self.standard_equipment['coffee_beans'] += int(input(Fore.BLUE + "Write how many grams of coffee "
                                                                         "beans do you want to add\n->"))
        self.standard_equipment['disposable_cups'] += int(input(Fore.BLUE + "Write how many disposable cups of "
                                                                            "coffee do you want to add\n->"))

    def process(self, _user_input):
        """Function for operating the coffee machine"""
        if user_input == "buy":
            order = input(Fore.YELLOW + "What do you want to buy? 1 - espresso, 2 - latte,"
                                        " 3 - cappuccino, back - to main menu\n->")
            if order == 'back':
                return True
            how_many_cups = int(input(Fore.YELLOW + "Write how many cups of coffee you will need \n"))

            if order == 'back':
                return True
            print(self.buy_action(how_many_cups, order))
        elif user_input == "remaining":
            self.remaining_action()
        elif user_input == "exit":
            sys.exit("Goodbye!")
        elif user_input == "fill":
            self.fill_action()
        elif user_input == "take":
            self.take_action()
        else:
            print(Fore.RED + "Wrong selection, try again")
        return True


machine = CoffeeMachine()
run = True
while run:
    user_input = input(Fore.GREEN + "####|CoffeeMachine|####""\n[BUY]""\n[FILL]""\n[TAKE]""\n[REMAINING]""\n[EXIT]\n->")
    run = machine.process(user_input)
