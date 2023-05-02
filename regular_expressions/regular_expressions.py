"""Regular Expressions Program"""

# Libraries
import re


class RegularExpressions:
    def __init__(self):
        """Initialize variables"""
        self.user_input = None

    def menu(self):
        """Menu for the program"""
        while True:
            print("Regular Expressions.\n"
                  "Rule: The string must contain \"|\".\n[1]Start program\n[2]Exit")
            self.user_input = input("Enter your choice: ")
            if self.user_input == "1":
                self.get_user_input()
            elif self.user_input == "2":
                exit()
            else:
                print("You must input 1 or 2")

    @staticmethod
    def check_match(user_input):
        """Check match string and pattern and return True or False"""
        pattern = user_input.split("|")[0]
        match_string = user_input.split("|")[1]
        if not pattern:
            return False
        if pattern[0] == "^" and pattern[-1] == "$":
            return bool(re.match(pattern, match_string))
        return bool(re.search(pattern, match_string))

    def get_user_input(self):
        """Get user input and check match"""
        while True:
            self.user_input = input("Enter a string (or 'exit' for stop the program): ")
            if self.user_input == "exit":
                exit()
            while not self.user_input.count("|") == 1:
                print("You must input string with \"|\"")
                break
            else:
                print(self.check_match(self.user_input))


# Main
if __name__ == "__main__":
    reg = RegularExpressions()
    reg.menu()
