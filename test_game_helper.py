from game_helper import is_first_word


def test_is_first_word(monkeypatch):
    import game_pieces

    assert is_first_word() is True

    new_board = [row[:] for row in game_pieces.board]
    new_board[7][7] = 'A'
    monkeypatch.setattr(game_pieces, "board", new_board)
    assert is_first_word() is False
