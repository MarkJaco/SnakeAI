"""
The main game file for making the snake game
"""
import random
import pygame
import food
import snake
import grid


# init pygame
pygame.init()

# create the Game class
class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode([width, height])
        self.running = False
        self.clock = pygame.time.Clock()
        self.current_frame = 0
        # init game objects
        self.cell_width = 25
        self.grid = grid.Grid(self.width, self.height, self.cell_width, self.screen)
        self.snake = snake.Snake(self.width / 2, self.height / 2, self.cell_width, self.screen)
        self.food = []

    #################
    # SETUP METHODS #
    #################

    def run(self):
        self.running = True
        while self.running:
            # manage the fps
            self.current_frame += 1
            dt = self.clock.tick(60)
            
            # setup
            self.handle_events()
            self.draw()
            
            # randomly spawn new food
            self.spawn_food()

            # move the snake
            if self.current_frame % 10 == 0:
                self.snake.move(dt)

    def draw(self):
        """
        draw all objects on pygame screen
        """
        # Fill the background with white
        self.screen.fill((255, 255, 255))
        # draw the underlying grid
        self.grid.draw()
        # draw the food
        for f in self.food:
            f.draw()
        # draw the snake
        self.snake.draw()
        # Flip the display
        pygame.display.flip()

    def handle_events(self):
        """
        handle all pygame events such as mouse clicks
        :return: None
        """
        # handle game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
            # handle snake events
            self.snake.handle_events(event)

    ################
    # GAME METHODS #
    ################

    def spawn_food(self):
        """
        randomly spawn food on the game map
        """
        spawn_chance_per_frame = 0.01
        if random.random() < spawn_chance_per_frame:
            food_type = random.choice([food.Apple, food.Bomb])
            random_x = random.randrange(int(self.width / self.cell_width)) * self.cell_width
            random_y = random.randrange(int(self.height / self.cell_width)) * self.cell_width
            random_food = food_type(random_x, random_y, self.cell_width, self.screen)
            self.food.append(random_food)



if __name__ == "__main__":
    game = Game(1000, 800)
    game.run()