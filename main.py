import random

import display
import game_pieces as gp
from game_cycle import *
from game_helper import *
from game_prompts import *


display.print_title()

print("Enter number of players:")
num_players = int_input_prompt(2, 4)

player_names = []
for i in range(num_players):
    player_name = input(f"Enter name of Player {i+1}: ")
    player_names.append(player_name)

# print rules

bag = []
for i in range(len(gp.LETTER_TILES)):
    bag += [gp.LETTER_TILES[i]] * gp.LETTERS_IN_BAG[i]

players_tiles = [[] for _ in range(num_players)]
initial_num_tiles = len(bag)
max_tiles_per_player = 7
scores = [0 for _ in range(num_players)]
turn = 0
round = 1
occupied_tiles = []

for i in range(max_tiles_per_player):
    for j in range(len(players_tiles)):
        player_tile = random.choice(bag)
        bag.remove(player_tile)
        players_tiles[j].append(player_tile)

# main game loop
while len(bag) > 0:
    print()
    display.print_game_turn_start(round)
    display.print_player_turn_start(player_names[turn])
    display.print_board(gp.board)
    print()

    display.print_player_tiles(
        players_tiles[turn], get_tile_points(players_tiles[turn]))

    players_tiles[turn], bag = menu_handler(players_tiles[turn], bag)

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
