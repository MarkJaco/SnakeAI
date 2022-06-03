"""
Module collects data for object recognition
"""
import numpy as np
import os
import cv2
import pygame
from pathlib import Path


class DataCollector:
    def __init__(self):
        # directory paths
        self.script_dir = os.path.dirname(__file__)
        self.parent_dir = Path(self.script_dir).parent.absolute()
        self.image_path = os.path.join(str(self.parent_dir) + "\\"  + "Game" + "\\" + "images" + "\\")
        self.screenshot_path = os.path.join(self.image_path + "\\" + "screenshots" + "\\")
        self.detection_path = os.path.join(self.image_path + "\\" + "detection_images" + "\\")
        # find images
        self.apple_img = cv2.imread(self.detection_path + "apple.png", cv2.IMREAD_UNCHANGED)
        self.bomb_img = cv2.imread(self.detection_path + "bomb.png", cv2.IMREAD_UNCHANGED)
        self.snakebody_img = cv2.imread(self.detection_path + "snakebody.png", cv2.IMREAD_UNCHANGED)
        self.snakehead_left_img = cv2.imread(self.detection_path + "snake_head_left.png", cv2.IMREAD_UNCHANGED)
        self.snakehead_right_img = cv2.imread(self.detection_path + "snake_head_right.png", cv2.IMREAD_UNCHANGED)
        self.snakehead_up_img = cv2.imread(self.detection_path + "snake_head_up.png", cv2.IMREAD_UNCHANGED)
        self.snakehead_down_img = cv2.imread(self.detection_path + "snake_head_down.png", cv2.IMREAD_UNCHANGED)
        # other
        self.threshold = 0.6

    def group_findings(self, xloc, yloc):
        """
        group recognised objects so that one object is not recognised
        multiple times
        :param xloc: the x locations of the found objects
        :param yloc: the y locations of the found objects
        :return: (xnew, ynew) holding only the relevant locations
        """
        if len(xloc) == 0:
            return [], []
        xnew = [xloc[0]]
        ynew = [yloc[0]]
        for (x, y) in zip(xloc, yloc):
            xdifference, ydifference = 0, 0
            for i in range(len(xnew)):
                xdifference = abs(xnew[i] - x)
                ydifference = abs(ynew[i] - y)
            if xdifference + ydifference >= 20:
                xnew.append(x)
                ynew.append(y)
        return xnew, ynew

    def get_screen_data(self, screen):
        """
        get the screen data to recognize objects
        :param screen: the pygame screen to detect object on
        :return: None
        """
        # make and load image of current game state
        pygame.image.save(screen, self.screenshot_path + "screenshot.png")
        game_img = cv2.imread(self.screenshot_path + "screenshot.png", cv2.IMREAD_UNCHANGED)

        # get apples
        result = cv2.matchTemplate(game_img, self.apple_img, cv2.TM_CCOEFF_NORMED)
        yloc, xloc = np.where(result >= self.threshold)
        xnew, ynew = self.group_findings(xloc, yloc)
        self.draw_labels(xnew, ynew, "Apple", (255, 0, 0), self.apple_img, screen)

        # get bombs
        result = cv2.matchTemplate(game_img, self.bomb_img, cv2.TM_CCOEFF_NORMED)
        yloc, xloc = np.where(result >= self.threshold)
        xnew, ynew = self.group_findings(xloc, yloc)
        self.draw_labels(xnew, ynew, "Bomb", (255, 255, 0), self.bomb_img, screen)

        # get snakehead

    def draw_labels(self, xlocations, ylocations, label, color, img, screen):
        """
        draws boxes around identified objects and labels them
        :param xlocations: x locations of the objects
        :param ylocations: y locations of the objects to label
        :param label: what to label as (string)
        :param color: rgb color of box as (r, g, b) tuple
        :param img: the image that was used to identify the objects
        :param screen: the pygame screen to draw on
        :return: None
        """
        width = img.shape[1]
        height = img.shape[0]
        for (x, y) in zip(xlocations, ylocations):
            print(f"drawing rect: {(x, y, width, height)}")
            pygame.draw.rect(screen, color, (x, y, width, height), 5)

        

    
