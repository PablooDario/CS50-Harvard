# Game of Life

## Overview

The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It's a zero-player game, meaning its evolution is determined by its initial state, with no further input from human players. The game consists of a grid of cells that can live, die, or multiply based on specific rules.

## Rules of the Game

1. **Birth**: A dead cell with exactly three live neighbors becomes a live cell.
2. **Survival**: A live cell with two or three live neighbors stays alive.
3. **Death by isolation**: A live cell with fewer than two live neighbors dies.
4. **Death by overcrowding**: A live cell with more than three live neighbors dies.

## How to Play

1. **Installation**: Ensure you have Python installed on your system. Then, clone the repository and navigate to its directory.

2. **Running the Game**: Use the terminal to run the game with customizable parameters.

### Main Menu

Before playing, you will be presented with a main menu with the following options:

- **Play Game:** Starts the Game of Life in a new window.
- **View Flags to Configure Game:** Displays the command-line flags and their descriptions.
- **Exit:** Exits the game.

### Flags for a custom setting

| Flag | Parameter                     | Action                                |
|------|-------------------------------|---------------------------------------|
| `-n` | Integer between 20 and 100    | Number of cells playing               |
| `-p` | Float between 0 and 1         | Probability of a cell to be born alive|
| `-c` | A string specifying a color   | Color of the alive cells              |
| `-h` | None                          | Display the usage of the game and available colors for the cells |

## Usage Example

To run the game with default settings:

```bash
python main.py
```

Examples of custom settings:

```bash
python main.py -n 60 -p 0.3 -c blue
```

```bash
python main.py -n 50 -p 0.2 -c green
```