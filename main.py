import sys
import random
from prompt_toolkit import prompt

import display
import game_pieces as gp


with open("words.txt", "r") as f:
    words = set(word.strip() for word in f)

# menu 1 -> place -> next turn
# menu 2 -> exchange loop -> next turn
# menu 3 -> shuffle -> menu
# menu 4 -> next turn


def player_menu():
    print("""\n1. Place word
2. Exchange letters
3. Shuffle letters (no turn spent)
4. Pass turn\n""")
    while True:
        choice = input("> ")
        if choice == "1" or choice == "2" or choice == "3" or choice == "4":
            return choice
        else:
            sys.stdout.write("\033[F\033[K")


def exchange_letters_prompt(letters):
    print()
    print("Enter letter to exchange (and . to confirm selection)")
    letters_selected = ""
    while True:
        print(letters_selected)
        letter = input("> ")
        if letter.upper() in letters:
            letters_selected += letter.upper() + " "
            letters.remove(letter.upper())
        elif letter == ".":
            return letters_selected.split(" ")[:-1]

        sys.stdout.write("\033[F\033[K")
        sys.stdout.write("\033[F\033[K")


def is_word_valid(word, letters, game_turn):
    if len(word) == 1 and game_turn > 1:
        return "Word cannot be placed legally"

    if word.upper() not in words:
        return "Not a real word"

    letters_left = letters.copy()
    for letter in word.upper():
        if letter in letters_left:
            letters_left.remove(letter)
        else:
            return "Word must only use letters in hand"

    return ""


def place_word():
    pass


display.print_title()

player1_name = input("Enter name of Player 1: ")
player2_name = input("Enter name of Player 2: ")
player_names = [player1_name, player2_name]
num_players = 2  # TODO: dynamic between 2-4 players

# print rules

bag = []
for i in range(len(gp.letter_tiles)):
    bag += [gp.letter_tiles[i]] * gp.letters_in_bag[i]

players_tiles = [[], []]
scores = [0, 0]
turn = 0
game_turn = 0

for i in range(7):
    for player_tiles in players_tiles:
        player_tile = random.choice(bag)
        bag.remove(player_tile)
        player_tiles.append(player_tile)

# game loop
while len(bag) > 0:
    game_turn += 1
    display.print_player_turn_start(player_names[turn])
    display.print_board(gp.board)
    print()

    tile_points = []
    for tile in players_tiles[turn]:
        tile_points.append(gp.letter_points[tile])
    display.print_player_tiles(players_tiles[turn], tile_points)

    choice = "3"
    while choice == "3":
        choice = player_menu()
        if choice == "3":
            random.shuffle(players_tiles[turn])
            for i in range(9):
                sys.stdout.write("\033[F\033[K")
            sys.stdout.flush()

            tile_points = []
            for tile in players_tiles[turn]:
                tile_points.append(gp.letter_points[tile])
            display.print_player_tiles(players_tiles[turn], tile_points)

    if choice == "2":
        letters_to_exchange = exchange_letters_prompt(players_tiles[turn])

        for i in range(len(letters_to_exchange)):
            exchanged_tile = random.choice(bag)
            players_tiles[turn].append(exchanged_tile)
            bag.remove(exchanged_tile)

        bag += letters_to_exchange

    elif choice == "1":
        for i in range(6):
            sys.stdout.write("\033[F\033[K")
        sys.stdout.flush()

        print("Enter word to place:")
        print()
        word = input("> ")
        word_valid = is_word_valid(word, players_tiles[turn], game_turn)
        while word_valid != "":
            sys.stdout.write("\033[F\033[K")
            sys.stdout.write("\033[F\033[K")
            sys.stdout.flush()
            print(word_valid)
            word = input("> ")
            word_valid = is_word_valid(word, players_tiles[turn], game_turn)

    # prompt to begin next player turn
    # turn = (turn + 1) % num_players
