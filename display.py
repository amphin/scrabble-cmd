def print_title():
    print(r"""                             __       __       ___                                      __     
                            /\ \     /\ \     /\_ \                                    /\ \    
  ____    ___   _ __    __  \ \ \____\ \ \____\//\ \      __         ___    ___ ___    \_\ \   
 /',__\  /'___\/\`'__\/'__`\ \ \ '__`\\ \ '__`\ \ \ \   /'__`\      /'___\/' __` __`\  /'_` \  
/\__, `\/\ \__/\ \ \//\ \L\.\_\ \ \L\ \\ \ \L\ \ \_\ \_/\  __/     /\ \__//\ \/\ \/\ \/\ \L\ \ 
\/\____/\ \____\\ \_\\ \__/.\_\\ \_,__/ \ \_,__/ /\____\ \____\    \ \____\ \_\ \_\ \_\ \___,_\
 \/___/  \/____/ \/_/ \/__/\/_/ \/___/   \/___/  \/____/\/____/     \/____/\/_/\/_/\/_/\/__,_ /)
""")


def print_board(board):
    print("      1  2  3  4  5  6  7  8  9  10 11 12 13 14 15")
    print("      |  |  |  |  |  |  |  |  |  |  |  |  |  |  |")

    for i in range(len(board[0])):
        if i < 9:
            print(" ", end="")
        print(f"{i+1} - ", end="")

        for j in range(len(board[i])):
            print(f"[{board[i][j]}]", end="")
        print()


# TODO: center text based on player name length
def print_player_turn_start(player):
    print("--------------------------------------------------------")
    print(f"                    {player.upper()}'S TURN                    ")
    print("--------------------------------------------------------")


def print_player_tiles(tiles, points):
    print("              ", end="")
    for tile in tiles:
        print(tile, end="   ")

    print()
    print("             ", end="")
    for point in points:
        if point < 10:
            print(" ", end="")
        print(point, end="  ")

    print()
