import sys

from objects import Sign, Cross, Circle
import random

temp = {'1': '1', '2': '2', '3': '3', '4': '4',
        '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
board = f"""
         {temp['1']} | {temp['2']} | {temp['3']} 
        ___|___|___
         {temp['4']} | {temp['5']} | {temp['6']}
        ___|___|___
         {temp['7']} | {temp['8']} | {temp['9']}
        """
taken = []


def pick_player_symbol(player: str) -> Sign:
    if player.upper() == 'X':
        return Cross()
    elif player.upper() == 'O':
        return Circle()


def pick_computer_symbol(player: str) -> Sign:
    if player.upper() == "X":
        return Circle()
    elif player.upper() == "O":
        return Cross()


def pick_comp_spot(player_spot: int) -> int:
    while len(taken) < 8:
        comp = random.randint(1, 9)
        if comp != player_spot and comp not in taken:
            taken.append(comp)
            return comp
        else:
            pass


def pick_player_spot() -> int:
    while len(taken) <= 9:
        player = int(input("Pick a spot on the board: "))
        if player not in taken:
            taken.append(player)
            return player
        else:
            print("Pick another spot")


def game(player: str, computer: str) -> None:
    n = 0
    print(f"Player: {player} \tComputer: {computer}")
    print(board)
    while n != 5:
        n += 1
        player_spot = pick_player_spot()
        comp_spot = pick_comp_spot(player_spot)
        temp[str(player_spot)] = player
        temp[str(comp_spot)] = computer
        update_board()
        check_winner()
    print("===========[End of game]===========")
    update_board()
    print("===================================")


def check_winner() -> None:
    # Row 1
    if (temp['1'], temp['2'], temp['3']) == ('X', 'X', 'X'):
        print(f"Player {temp['1']} wins")
        sys.exit()
    elif (temp['1'], temp['2'], temp['3']) == ('O', 'O', 'O'):
        print(f"Player {temp['1']} wins")
        sys.exit()
    # Row 2
    elif (temp['4'], temp['5'], temp['6']) == ('X', 'X', 'X'):
        print(f"Player {temp['4']} wins")
        sys.exit()
    elif (temp['4'], temp['5'], temp['6']) == ('O', 'O', 'O'):
        print(f"Player {temp['4']} wins")
        sys.exit()
    # Row 3
    elif (temp['7'], temp['8'], temp['9']) == ('X', 'X', 'X'):
        print(f"Player {temp['7']} wins")
        sys.exit()
    elif (temp['7'], temp['8'], temp['9']) == ('O', 'O', 'O'):
        print(f"Player {temp['7']} wins")
        sys.exit()

    # Column 1
    elif (temp['1'], temp['4'], temp['7']) == ('X', 'X', 'X'):
        print(f"Player {temp['1']} wins")
        sys.exit()
    elif (temp['1'], temp['4'], temp['7']) == ('O', 'O', 'O'):
        print(f"Player {temp['1']} wins")
        sys.exit()
    # Column 2
    elif (temp['2'], temp['5'], temp['8']) == ('X', 'X', 'X'):
        print(f"Player {temp['2']} wins")
        sys.exit()
    elif (temp['2'], temp['5'], temp['8']) == ('O', 'O', 'O'):
        print(f"Player {temp['2']} wins")
        sys.exit()
    # Column 3
    elif (temp['3'], temp['6'], temp['9']) == ('X', 'X', 'X'):
        print(f"Player {temp['3']} wins")
        sys.exit()
    elif (temp['3'], temp['6'], temp['9']) == ('O', 'O', 'O'):
        print(f"Player {temp['3']} wins")
        sys.exit()

    # Diagonal 1
    elif (temp['1'], temp['5'], temp['9']) == ('X', 'X', 'X'):
        print(f"Player {temp['1']} wins")
        sys.exit()
    elif (temp['1'], temp['5'], temp['9']) == ('O', 'O', 'O'):
        print(f"Player {temp['1']} wins")
        sys.exit()

    elif (temp['3'], temp['5'], temp['7']) == ('X', 'X', 'X'):
        print(f"Player {temp['3']} wins")
        sys.exit()
    elif (temp['3'], temp['5'], temp['7']) == ('O', 'O', 'O'):
        print(f"Player {temp['3']} wins")
        sys.exit()


def update_board() -> None:
    print(
        f"""
             {temp['1']} | {temp['2']} | {temp['3']} 
            ___|___|___
             {temp['4']} | {temp['5']} | {temp['6']}
            ___|___|___
             {temp['7']} | {temp['8']} | {temp['9']}
        """

    )
