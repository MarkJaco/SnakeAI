"""
contains the food class and all subclasses
a food object can be eaten by the snake and creates some sort of effect
this effect can be good or bad

Parameters:
    x: the x position to spawn the food
    y: the y position ot spawn the food
    screen: the pygame screen to draw on
"""
import pygame


class Food:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.color = (0, 255, 0)
        self.radius = 30
        self.effect = ""
        self.image_path = ""
        self.image = None

    def draw(self):
        """
        draw the food on the pygame screen
        """
        # pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
        self.screen.blit(self.image, (self.x, self.y))


class Apple(Food):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.image_path = "images/apple.png"
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (self.radius, self.radius))


class Bomb(Food):
    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)
        self.image_path = "images/bomb.png"
        self.image = pygame.image.load(self.image_path)
        self.radius = 50
        self.image = pygame.transform.scale(self.image, (self.radius, self.radius))
