import pygame

WINDOW_HEIGHT = 768
WINDOW_WIDTH = 512

class PlaneBullet(object):

    def __init__(self):

        self.img = pygame.image.load('res/maozi.jpg')

        self.img_rect = self.img.get_rect()

        self.speed = 4

        self.is_shot = False


    def move_up(self):

        self.img_rect.move_ip(0, -self.speed)

        if self.img_rect[1] <= -self.img_rect[3]:

            self.is_shot = False

