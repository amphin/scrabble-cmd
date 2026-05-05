import sys
from collections.abc import Callable
from math import inf
from game_helper import is_word_valid


def clear_lines(n: int) -> None:
    for _ in range(n):
        sys.stdout.write("\033[F\033[K")

    sys.stdout.flush()


def int_input_prompt(min_range: int = -inf, max_range: int = inf) -> int:
    while True:
        try:
            num = int(input("> "))
            if min_range <= num <= max_range:
                return num
            else:
                clear_lines(1)
        except:
            clear_lines(1)


def choice_prompt(
    prompt: str,
    choices: list[str] | None = None,
    validator: Callable[[str], str] | None = None,
    clear_count: int = 1,
    show_error: bool = False,
    after_error: Callable[[], None] | None = None,
) -> str:
    if prompt != "":
        print(prompt)

    while True:
        choice = input("> ")

        error = ""
        if choices is not None and choice not in choices:
            error = "Invalid choice"
        elif validator is not None:
            error = validator(choice)

        if error == "":
            return choice

        clear_lines(clear_count)
        if show_error:
            print(error)
        if after_error is not None:
            after_error()


def word_prompt(letters: list[str]) -> str:
    player_word = choice_prompt(
        "\nEnter word:\n",
        validator=lambda word: is_word_valid(word, letters),
        clear_count=2,
        show_error=True,
    )
    clear_lines(3)

    return player_word


def exchange_letters_prompt(letters: list[str]) -> list[str]:
    print()
    print("Enter letter to exchange (and . to confirm selection)")
    letters_left = letters.copy()
    letters_selected = []

    while True:
        print(" ".join(letters_selected))
        letter = choice_prompt(
            "",
            validator=lambda choice: ""
            if choice == "." or choice.upper() in letters_left
            else "Invalid choice",
            clear_count=2,
            after_error=lambda: print(" ".join(letters_selected)),
        )

        if letter == ".":
            return letters_selected

        selected_letter = letter.upper()
        letters_selected.append(selected_letter)
        letters_left.remove(selected_letter)
        clear_lines(2)
