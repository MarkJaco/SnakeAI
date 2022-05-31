"""
The main game file for making the snake game
"""
import random
import pygame
import food
import snake


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
        self.snake = snake.Snake(self.width / 2, self.height / 2, 30, self.screen)
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
            random_x = random.randrange(self.width)
            random_y = random.randrange(self.height)
            random_food = food.Apple(random_x, random_y, self.screen)
            self.food.append(random_food) 



if __name__ == "__main__":
    game = Game(1000, 800)
    game.run()