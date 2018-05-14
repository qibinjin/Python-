import pygame, sys, random, game_map, hero_plane, enemy_plane, game_score

WINDOW_HEIGHT = 768
WINDOW_WIDTH = 512

class GameWindow(object):
    __cls_score = 0

    def __init__(self):
        pygame.init()

        self.set_game_music()

        self.boom_sound = pygame.mixer.Sound('res/baozha.ogg')

        self.window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

        pygame.display.set_caption('飞机大战')

        logo_image = pygame.image.load('res/app.ico')

        pygame.display.set_icon(logo_image)

        self.map = game_map.GameMap()

        self.hero_plane = hero_plane.HeroPlane()

        self.enemy_plane_list = [enemy_plane.EnemyPlane() for _ in range(5)]

        self.game_score = game_score.GameScore(30)

    def set_game_music(self):

        pygame.mixer.music.load('res/bg2.ogg')

        pygame.mixer.music.play(-1)

    def __action(self):

        self.map.move()

        for bullet in self.hero_plane.bullet_list:
            if bullet.is_shot:
                bullet.move_up()

        for enemy in self.enemy_plane_list:
            enemy.move_down()
    def __draw(self):
        self.window.blit(self.map.bg_img1, (0, self.map.img1_y))
        self.window.blit(self.map.bg_img2, (0, self.map.img2_y))

        self.window.blit(self.hero_plane.img, (self.hero_plane.img_rect[0], self.hero_plane.img_rect[1]))

        for bullet in self.hero_plane.bullet_list:
            if bullet.is_shot:
                self.window.blit(bullet.img, (bullet.img_rect[0], bullet.img_rect[1]))
        for enemy in self.enemy_plane_list:
            self.window.blit(enemy.img, (enemy.img_rect[0], enemy.img_rect[1]))

        self.window.blit(self.game_score.text_obj, (5, 5))

    def __event(self):

        event_list = pygame.event.get()

        for event in event_list:
            if event.type == pygame.QUIT:
                self.__game_over()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__game_over()

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            self.hero_plane.move_up()
        if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
            self.hero_plane.move_down()
        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            self.hero_plane.move_left()
        if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            self.hero_plane.move_right()
        if keys_pressed[pygame.K_SPACE]:
            self.hero_plane.shot()
    def __update(self):

        pygame.display.update()

    def __bullet_hit_enemyplane(self):
        for bullet in self.hero_plane.bullet_list:

            if bullet.is_shot:

                for enemy in self.enemy_plane_list:

                    if pygame.Rect.colliderect(bullet.img_rect, enemy.img_rect):

                        bullet.is_shot = False

                        enemy.reset()

                        self.__set_boom_sound()

                        self.game_score.set_text_obj()

    def __set_boom_sound(self):

        self.boom_sound.play()

    def __game_over(self):
        print('游戏结束')

        pygame.mixer.music.stop()

        self.boom_sound.stop()

        sys.exit()

        pygame.quit()

    def run(self):
        while True:
            self.__action()
            self.__draw()
            self.__event()
            self.__update()
            self.__bullet_hit_enemyplane()

def main():
    game = GameWindow()

    game.run()

if __name__ == '__main__':
    main()
