"""
Module contains the label class
A label object is displayed on the pygame screen to indicate the presents of 
a detected object

creator: Mark Jacobsen
"""
import pygame


class Label:
    def __init__(self, x, y, width, height, txt, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.txt = txt
        self.screen = screen
        self.color = (255, 0, 0)
        self.border = 2

    def draw(self):
        """
        draw the label on the pygame screen
        :param screen: the pygame screen to draw on
        :returns: None
        """
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), self.border)