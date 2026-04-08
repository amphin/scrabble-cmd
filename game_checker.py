import game_pieces as gp

with open("words.txt", "r") as f:
    words = set(word.strip() for word in f)


def is_row_full(row):
    return any(not tile.isalpha() for tile in gp.board[row])


def is_tile_free(row, col):
    return not gp.board[row][col].isalpha()


def is_word_valid(word, letters, game_turn):
    # if len(word) == 1 and game_turn > 1:
    #     return "Word cannot be placed legally"

    # if word.upper() not in words:
    #     return "Not a real word"

    letters_left = letters.copy()
    for letter in word.upper():
        if letter in letters_left:
            letters_left.remove(letter)
        else:
            if '$' in letters_left:
                letters_left.remove('$')
            else:
                return "Word must only use letters in hand"

    return ""
