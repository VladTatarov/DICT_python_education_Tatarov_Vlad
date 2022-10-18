from random import choice
from colorama import init, Fore
import sys

init(autoreset=True)

HANGMAN = (
            """
        ------
        | |
        |
        |
        |
        |
        |
        ----------
        """,
            """
        ------
        | |
        | O
        |
        |
        |
        |
        ----------
        """,
            """
        ------
        | |
        | O
        | |
        |
        |
        |
        ----------
        """,
            """
        ------
        | |
        | O
        | /|
        |
        |
        |
        ----------
        """,
            """
        ------
        | |
        | O
        | /|\\
        |
        |
        |
        ----------
        """,
            """
        ------
        | |
        | O
        | /|\\
        | /
        |
        |
        ----------
        """,
            """
        ------
        | |
        | O
        | /|\\
        | / \\
        |
        |
        ----------
        """
        )
words = ('python', 'java', 'javascript', 'php')


def examination(guess):
    if guess == "Exit":
        sys.exit("Goodbye!")
    elif len(guess) > 1:
        print((Fore.RED + "\n You must enter one letter.Try again"))
    elif guess == guess.upper():
        print((Fore.RED + "\n Turn capslock off or don't use numbers!"))


def menu():
    print("[1] START A NEW GAME!")
    print("[2] EXIT")


def win_or_not(wrong, wrong_max, player_letter):
    if wrong == wrong_max:
        print("\nYou lost!")

    else:
        print("\nYou survived!")

    print("The hidden word was \"" + player_letter + "\" ")


def board():
    print("############################################")
    print("|-HANGMAN-|""\nThe game will be available soon.")
    print("############################################")


def board_2(wrong, used_letters, far):
    print(HANGMAN[wrong])
    print("\n You used this letter >\n", *used_letters)
    print("\n At the moment the word looks like this >\n", far)

    print("\n EXIT GAME - WRITE \"Exit\"")


def game():
    board()
    wrong_max = len(HANGMAN)
    player_letter = choice(words)
    far = '-' * len(player_letter)
    wrong = 0
    used_letters = set()

    while wrong < wrong_max and far != player_letter:
        board_2(wrong, used_letters, far)
        guess = input("\n Please enter above guess > ")
        if guess in used_letters:
            print("You already guessed that letter!", guess)
            continue
        examination(guess)

        used_letters.add(guess)

        if guess in player_letter:
            print("Great! \'" + guess + "\" is in the word")
            new = ''
            for x in range(len(player_letter)):
                if guess == player_letter[x]:
                    new += guess
                else:
                    new += far[x]
            far = new
        else:
            print("\n Sorry, no letter \"" + guess + "\" in the word")
            wrong += 1

    win_or_not(wrong, wrong_max, player_letter)


menu()
player_choice = int(input("Enter your choice:"))
while player_choice != 0:
    if player_choice == 1:
        game()
        pass
    elif player_choice == 2:
        sys.exit("Goodbye!")
        pass
    else:
        print("Invalid Choice!")
    print()
    menu()
    player_choice = int(input("Enter your choice:"))
