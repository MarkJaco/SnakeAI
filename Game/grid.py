"""
Module contains the grid class for the board to play snake on
"""
import pygame


class Grid:
    def __init__(self, width, height, cell_width, screen):
        self.width = width
        self.height = height
        self.cell_width = cell_width
        self.screen = screen
        self.colors = [(0, 250, 154), (143, 188, 143)]

    def draw(self):
        color_index = 0
        for x in range(0, self.width, self.cell_width):
            color_index = 1 if color_index == 0 else 0
            for y in range(0, self.height, self.cell_width):
                pygame.draw.rect(self.screen, self.colors[color_index], (x, y, self.cell_width, self.cell_width))
                color_index = 1 if color_index == 0 else 0