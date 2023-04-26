"""Currency exchange program."""

# Libraries
import requests
import re
import json
import sys


class MoneyExchange:
    def __init__(self):
        """Initialize the class."""
        self.from_currency = None
        self.to_currency = None
        self.amount = None

    def menu(self):
        """Menu for the program."""
        while True:
            print("1. Convert")
            print("2. Available currencies")
            print("3. Exit")
            try:
                choice = input("Enter your choice: ")
            except ValueError:
                print("Invalid choice")
                continue
            if choice == "1":
                self.convert()
            elif choice == "2":
                self.currencies()
            elif choice == "3":
                sys.exit("Goodbye!")
            else:
                print("Invalid choice")

    @staticmethod
    def currencies():
        """Prints available currencies."""
        response = requests.get("https://www.floatrates.com/daily/usd.json")
        json_data = response.json().values()
        print("Available currencies:")
        for currency in json_data:
            print("{:<15} => {}".format(currency["name"], currency["code"]))

    def convert(self):
        """Converts currency and prints the result. If the currency is not available, prints a message."""
        while True:
            self.from_currency = input("Enter the currency you want to convert (or 'exit' to quit): ")
            if not self.from_currency:
                print("Invalid input for currency")
                continue
            if self.from_currency == "exit":
                self.menu()
                break
            if not re.match("^[A-Za-z]+$", self.from_currency):
                print("Invalid input for currency")
                continue

            self.to_currency = input("Enter the currency you want to convert to (or 'exit' to quit): ").lower()
            if not self.to_currency:
                print("Invalid input for currency")
                continue
            if self.to_currency == "exit":
                self.menu()
                break
            if not re.match("^[A-Za-z]+$", self.to_currency):
                print("Invalid input for currency")
                continue

            self.amount = input("Enter amount (or 'exit' to quit): ")
            if self.amount == "exit":
                self.menu()
                break
            try:
                self.amount = float(self.amount)
            except ValueError:
                print("Invalid input for amount")
                continue
            try:
                response = requests.get(f"https://www.floatrates.com/daily/{self.from_currency}.json")
                data = response.json()
            except json.JSONDecodeError:
                print("Invalid input for currency")
                continue

            if self.to_currency in data:
                exchange_rate = data[self.to_currency]["rate"]
                result = self.amount * exchange_rate

                print(f"{self.amount} {self.from_currency} = {round(result, 2)} {self.to_currency}")
            else:
                print(f"API does not contain currency information {self.to_currency}")
                continue


# Main
if __name__ == "__main__":
    money_exchange = MoneyExchange()
    money_exchange.menu()
