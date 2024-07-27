from GameOfLife import Game
from tabulate import tabulate
import sys
import os

def display_flags():
    
    input("Press any Key to continue: ")
    ...

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
    display_menu()
    
    actions = {
        1: lambda: print("A new window will be open with the game. Enjoy it!"),
        2: lambda: (clear_terminal(), display_flags(), display_menu()),
        3: sys.exit
    }
    
    while True:
        try:
            action = int(input("What do you want to do: "))
            if action in actions:
                actions[action]()
                if action == 1:  # Return after playing game
                    return
            else:
                print("Invalid Key, please enter a valid key")
        except ValueError:
            print("Invalid Key, please enter a valid key")
    
def read_arg():
    ...

def main():
    display_menu_actions()
    argv = sys.argv
    if len(argv) > 1:
        read_arg()
    game = Game()
    game.run()
    

if __name__ == "__main__":
    main()