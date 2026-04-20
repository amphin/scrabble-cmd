import sys
from math import inf

import game_pieces as gp


with open("words.txt", "r") as f:
    words = set(word.strip() for word in f)


def get_tile_points(letters: list[str]) -> list[int]:
    tile_points = []
    for tile in letters:
        tile_points.append(gp.LETTER_POINTS[tile])

    return tile_points


def int_input_prompt(min_range: int = -inf, max_range: int = inf) -> int:
    while True:
        try:
            num = int(input("> "))
            if min_range <= num <= max_range:
                return num
            else:
                sys.stdout.write("\033[F\033[K")
                sys.stdout.flush()
        except:
            sys.stdout.write("\033[F\033[K")
            sys.stdout.flush()


def is_first_word() -> bool:
    start_row, start_col = gp.start_pos
    return gp.board[start_row][start_col] == gp.Tile.START


def can_place_word(word: str, position: int, row: list[str]) -> bool:
    # TODO: account for points tile
    all_empty_tiles = True
    for i, letter in enumerate(word):
        letter_pos = position + i
        if (letter_pos >= len(row)):
            return False

        row_letter = row[letter_pos]
        if row_letter != gp.Tile.EMPTY and not gp.Tile.is_points_tile(row_letter):
            all_empty_tiles = False
            if letter != row_letter and row_letter != gp.Tile.START:
                return False

    return not all_empty_tiles


def get_word_placements(word: str) -> tuple[list[tuple[int, int]]]:
    horizontal_placements = []
    vertical_placements = []

    for i, row in enumerate(gp.board):
        for j, _ in enumerate(row):
            if can_place_word(word, j, row):
                horizontal_placements.append((i, j))

            column = [r[j] for r in gp.board]
            if can_place_word(word, i, column):
                vertical_placements.append((i, j))

    return horizontal_placements, vertical_placements


def is_word_valid(word: str, letters: list[str]) -> bool:
    if len(word) == 1 and is_first_word():
        return "Word cannot be placed legally"

    letters_left = letters.copy()
    for letter in word.upper():
        if letter in letters_left:
            letters_left.remove(letter)
        else:
            if gp.Letter.WILD_LETTER in letters_left:
                letters_left.remove(gp.Letter.WILD_LETTER)
            else:
                return "Word must only use letters in hand"

    if word.upper() not in words:
        return "Not a real word"

    return ""
