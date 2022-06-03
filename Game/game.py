"""
The main game file for making the snake game
"""
import random
import pygame
from .food import Food, Apple, Bomb
from .snake import Snake
from .grid import Grid


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
        self.cell_width = 40
        self.grid = Grid(self.width, self.height, self.cell_width, self.screen)
        self.snake = Snake(0, 0, self.cell_width, self.screen)
        self.food = []
        # other input
        self.external_function = None
        self.func_parameters = None

    def add_external_function(self, func, *args):
        """
        add external function that is to be called in the run loop
        :param func: the function that is to be executed
        :param args: the parameters to run the function
        :return: None
        """
        self.external_function = func
        self.func_parameters = args

    #################
    # SETUP METHODS #
    #################

    def run(self):
        self.running = True
        while self.running:
            if self.current_frame == 1000:
                return
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
                self.handle_collision()
            if self.current_frame % 100 == 0:
                # call external function
                if self.external_function:
                    self.external_function(*self.func_parameters)

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
            f.draw(self.cell_width)
        # draw the snake
        self.snake.draw(self.cell_width)
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
            food_type = random.choice([Apple, Bomb])
            random_x = random.randrange(int(self.width / self.cell_width))
            random_y = random.randrange(int(self.height / self.cell_width))
            random_food = food_type(random_x, random_y, self.cell_width, self.screen)
            self.food.append(random_food)

    def handle_collision(self):
        """
        handles snake collision with food etc.
        :return: None
        """
        collided_with = self.snake.collision_detection(self.food)
        if collided_with == "edge" or collided_with == "itself":
            self.running = False
            return
        if isinstance(collided_with, Food):
            self.handle_food_effect(collided_with)

    def handle_food_effect(self, collided_with):
        """
        after colliding with a certain type of food
        apply the food effect to the game
        :param collided_with: the food that was collided with
        :return: None
        """
        self.food.remove(collided_with)
        if collided_with.effect == "death":
            self.running = False
        elif collided_with.effect == "increase length":
            self.snake.current_length += 1


if __name__ == "__main__":
    game = Game(1000, 800)
    game.run()