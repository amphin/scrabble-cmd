from game_helper import is_first_word, get_word_placements, can_place_word


def test_is_first_word_true(monkeypatch):
    assert is_first_word() is True


def test_is_first_word_false(monkeypatch):
    import game_pieces

    new_board = [row[:] for row in game_pieces.board]
    new_board[7][7] = 'A'
    monkeypatch.setattr(game_pieces, "board", new_board)

    assert is_first_word() is False


def test_can_place_word_start_tile():
    row = [' ', ' ', ' ', ' ', ' ', ' ', '*']
    assert can_place_word('TESTING', 0, row) is True


def test_can_place_word_matching_midway():
    row = [' ', ' ', ' ', 'T', ' ', ' ', ' ']
    assert can_place_word('TESTING', 0, row) is True


def test_can_place_word_matching_start():
    row = ['T', 'E', 'S', 'T', ' ', ' ', ' ']
    assert can_place_word('TESTING', 0, row) is True


def test_can_place_word_part_match():
    row = [' ', ' ', 'S', ' ', 'B', ' ', ' ']
    assert can_place_word('TESTING', 0, row) is False


def test_can_place_word_empty():
    row = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    assert can_place_word('TESTING', 0, row) is False


def test_can_place_word_too_long():
    row = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
    assert can_place_word('TESTING', 4, row) is False


def test_can_place_word_real_board():
    row = ['@', ' ', ' ', '2', ' ', ' ', ' ',
           '*', ' ', ' ', ' ', '2', ' ', ' ', '£']
    assert can_place_word('TESTING', 0, row) is False


def test_tile_is_points_tile():
    import game_pieces
    assert game_pieces.Tile.is_points_tile('F') is False


def test_get_word_placements_empty_board():
    expected_horizontal = [(7, 1), (7, 2), (7, 3),
                           (7, 4), (7, 5), (7, 6), (7, 7)]
    expected_vertical = [(1, 7), (2, 7), (3, 7),
                         (4, 7), (5, 7), (6, 7), (7, 7)]

    horizontal, vertical = get_word_placements('TESTING')
    assert horizontal == expected_horizontal
    assert vertical == expected_vertical
