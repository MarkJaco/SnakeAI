"""
The main game file for making the snake game
"""
import random
import pygame
import food


# init pygame
pygame.init()

# create the Game class
class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode([width, height])
        self.running = False
        # init game objects
        self.snake = None
        self.food = []

    def run(self):
        self.running = True
        while self.running:
            self.handle_events()
            self.draw()

    def draw(self):
        """
        draw all objects on pygame screen
        """
        # Fill the background with white
        self.screen.fill((255, 255, 255))
        # draw the food
        for f in self.food:
            f.draw()
        # Flip the display
        pygame.display.flip()

    def handle_events(self):
        """
        handle all pygame events such as mouse clicks
        :return: None
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    ################
    # GAME METHODS #
    ################

    def spawn_food(self):
        """
        randomly spawn food on the game map
        """
        spawn_chance_per_frame = 0.001



if __name__ == "__main__":
    game = Game(800, 800)
    game.run()