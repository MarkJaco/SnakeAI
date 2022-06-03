"""
Module collects data for object recognition
"""
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

    def get_screen_data(self, screen):
        """
        get the screen data to recognize objects
        :param screen: the pygame screen to detect object on
        :return: None
        """
        pygame.image.save(screen, self.screenshot_path + "screenshot.png")
        game_img = cv2.imread(self.screenshot_path + "screenshot.png", cv2.IMREAD_UNCHANGED)
    
