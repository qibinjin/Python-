import pygame, random

WINDOW_HEIGHT = 768
WINDOW_WIDTH = 512

class EnemyPlane(object):

    def __init__(self):

        self.num = str(random.randint(1,7))

        self.img = pygame.image.load('res/img-plane_' + self.num + '.jpg')

        self.img_rect = self.img.get_rect()

        self.reset()
    def reset(self):

        self.img_rect[0] = random.randint(0, WINDOW_WIDTH - self.img_rect[2])
        self.img_rect[1] = -self.img_rect[3]

        self.speed = random.randint(1, 2)

    def move_down(self):

        self.img_rect.move_ip(0, self.speed)

        if self.img_rect[1] > WINDOW_HEIGHT:
            self.reset()