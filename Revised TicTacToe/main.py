from actions import *


def main():
    player_choice: str = input("Pick X/O: ")
    player: Sign = pick_player_symbol(player_choice)
    computer: Sign = pick_computer_symbol(player_choice)

    game(player.str_symbol, computer.str_symbol)


if __name__ == '__main__':
    main()
