import random
import sys

from colorama import Fore, Back

global board_values
global spots

board_values = {"1": " ", "2": " ", "3": " ",
                "4": " ", "5": " ", "6": " ",      
                "7": " ", "8": " ", "9": " "}
spots = []

class Game:
    """
    Move functions outside the class into it and use self.method_name() to call them
    inside the class.
    """
    def __init__(self):
        self.player = ""
        self.computer = ""

    
    def choose_sign(self, sign):
        if sign.upper() == "X" or sign.upper() == "O":
            self.player = sign
        else:
            print("Please pick X/O")
            sys.exit()

        if self.player.upper() == "X":
            self.computer = "O"
        else:
            self.computer = "X"

        print(f"Player: {self.player.upper()}, Computer: {self.computer.upper()}")
    
    def play(self):
        # Make logic more readable.
        ##########################################################################################################
        # TODO: Create a list with values 1-9 remove values from it when a spot is picked by the user or computer#
        # and use it to check if a spot has been taken. Good luck!                                               #
        ##########################################################################################################
        n = 0
        picked_spot = []
        update_board()
        while n <= 9:
            print(spots)    
            position = input("Where do you want to play(1-9)?: ")

            if int(position) in range(1, 10):
                # use if and statement instead of nesting another branch in it...
                if board_values[position] == " ":
                    board_values[position] = self.player.upper()
                    print(f"Player position: {position}")
                    spots.append(int(position))
                    n = n + 1

                    cpu_choice = cpu_choice_handler()
                    print(f"CPU position: {cpu_choice}")
                    spots.append(cpu_choice)
                    print(f"Spots: {spots}")
                    print(f"Cpu choice: {cpu_choice}")
                    board_values[f"{cpu_choice}"] = self.computer 
                    n = n + 1
                    
                else:
                    print(Fore.RED + "Pick another spot!")
            else:
                print("Error")

            update_board()
            # print(board_values)
        print("Game Over!")
        print(check_winner())


def update_board():
    board_grid = f"""
                {board_values["1"]} | {board_values["2"]} | {board_values["3"]}
                --|---|--
                {board_values["4"]} | {board_values["5"]} | {board_values["6"]}
                --|---|--
                {board_values["7"]} | {board_values["8"]} | {board_values["9"]}
                """

    print(board_grid)


def cpu_choice_handler():
    choice = random.randint(1, 9)
    if choice in spots:
        choice = random.randint(1, 9)
        if choice in spots:
            choice = random.randint(1, 9)
        else:
            return choice
    else:
        return choice
    print(f"Chosen choice: {choice}")
            

def check_winner():
    winner = "Foo"
    return f"The winner is {winner}"


def main():
    try:
        game = Game()
        game.choose_sign(input("What do you want to play as (X/O)?: "))
        game.play()

    except ValueError:
        game = Game()
        game.choose_sign(input("What do you want to play as (X/O)?: "))
        game.play()



main()
