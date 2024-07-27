import os
# Hide Pygame messages
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import numpy as np

class Game:
    # Directions to iterate over the neighbors of the cell 'x'
    directions = (
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
        )
    def __init__(self):
        pygame.init()

        # Set the size of the screen
        self.width = 500
        self.height = 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.running = True

        # Set the size of the grid and cell
        self.grid_size = 50
        self.cell_size = self.width // self.grid_size

        # Initialize the grid
        probabilities = [0.8, 0.2]
        self.grid = np.random.choice(
            [0, 1], size=(self.grid_size, self.grid_size), p=probabilities
        )

    def run(self):
        # Run Game of Life and update the grid in each iteration
        while self.running:
            for event in pygame.event.get():
                # If the ser closes the window game
                if event.type == pygame.QUIT:
                    self.running = False

            self._update_grid()
            pygame.display.flip()

        pygame.quit()

    def _is_inside(self, x: int, y: int) -> bool:
        '''
        Determine if a cell is inside of the grid to avoid Index out of bounds.
        
        :param x: Coordenate x in the grid
        :param y: Coordenate y in the grid
        
        :return: 1 if the cell is inside and 0 if it is out of the grid
        :rtype: bool
        '''
        return x >= 0 and y >= 0 and x < self.grid_size and y < self.grid_size

    def _update_grid(self):
        '''
        DocString missing
        '''
        
        new_grid = np.zeros_like(self.grid)
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                alive = 0
                for d in Game.directions:
                    x, y = (i + d[0], j + d[1])
                    if self._is_inside(x, y) and self.grid[x][y]:
                        alive += 1

                color = self._rules(self.grid[i][j], alive)
                new_grid[i][j] = 1 if color == "white" else 0
                dimensions = (
                    i * self.cell_size,
                    j * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
                pygame.draw.rect(self.screen, color, dimensions)
        self.grid = new_grid

    def _rules(self, is_alive: int, alive_neighbors: int) -> str:
        '''
        Determine whether a cell will be dead or alive at the next iteration.
        
        :param is_alve: 1 if the cell is alive, 0 if is dead
        :param alive_neighbors: number of alive neighbors
        
        :return: A string saying 'white' if the cell is alive or black in other case
        :rtype: str
        '''
        
        if is_alive:
            if alive_neighbors == 2 or alive_neighbors == 3:
                return "white"
            return "black"
        if alive_neighbors == 3:
            return "white"
        return "black"


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
