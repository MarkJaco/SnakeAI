"""
This module is used for conversion between input and output to tensorflow models etc.

creator: Mark Jacobsen
"""
import numpy as np


def pygame_to_list(screen):
    """
    this function converts the current pygame pixels into a list
    of RGB values, stored as BGR
    This replaces having to store the image and using cv2 for loading
    :param screen: the pygame screen to convert
    :return: list of rows of RGB values for the pixels
    """
    width, height = screen.get_size()
    
    return_list = []
    for y in range(height):
        row = []
        for x in range(width):
            color = screen.get_at((x, y))
            row.append(color)
        return_list.append(row)

    return return_list