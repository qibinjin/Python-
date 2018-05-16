import pygame, plane_bullet

WINDOW_HEIGHT = 768
WINDOW_WIDTH = 512

class HeroPlane(object):


    def __init__(self):

        self.img = pygame.image.load('res/timg.jpg')

        self.img_rect = self.img.get_rect()

        self.img_rect.move_ip((WINDOW_WIDTH - self.img_rect[2])/2, WINDOW_HEIGHT - self.img_rect[3] - 30)

        self.speed = 3

        self.bullet_list = [plane_bullet.PlaneBullet() for _ in range(8)]

    def move_up(self):
        if self.img_rect[1] > 0:
            self.img_rect.move_ip(0, -self.speed)

    def move_down(self):
        if self.img_rect[1] < WINDOW_HEIGHT - self.img_rect[3]:
            self.img_rect.move_ip(0, self.speed)

    def move_left(self):
        if self.img_rect[0] > 0:
            self.img_rect.move_ip(-self.speed, 0)

    def move_right(self):
        if self.img_rect[0] < WINDOW_WIDTH - self.img_rect[2]:
            self.img_rect.move_ip(self.speed, 0)

    def shot(self):

        for bullet in self.bullet_list:
            if not bullet.is_shot:

                bullet.img_rect[0] = self.img_rect[0] + (self.img_rect[2] - bullet.img_rect[2])/2
                bullet.img_rect[1] = self.img_rect[1] - bullet.img_rect[3]

                bullet.is_shot = True
                break