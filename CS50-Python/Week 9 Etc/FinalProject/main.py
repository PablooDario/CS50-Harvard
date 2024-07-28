from GameOfLife import Game
from tabulate import tabulate
import sys
import os
import argparse


def read_argv():
    """
    Parse command-line arguments for the Game of Life.
    
    Returns:
        dict: A dictionary of arguments with keys 'n', 'p', and 'c'.
    """
    parser = argparse.ArgumentParser(description="Play the Game of Life")
    parser.add_argument("-n", default=50, help="Number of cells playing", type=int)
    parser.add_argument("-p", default=0.2, help="Probability of a cell to be born alive", type=float)
    parser.add_argument("-c", default="white", help="Color of the alive cells", type=str)
    args = parser.parse_args()
    
    if args.n < 20 or args.n > 100:
        raise argparse.ArgumentTypeError(f"Invalid value for n: {args.n}. Valid Range [20, 100].")
    
    if args.p < 0.0 or args.p > 1.0:
        raise argparse.ArgumentTypeError(f"Invalid value for p: {args.p}. Valid Range [0, 1].")
    
    return vars(args)  


def display_flags():
    """Display the command-line flags and their descriptions."""
    
    print("-----The following flags should be passed via terminal-----")
    flags = [
        ["Flag", "Parameter", "Action"],
        ["-n", "Integer between 20 and 100", "Number of cells playing"],
        ["-p", "Float between 0 and 1", "Probability of a cell to be born alive"],
        ["-c", "A string specifying a color", "Color of the alive cells"],
        ["-h", "None", "Display the usage of the game and available colors for the cells"]
    ]
    print(tabulate(flags, headers="firstrow", tablefmt="mixed_grid"))
    while True:
        try:
            int(input("Press any number to continue: "))
            return
        except ValueError:
            print("Invalid input, please enter a number.")
    
    

def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')


def display_menu():
    actions = [
        ["Key", "Action"],
        ["1", "Play Game"],
        ["2", "View Flags to Configure Game"],
        ["3", "Exit"]
    ]
    print(tabulate(actions, headers="firstrow", tablefmt="mixed_grid"))

def display_menu_actions():
    """Display the main menu and handle user actions."""
    display_menu()
    
    actions = {
        "1": lambda: print("A new window will be opened with the game. Enjoy it!"),
        "2": lambda: (clear_terminal(), display_flags(), display_menu()),
        "3": sys.exit
    }
    
    while True:
        action = input("What do you want to do: ")
        if action in actions:
            actions[action]()
            if action == "1":  
                return
        else:
            print("Invalid input, please enter a valid key.")


def main():
    parameters = read_argv()
    
    display_menu_actions()
    game = Game(*parameters.values())
    game.run()
    

if __name__ == "__main__":
    main()
