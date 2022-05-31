"""
Module contains the snake class
The snake can move around the map either through player input or with AI
"""
import pygame


class Snake:
    def __init__(self, x, y, width, screen):
        self.x = x
        self.y = y
        self.width = width
        self.color = (255, 0, 0)
        self.screen = screen
        self.current_length = 5
        self.movement_direction = (1, 0)
        self.previous_positions = []

    def move(self, dt):
        """
        move the snake in the current direction
        :param dt: delta t, to manage the fps
        :return: None
        """
        self.previous_positions.append((self.x, self.y))
        self.x += self.movement_direction[0] * self.width
        self.y += self.movement_direction[1] * self.width

    def draw(self):
        """
        draw the snake on the map using the pygame screen
        :return: None
        """
        # draw head
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.width))
        # draw body
        for x in range(1, self.current_length):
            if len(self.previous_positions) < x:
                break
            pos = self.previous_positions[-x]
            pygame.draw.rect(self.screen, self.color, (pos[0], pos[1], self.width, self.width))