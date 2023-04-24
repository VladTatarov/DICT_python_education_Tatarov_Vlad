"""Game Dominoes"""

# Libraries
import random
import sys
from itertools import combinations_with_replacement
from random import shuffle


class Dominos:
    """Initializing class attributes"""
    def __init__(self):
        # Stock of chips
        self.reserve_tiles: list = []
        # Computer chips
        self.computer_tiles: list = []
        # Player chips
        self.player_tiles: list = []
        # Snake
        self.snake = None
        # Game board
        self.board: list = []
        # Game status (Player/Computer)
        self.status = None

    def shuffle_tiles(self):
        """Shuffle tiles"""
        self.reserve_tiles = list(combinations_with_replacement(range(0, 7), 2))
        shuffle(self.reserve_tiles)

    def interface(self):
        """Game interface"""
        print("=============================================================")
        print(f"Stock pieces: {len(self.reserve_tiles)}")
        print(f"Computer pieces: {len(self.computer_tiles)}")
        print(*self.board, '\n', sep='') if len(self.board) <= 6 else \
            print(*self.board[:3], '...', *self.board[-3:], '\n', sep='')
        print('Your pieces:')
        for i, tile in enumerate(self.player_tiles):
            print(f"{i + 1}:[{tile[0]}, {tile[1]}]")
        print(f"Status:{self.status}")
        print("=============================================================")

    def make_a_move(self, m, pieces):
        """Define the player's move"""
        if m > 0:
            domino = pieces[m - 1]
            right_snake = int(self.board[-1][4])
            if domino.count(right_snake) > 0:
                if right_snake == domino[1]:
                    domino = [domino[1], domino[0]]
                self.board.append(str(domino))
                del pieces[m - 1]
            else:
                return 'Illegal'
        if m < 0:
            domino = pieces[-m - 1]
            left_snake = int(self.board[0][1])
            if left_snake in domino:
                if left_snake == domino[0]:
                    domino = [domino[1], domino[0]]
                self.board.insert(0, str(domino))
                del pieces[-m - 1]
            else:
                return 'Illegal'
        if m == 0:
            if self.reserve_tiles:
                pieces.append(self.reserve_tiles.pop(0))

    def insert_tile(self):
        """Insert tiles and define the first move"""
        for i in range(7):
            self.player_tiles.append(self.reserve_tiles.pop())
            self.computer_tiles.append(self.reserve_tiles.pop())
        if max(self.player_tiles) > max(self.computer_tiles):
            self.snake = max(self.player_tiles)
            self.player_tiles.remove(self.snake)
        elif max(self.player_tiles) < max(self.computer_tiles):
            self.snake = max(self.computer_tiles)
            self.computer_tiles.remove(self.snake)

    def game_menu(self):
        """Game menu"""
        print("Dominoes Game!")

        while True:
            print("1. Start game")
            print("2. Exit game")
            try:
                user_choice = int(input("Enter your choice: "))
            except ValueError:
                print('Invalid input. Please try again.')
                continue
            if user_choice == 1:
                self.game_process()
            elif user_choice == 2:
                sys.exit("Bye!")
            else:
                print('Invalid input. Please try again.')

    def game_process(self):
        """Game process"""
        self.shuffle_tiles()
        self.insert_tile()

        if len(self.player_tiles) > len(self.computer_tiles):
            self.status = 'Player'
        else:
            self.status = 'Computer'
        self.board.append(str(self.snake))
        while True:
            self.interface()
            if self.status == 'Player':
                while True:
                    try:
                        user_input = int(input("Enter your choice:"))
                    except ValueError:
                        print('Invalid input. Please try again.')
                        continue
                    if int(user_input) not in range(-len(self.player_tiles), len(self.player_tiles) + 1):
                        print('Invalid input. Please try again.')
                        continue
                    if self.make_a_move(int(user_input), self.player_tiles) == 'Illegal':
                        print('Illegal move. Please try again.')
                        continue
                    break
                self.status = 'Computer'
            elif self.status == 'Computer':
                while True:
                    user_input = random.randint(-len(self.computer_tiles), len(self.computer_tiles))
                    if self.make_a_move(user_input, self.computer_tiles) == 'Illegal':
                        continue
                    break
                self.status = 'Player'
            if self.board[0][1] == self.board[-1][4] and "".join(self.board).count(
                    self.board[0][1]) == 8:
                print("Draw!")
                self.game_menu()
            if len(self.player_tiles) == 0:
                print("You win!")
                self.game_menu()
            if len(self.computer_tiles) == 0:
                print("Computer wins!")
                self.game_menu()


# Main
if __name__ == '__main__':
    game = Dominos()
    game.game_menu()
