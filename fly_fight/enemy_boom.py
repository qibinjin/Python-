import pygame, random
class EnemyBoom(object):
    def __init__(self):
        self.num1 = random.randint(1, 14)

        self.boom_img = pygame.image.load('res/image %d.png' % self.num1)

        self.boom_img_rect = self.boom_img.get_rect()

        self.is_boom = False