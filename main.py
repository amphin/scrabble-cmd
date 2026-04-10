import sys
import random
from prompt_toolkit import prompt

import display
import game_pieces as gp
import game_checker as checker
import game_helper as helper


display.print_title()

player0_name = input("Enter name of Player 1: ")
player1_name = input("Enter name of Player 2: ")
player_names = [player0_name, player1_name]
num_players = 2  # TODO: choose between 2-4 players

# print rules

bag = []
for i in range(len(gp.letter_tiles)):
    bag += [gp.letter_tiles[i]] * gp.letters_in_bag[i]

players_tiles = [[], []]
initial_num_tiles = len(bag)
scores = [0, 0]
turn = 0
game_turn = 0

for i in range(7):
    for player_tiles in players_tiles:
        player_tile = random.choice(bag)
        bag.remove(player_tile)
        player_tiles.append(player_tile)

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
        if choice in ["1", "2", "3", "4"]:
            return choice
        else:
            sys.stdout.write("\033[F\033[K")


# TODO: don't modify players_tiles[turn]
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


# TODO: decouple from main code
def shuffle_letters():
    random.shuffle(players_tiles[turn])
    for i in range(9):
        sys.stdout.write("\033[F\033[K")
    sys.stdout.flush()

    tile_points = []
    for tile in players_tiles[turn]:
        tile_points.append(gp.letter_points[tile])
    display.print_player_tiles(
        players_tiles[turn], helper.get_tile_points(players_tiles[turn]))


def menu_handler():
    global bag

    choice == "3"
    while choice == "3":
        choice = player_menu()

        if choice == "1":
            pass

        elif choice == "2":
            letters_to_exchange = exchange_letters_prompt(players_tiles[turn])
            print(players_tiles[turn])

            for i in range(len(letters_to_exchange)):
                # TODO: handle case if len(bag) > len(letters_to_exchange)
                exchanged_tile = random.choice(bag)
                players_tiles[turn].append(exchanged_tile)
                bag.remove(exchanged_tile)

            bag += letters_to_exchange

            print()
            print("              ------- NEW TILES -------")
            display.print_player_tiles(
                players_tiles[turn], helper.get_tile_points(players_tiles[turn]))

        elif choice == "3":
            shuffle_letters()

    # elif choice == "10":
    #     for i in range(6):
    #         sys.stdout.write("\033[F\033[K")
    #     sys.stdout.flush()

    #     print("Enter word to place:")
    #     print()
    #     word = input("> ")
    #     word_valid = checker.is_word_valid(
    #         word, players_tiles[turn], game_turn)
    #     while word_valid != "":
    #         sys.stdout.write("\033[F\033[K")
    #         sys.stdout.write("\033[F\033[K")
    #         sys.stdout.flush()
    #         print(word_valid)
    #         word = input("> ")
    #         word_valid = checker.is_word_valid(
    #             word, players_tiles[turn], game_turn)


# game loop
while len(bag) > 0:
    game_turn += 1
    print()
    display.print_player_turn_start(player_names[turn])
    display.print_board(gp.board)
    print()

    display.print_player_tiles(
        players_tiles[turn], helper.get_tile_points(players_tiles[turn]))

    menu_handler()

    # print()
    # print("Enter row to place on (1-15):")
    # print()
    # row = enter_line() - 1
    # row_valid = is_line_valid(row)
    # while row_valid != "":
    #     sys.stdout.write("\033[F\033[K")
    #     sys.stdout.write("\033[F\033[K")
    #     sys.stdout.flush()
    #     print(row_valid)
    #     row = enter_line() - 1
    #     row_valid = is_line_valid(row)

    # print()
    # print("Enter column to place on (1-15):")
    # column = enter_line() - 1

    print()
    print("--------------------------------------------------------")
    print()
    for i in range(num_players):
        print(f"{player_names[i]}'s score: {scores[i]}")

    print()
    print(f"Letters left in bag: {len(bag)}/{initial_num_tiles}")
    print()

    finish_turn = input("Enter anything to finish turn: ")
    turn = (turn + 1) % num_players
