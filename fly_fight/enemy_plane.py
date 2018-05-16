import pygame, random,enemy_boom

WINDOW_HEIGHT = 768
WINDOW_WIDTH = 512

class EnemyPlane(object):

    def __init__(self):

        self.num = str(random.randint(1,7))

        self.img = pygame.image.load('res/img-plane_' + self.num + '.jpg')


        self.img_rect = self.img.get_rect()

        self.boom_list = [enemy_boom.EnemyBoom() for _ in range(5)]

        self.reset()

    def reset(self):

        self.img_rect[0] = random.randint(0, WINDOW_WIDTH - self.img_rect[2])
        self.img_rect[1] = -self.img_rect[3]

        self.speed = random.randint(1, 2)

    def move_down(self):

        self.img_rect.move_ip(0, self.speed)

        if self.img_rect[1] > WINDOW_HEIGHT:
            self.reset()

    def boom(self):
        for n in self.boom_list:
            if not n.is_boom:
                n.boom_img_rect[0] = self.img_rect[0]
                n.boom_img_rect[1] = self.img_rect[1]
                n.is_boom = True
                break
            n.is_boom = False

