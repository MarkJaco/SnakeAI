"""
Module contains the label class
A label object is displayed on the pygame screen to indicate the presents of 
a detected object

creator: Mark Jacobsen
"""
import pygame


class Label:
    def __init__(self, x, y, txt, screen):
        self.x = x
        self.y = y
        self.txt = txt
        self.screen = screen
        self.color = (255, 0, 0)
        self.border = 2

    def draw(self, cell_width):
        """
        draw the label on the pygame screen
        :param cell_width: the current used cell width in the map as int
        :returns: None
        """
        rect_size = cell_width * 1.5
        subtract = cell_width * 0.25
        x = self.x - subtract
        y = self.y - subtract
        pygame.draw.rect(self.screen, self.color, (x, y, rect_size, rect_size), self.border)