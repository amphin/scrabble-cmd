import sys
import random

import display
import game_pieces as gp
import game_helper as helper


display.print_title()

print("Enter number of players:")
num_players = helper.int_input_prompt(2, 4)

player_names = []
for i in range(num_players):
    player_name = input(f"Enter name of Player {i+1}: ")
    player_names.append(player_name)

# print rules

bag = []
for i in range(len(gp.LETTER_TILES)):
    bag += [gp.LETTER_TILES[i]] * gp.LETTERS_IN_BAG[i]

players_tiles = [[] for n in range(num_players)]
initial_num_tiles = len(bag)
max_tiles_per_player = 7
scores = [0 for n in range(num_players)]
turn = 0
round = 1
occupied_tiles = []

for i in range(max_tiles_per_player):
    for j in range(len(players_tiles)):
        player_tile = random.choice(bag)
        bag.remove(player_tile)
        players_tiles[j].append(player_tile)


# menu 1 -> place -> next turn
# menu 2 -> exchange loop -> next turn
# menu 3 -> shuffle -> menu
# menu 4 -> next turn


def player_menu() -> str:
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
def exchange_letters_prompt(letters: list[str]) -> list[str]:
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
def shuffle_letters() -> None:
    random.shuffle(players_tiles[turn])
    for i in range(9):
        sys.stdout.write("\033[F\033[K")
    sys.stdout.flush()

    tile_points = []
    for tile in players_tiles[turn]:
        tile_points.append(gp.LETTER_POINTS[tile])
    display.print_player_tiles(
        players_tiles[turn], helper.get_tile_points(players_tiles[turn]))


def word_prompt(letters: list[str]) -> str:
    print()
    print("Enter word:")
    print()
    player_word = input("> ")

    word_validity = helper.is_word_valid(player_word, letters)
    while word_validity != "":
        sys.stdout.write("\033[F\033[K")
        sys.stdout.write("\033[F\033[K")
        sys.stdout.flush()

        print(word_validity)
        player_word = input("> ")
        word_validity = helper.is_word_valid(player_word, letters)

    sys.stdout.write("\033[F\033[K")
    sys.stdout.write("\033[F\033[K")
    sys.stdout.write("\033[F\033[K")
    sys.stdout.flush()

    return player_word


def menu_handler() -> None:
    turn_spent = False

    while not turn_spent:
        choice = player_menu()

        if choice == "1":
            # TODO: below
            # input word
            # if word is legal, calculate all possible placements on board
            # if placements = 0, word is invalid
            # else, print placements as numbered list
            # once user picks placement, place word at that position

            word_placeable = True
            while word_placeable:
                word = word_prompt(players_tiles[turn])
                horizontal_placements, vertical_placements = helper.get_word_placements(
                    word.upper())

                # TODO: word is invalid message, then show word prompt again (while loop in this if block)
                if len(horizontal_placements) == 0 and len(vertical_placements) == 0:
                    sys.stdout.write("\033[F\033[K")
                else:
                    word_placeable = False

            # TODO: position selection

            # if user enters . they exit to main menu i.e. continue loop with turn_spent = False

        elif choice == "2":
            letters_to_exchange = exchange_letters_prompt(players_tiles[turn])
            print(players_tiles[turn])

            for i in range(len(letters_to_exchange)):
                # TODO: handle case if len(bag) > len(letters_to_exchange)
                exchanged_tile = random.choice(bag)
                players_tiles[turn].append(exchanged_tile)
                bag.remove(exchanged_tile)

            bag.extend(letters_to_exchange)

            print()
            print("              ------- NEW TILES -------")
            display.print_player_tiles(
                players_tiles[turn], helper.get_tile_points(players_tiles[turn]))

            turn_spent = True
        elif choice == "3":
            shuffle_letters()
        elif choice == "4":
            turn_spent = True


# game loop
while len(bag) > 0:
    print()
    display.print_game_turn_start(round)
    display.print_player_turn_start(player_names[turn])
    display.print_board(gp.board)
    print()

    display.print_player_tiles(
        players_tiles[turn], helper.get_tile_points(players_tiles[turn]))

    menu_handler()

    print()
    print("--------------------------------------------------------")
    print()
    for i in range(num_players):
        print(f"{player_names[i]}'s score: {scores[i]}")

    print()
    print(f"Letters left in bag: {len(bag)}/{initial_num_tiles}")
    print()

    finish_turn = input("Press Enter to finish turn: ")

    new_turn = (turn + 1) % num_players
    round += 1 if new_turn < turn else 0
    turn = new_turn
