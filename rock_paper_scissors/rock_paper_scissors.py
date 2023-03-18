"""GAME 'ROCK PAPER SCISSORS'"""

# Libraries
import sys
import random
import os

# LISTS WITH SIGNS FOR DIFFERENT LEVELS OF THE GAME
signs_level_hard = ["rock", "paper", "scissors", "lizard", "spock", "snake", "human", "tree", "wolf", "sponge",
                    "air", "water", "dragon", "devil", "lightning", "gun", "fire", "death"]
signs_level_easy = ["rock", "paper", "scissors"]
# GAME MENU
menu_options = {
    1: 'START THE GAME',
    2: 'Exit',
}
# LEVEL SELECTION
game_level = {
    1: 'Easy Level',
    2: 'Hard Level',
    3: 'Back'
}


def print_game_level():
    """GAP FILLING WITH SYMBOLS"""
    for key in game_level.keys():
        print(key, '--', game_level[key])


def print_menu():
    """GAP FILLING WITH SYMBOLS"""
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def load_rating():
    """UPLOADING PLAYER DATA"""
    rating = {}
    if os.path.exists('rating.txt'):
        with open('rating.txt', 'r', encoding='ISO-8859-1') as file:
            for line in file:
                name, score = line.strip().split(',')
                rating[name] = int(score)
    return rating


def update_rating(name, score):
    """SAVING PLAYER DATA"""
    rating = load_rating()
    rating[name] = rating.get(name, 0) + score
    with open('rating.txt', 'w', encoding='ISO-8859-1') as file:
        for name, score in rating.items():
            file.write(f'{name},{score}\n')


def users_name():
    """ENTERING A PLAYER NAME"""
    user_name = input("Enter your name:")
    print(f"Welcome, {user_name}")
    return user_name


def game_level_hard():
    """A GAME OF ROCK-PAPER-SCISSORS WITH LOTS OF CHARACTERS"""
    user_name = users_name()
    while True:
        score_player_easy = load_rating().get(user_name, 0)
        options = input(f"{user_name}, Enter a comma separated list of options - rock, paper, scissors, lizard, spock,"
                        f" snake, human, tree, wolf, sponge, air, water, dragon, devil, lightning, gun, fire, death.\n"
                        "To end the game enter '!exit'\n"
                        "To see the number of points enter '!rating \n->")
        if options == "!rating":
            print(f"{user_name}, you have {score_player_easy} points")
        elif options == "!exit":
            sys.exit("Bye!")
        elif options != "!exit" or options != "!rating":
            options = options.split(",")
            signs = []
            for OPTION in options:
                if OPTION.strip() in signs_level_hard:
                    signs.append(OPTION.strip())
            if len(signs) == 0:
                print("Error: Could not find options in the list")
                continue
            elif len(signs) < 3:
                print("Error: number of characters must be at least 3")
                continue
            n = len(signs)
            winners = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if i == j:
                        winners[i][j] = 0
                    elif (j - i) % n <= n // 2:
                        winners[i][j] = 1
                    else:
                        winners[i][j] = -1
            while True:
                user_input = input("Enter your choice: ")
                if user_input == "!rating":
                    print(f"{user_name}, you have {score_player_easy} points")
                elif user_input == "!exit":
                    update_rating(user_name, score_player_easy)
                    sys.exit("Bye!")
                elif user_input not in signs:
                    print("Error: This option is not in the list")
                    continue
                else:
                    pc_signs = random.choice(signs)
                    i = signs.index(user_input)
                    j = signs.index(pc_signs)
                    result = winners[i][j]
                    if result == 1:
                        print(f"Win -> Well done. The computer chose {pc_signs} and failed!")
                        score_player_easy += 100
                    elif result == -1:
                        print(f"Lose -> Sorry, but the computer chose {pc_signs}")
                    else:
                        print(f"Draw -> There is a draw, pc and you choose {pc_signs}")
                        score_player_easy += 50


def game_level_easy():
    """STANDARD GAME OF ROCK-PAPER-SCISSORS"""
    user_name = users_name()
    score_player_easy = load_rating().get(user_name, 0)
    print(f"{user_name}, you must choose one of the signs - rock, paper, scissors.\n"
          "To end the game enter '!exit'\n"
          "To see the number of points enter '!rating'")
    while True:
        pc_signs = random.choice(signs_level_easy)
        user_input = input("->")
        if user_input == pc_signs:
            print(f"Draw -> There is a draw, pc and you choose {pc_signs}")
            score_player_easy += 50
        elif user_input == "rock":
            if pc_signs == "scissors":
                print(f"Win -> Well done. The computer chose {pc_signs} and failed!")
                score_player_easy += 100
            else:
                print(f"Lose -> Sorry, but the computer chose {pc_signs}")
        elif user_input == "paper":
            if pc_signs == "rock":
                print(f"Win -> Well done. The computer chose {pc_signs} and failed!")
                score_player_easy += 100
            else:
                print(f"Lose -> Sorry, but the computer chose {pc_signs}")
        elif user_input == "scissors":
            if pc_signs == "paper":
                print(f"Win -> Well done. The computer chose {pc_signs} and failed!")
                score_player_easy += 100
            else:
                print(f"Lose -> Sorry, but the computer chose {pc_signs}")
        elif user_input == "!rating":
            print(f"{user_name}, you have {score_player_easy} points")
        elif user_input == "!exit":
            update_rating(user_name, score_player_easy)
            sys.exit("Bye!")
        else:
            print("Invalid choice. Please enter rock, paper, or scissors")


# APP MENU
if __name__ == '__main__':
    while True:
        print("###################"
              "\nROCK PAPER SCISSORS\n"
              "###################")
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except ValueError:
            print('Wrong input. Please enter a number ...')
        if option == 1:
            print_game_level()
            level = ''
            try:
                level = int(input('Enter your choice: '))
            except ValueError:
                print('Wrong input. Please enter a number ...')
            if level == 1:
                game_level_easy()
            elif level == 2:
                game_level_hard()
            elif level == 3:
                print_menu()
            else:
                print('Invalid option. Please enter a number between 1 and 3.')
        elif option == 2:
            sys.exit("Bye!")
        else:
            print('Invalid option. Please enter a number between 1 and 2.')
