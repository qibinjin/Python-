import pygame, random

WINDOW_HEIGHT = 768
WINDOW_WIDTH = 512

class GameMap(object):

    def __init__(self):

        self.num = str(random.randint(1,5))
        self.bg_img1 = pygame.image.load('res/img_bg_level_' + self.num + '.jpg')
        self.bg_img2 = pygame.image.load('res/img_bg_level_' + self.num + '.jpg')

        self.img1_y =  - WINDOW_HEIGHT
        self.img2_y = 0

        self.speed = 2
    def move(self):
        if self.img1_y >= 0:
            self.img1_y = -WINDOW_HEIGHT
            self.img2_y = 0
        self.img1_y += self.speed
        self.img2_y += self.speed
