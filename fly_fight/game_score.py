import pygame, random

class GameScore(object):

    __game_score = 0

    def __init__(self, font_size):

        self.font = pygame.font.SysFont('SimHei', font_size)

        self.text_obj = self.font.render('分数:0', 1, (255, 255, 255))

    def set_text_obj(self):
        GameScore.__game_score += 5
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        self.text_obj = self.font.render('分数:%d' % GameScore.__game_score, 1, (r, g, b))