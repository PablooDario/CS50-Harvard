import pygame
import numpy as np


class Game:
    def __init__(self):
        pygame.init()
        self.directions = (
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
        )

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
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.update_grid()
            pygame.display.flip()

        pygame.quit()

    def is_inside(self, x, y):
        return x >= 0 and y >= 0 and x < self.grid_size and y < self.grid_size

    def update_grid(self):
        new_grid = np.zeros_like(self.grid)
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                alive = 0
                for d in self.directions:
                    x, y = (i + d[0], j + d[1])
                    if self.is_inside(x, y) and self.grid[x][y]:
                        alive += 1

                color = self.rules(self.grid[i][j], alive)
                new_grid[i][j] = 1 if color == "white" else 0
                dimensions = (
                    i * self.cell_size,
                    j * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
                pygame.draw.rect(self.screen, color, dimensions)
        self.grid = new_grid

    def rules(self, is_alive, alive):
        if is_alive:
            if alive == 2 or alive == 3:
                return "white"
            return "black"
        if alive == 3:
            return "white"
        return "black"


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
