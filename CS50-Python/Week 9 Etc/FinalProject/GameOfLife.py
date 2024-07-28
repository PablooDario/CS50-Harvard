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
    def __init__(self, number_of_cells=50, probability_alive=0.2, color="white"):
        pygame.init()

        # Set the size of the screen
        self.width = 500
        self.height = 500
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game of Life")
        self.running = True
        self.start_game = False

        # Set the size of the grid and cell
        self.grid_size = number_of_cells
        self.cell_size = self.width // self.grid_size

        # Initialize the grid
        pd, pa = (1 - probability_alive, probability_alive)
        probabilities = [pd, pa]
        self.grid = np.random.choice(
            [0, 1], size=(self.grid_size, self.grid_size), p=probabilities
        )
        
        self.color = color

    def run(self):
        # Display start screen
        self._start_screen()

        # Run Game of Life and update the grid in each iteration
        while self.running:
            for event in pygame.event.get():
                # If the user closes the window game
                if event.type == pygame.QUIT:
                    self.running = False

            if self.start_game:
                self._update_grid()
                pygame.display.flip()

        pygame.quit()

    def _is_inside(self, x: int, y: int) -> bool:
        '''
        Determine if a cell is inside of the grid to avoid Index out of bounds.
        
        :param x: Coordinate x in the grid
        :param y: Coordinate y in the grid
        
        :return: True if the cell is inside and False if it is out of the grid
        :rtype: bool
        '''
        return 0 <= x < self.grid_size and 0 <= y < self.grid_size

    def _update_grid(self):
        
        new_grid = np.zeros_like(self.grid)
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                alive = 0
                for d in Game.directions:
                    x, y = (i + d[0], j + d[1])
                    if self._is_inside(x, y) and self.grid[x][y]:
                        alive += 1

                color = self._rules(self.grid[i][j], alive)
                new_grid[i][j] = 1 if color == self.color else 0
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
        
        :param is_alive: 1 if the cell is alive, 0 if it is dead
        :param alive_neighbors: number of alive neighbors
        
        :return: A string indicating 'white' if the cell is alive or 'black' if it is dead
        :rtype: str
        '''
        if is_alive:
            if alive_neighbors == 2 or alive_neighbors == 3:
                return self.color
            return "black"
        if alive_neighbors == 3:
            return self.color
        return "black"

    def _start_screen(self):
        '''Display the start screen with a title and a start button.'''
        font = pygame.font.Font(None, 74)
        title_text = font.render("Game of Life", True, pygame.Color('white'))
        start_button = pygame.Rect(self.width // 2 - 100, self.height // 2, 200, 50)
        button_text = font.render("Start", True, pygame.Color('black'))
        button_color = pygame.Color('white')

        while not self.start_game:
            self.screen.fill(pygame.Color('black'))
            self.screen.blit(title_text, (self.width // 2 - title_text.get_width() // 2, self.height // 4))

            pygame.draw.rect(self.screen, button_color, start_button)
            self.screen.blit(button_text, (start_button.x + (start_button.width - button_text.get_width()) // 2, start_button.y + (start_button.height - button_text.get_height()) // 2))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.start_game = True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if start_button.collidepoint(event.pos):
                        self.start_game = True

            pygame.display.flip()


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
