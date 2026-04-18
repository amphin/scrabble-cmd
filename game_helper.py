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


def is_row_full(row: list[str]) -> bool:
    return any(not tile.isalpha() for tile in gp.board[row])


def is_tile_free(row: list[str], col: list[str]) -> bool:
    return not gp.board[row][col].isalpha()


def is_first_word() -> bool:
    return gp.board[len(gp.board) // 2][len(gp.board[0]) // 2] == gp.Tile.START


def get_word_placements(word, row, column, direction, first_word=False):
    pass


def is_word_valid(word: str, letters: list[str]) -> bool:
    if len(word) == 1 and is_first_word():
        return "Word cannot be placed legally"

    letters_left = letters.copy()
    for letter in word.upper():
        if letter in letters_left:
            letters_left.remove(letter)
        else:
            if gp.Letter.WILD_TILE in letters_left:
                letters_left.remove(gp.WILD_TILE)
            else:
                return "Word must only use letters in hand"

    if word.upper() not in words:
        return "Not a real word"

    return ""
