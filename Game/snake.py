"""
Module contains the snake class
The snake can move around the map either through player input or with AI
"""
import pygame
import os


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
        # images
        self.script_dir = os.path.dirname(__file__)
        self.image_path = os.path.join(self.script_dir + "\\" + "images" + "\\")
        self.setup_images()
        self.current_image = self.head_image_right

    def setup_images(self):
        """
        setup the snake images
        """
        head_image = "snake_head_up.png"
        self.head_image_up = pygame.transform.scale(pygame.image.load(self.image_path + head_image), (self.width, self.width))
        head_image = "snake_head_down.png"
        self.head_image_down = pygame.transform.scale(pygame.image.load(self.image_path + head_image), (self.width, self.width))
        head_image = "snake_head_right.png"
        self.head_image_right = pygame.transform.scale(pygame.image.load(self.image_path + head_image), (self.width, self.width))
        head_image = "snake_head_left.png"
        self.head_image_left = pygame.transform.scale(pygame.image.load(self.image_path + head_image), (self.width, self.width))

    def move(self, dt):
        """
        move the snake in the current direction
        :param dt: delta t, to manage the fps
        :return: None
        """
        self.previous_positions.append((self.x, self.y))
        self.x += self.movement_direction[0]
        self.y += self.movement_direction[1]

    def draw(self, c_width):
        """
        draw the snake on the map using the pygame screen
        :param c_width: the cell width to adjust the coordinates
        :return: None
        """
        # draw head
        # pygame.draw.rect(self.screen, self.color, (self.x * c_width, self.y * c_width, self.width, self.width))
        self.screen.blit(self.current_image, (self.x * c_width, self.y * c_width))
        # draw body
        for i in range(1, self.current_length):
            if len(self.previous_positions) < i:
                break
            pos = self.previous_positions[-i]
            pygame.draw.rect(self.screen, self.color, (pos[0] * c_width, pos[1] * c_width, self.width, self.width))

    def handle_events(self, event):
        """
        handle pygame input events such as key presses
        :param event: the current occuring pygame event
        :return: None
        """
        # get key presses
        if event.type == pygame.KEYDOWN:
            # change direction based on arrow keys
            if event.key == pygame.K_LEFT:
                if self.movement_direction != (1, 0):
                    self.movement_direction = (-1, 0)
                    self.current_image = self.head_image_left
            if event.key == pygame.K_RIGHT:
                if self.movement_direction != (-1, 0):
                    self.movement_direction = (1, 0)
                    self.current_image = self.head_image_right
            if event.key == pygame.K_UP:
                if self.movement_direction != (0, 1):
                    self.movement_direction = (0, -1)
                    self.current_image = self.head_image_up
            if event.key == pygame.K_DOWN:
                if self.movement_direction != (0, -1):
                    self.movement_direction = (0, 1)
                    self.current_image = self.head_image_down

    def collision_detection(self, food):
        """
        detect if the snake has collided with one of:
            - itself
            - edge
            - food
        :param food: list of all foods currently on the map
        :return: the object it collided with, ("edge" for edge), (None for nothing)
        """
        # detect edge
        if self.x < 0 or self.x > 24:
            return "edge"
        if self.y < 0 or self.y > 19:
            return "edge"

        # detect food
        for item in food:
            if self.x == item.x and self.y == item.y:
                return item

        # detect itself
        for i in range(self.current_length):
            if i > len(self.previous_positions):
                continue
            if self.x == self.previous_positions[-i][0] and self.y == self.previous_positions[-i][1]:
                return "itself"