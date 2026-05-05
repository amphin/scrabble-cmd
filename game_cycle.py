from game_prompts import *
from game_helper import *
import game_pieces as gp
import display
import random

# menu 1 -> place -> next turn
# menu 2 -> exchange loop -> next turn
# menu 3 -> shuffle -> menu
# menu 4 -> next turn


def player_menu() -> str:
    menu_display = ("""\n1. Place word
2. Exchange letters
3. Shuffle letters (no turn spent)
4. Pass turn\n""")
    choices = ["1", "2", "3", "4"]

    return choice_prompt(menu_display, choices)


# TODO: separate shuffle from display logic
def shuffle_letters(player_tiles: list[str]) -> None:
    random.shuffle(player_tiles)
    clear_lines(9)

    tile_points = []
    for tile in player_tiles:
        tile_points.append(gp.LETTER_POINTS[tile])
    display.print_player_tiles(
        player_tiles, get_tile_points(player_tiles))

    return player_tiles


def menu_handler(player_tiles: list[str], bag: list[str]) -> None:
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
                word = word_prompt(player_tiles)
                horizontal_placements, vertical_placements = get_word_placements(
                    word.upper())

                # TODO: word is invalid message, then show word prompt again (while loop in this if block)
                if len(horizontal_placements) == 0 and len(vertical_placements) == 0:
                    clear_lines(1)
                else:
                    word_placeable = False

            # TODO: position selection

            # if user enters . they exit to main menu i.e. continue loop with turn_spent = False

        elif choice == "2":
            letters_to_exchange = exchange_letters_prompt(player_tiles)

            for letter in letters_to_exchange:
                player_tiles.remove(letter)

            for i in range(len(letters_to_exchange)):
                # TODO: handle case if len(bag) > len(letters_to_exchange)
                exchanged_tile = random.choice(bag)
                player_tiles.append(exchanged_tile)
                bag.remove(exchanged_tile)

            bag.extend(letters_to_exchange)

            print()
            print("              ------- NEW TILES -------")
            display.print_player_tiles(
                player_tiles, get_tile_points(player_tiles))

            turn_spent = True
        elif choice == "3":
            shuffle_letters(player_tiles)
        elif choice == "4":
            turn_spent = True

    return player_tiles, bag
