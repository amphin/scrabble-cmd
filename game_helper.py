import sys
import game_pieces as gp


def get_tile_points(letters):
    tile_points = []
    for tile in letters:
        tile_points.append(gp.letter_points[tile])

    return tile_points


def num_input_prompt(min_range, max_range):
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
