import sys
from colorama import init, Fore

init(autoreset=True)
board_list = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

game_win = True
game_draw = -1
game_run = False
our_game = game_run


def board_one():
    print("\n")
    print(Fore.BLUE + "\t      |      |")
    print(Fore.BLUE + "\t   {}  |  {}   |  {}".format(board_list[1], board_list[2], board_list[3]))
    print(Fore.BLUE + '\t______|______|______')
    print(Fore.BLUE + "\t      |      |")

    print(Fore.BLUE + "\t   {}  |  {}   |  {}".format(board_list[4], board_list[5], board_list[6]))
    print(Fore.BLUE + '\t______|______|______')
    print(Fore.BLUE + "\t      |      |")

    print(Fore.BLUE + "\t   {}  |  {}   |  {}".format(board_list[7], board_list[8], board_list[9]))
    print(Fore.BLUE + "\t      |      |")
    print("\n")


def player_position(x):
    if board_list[x] == ' ':
        return True
    else:
        print(Fore.RED + "\nThis cell is already taken!")
        return False


def win_or_not():
    global our_game
    if board_list[1] == board_list[2] and board_list[2] == board_list[3] and board_list[1] != ' ':
        our_game = game_win
    elif board_list[4] == board_list[5] and board_list[5] == board_list[6] and board_list[4] != ' ':
        our_game = game_win
    elif board_list[7] == board_list[8] and board_list[8] == board_list[9] and board_list[7] != ' ':
        our_game = game_win
    elif board_list[1] == board_list[4] and board_list[4] == board_list[7] and board_list[1] != ' ':
        our_game = game_win
    elif board_list[2] == board_list[5] and board_list[5] == board_list[8] and board_list[2] != ' ':
        our_game = game_win
    elif board_list[3] == board_list[6] and board_list[6] == board_list[9] and board_list[3] != ' ':
        our_game = game_win
    elif board_list[1] == board_list[5] and board_list[5] == board_list[9] and board_list[5] != ' ':
        our_game = game_win
    elif board_list[3] == board_list[5] and board_list[5] == board_list[7] and board_list[5] != ' ':
        our_game = game_win
    elif (board_list[1] != ' ' and board_list[2] != ' ' and board_list[3] != ' ' and board_list[4] != ' '
          and board_list[5] != ' ' and board_list[6] != ' ' and board_list[7] != ' ' and
          board_list[8] != ' ' and board_list[9] != ' '):
        our_game = game_draw
    else:
        our_game = game_run


def game_procces():
    player = 1
    while our_game == game_run:
        board_one()
        if player % 2 != 0:
            print(Fore.GREEN + "Player 1's chance")
            Mark = 'X'
        else:
            print(Fore.GREEN + "Player 2's chance")
            Mark = '0'
        choice = int(input(Fore.BLUE + "Enter the position between [1-9] where you want to mark:"))
        if choice > 9:
            print(Fore.RED + "Invalid input")
            break
        elif choice < 1:
            print(Fore.RED + "Invalid input")
            break
        if player_position(choice):
            board_list[choice] = Mark
            player += 1
            win_or_not()
    board_one()
    if our_game == game_draw:
        print(Fore.RED + "Game Draw")
    elif our_game == game_win:
        player -= 1
        if player % 2 != 0:
            print(Fore.RED + "Player 1 Won")
        else:
            print(Fore.RED + "Player 2 Won")


def menu():
    print(Fore.GREEN + "#################")
    print(Fore.GREEN + "  TIC TAC TOE  ")
    print(Fore.GREEN + "[1] START GAME!")
    print(Fore.GREEN + "[2] EXIT")
    print(Fore.GREEN + "#################")


menu()
user_choice = int(input(Fore.GREEN + "Enter your choice:"))
while user_choice != 0:
    if user_choice == 1:
        game_procces()
        pass
    elif user_choice == 2:
        sys.exit("Goodbye!")
        pass
    else:
        print(Fore.RED + "Invalid Choice!")

    menu()
    user_choice = int(input(Fore.GREEN + "Enter your choice"))
