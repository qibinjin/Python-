import pygame

WINDOW_WIDTH = 512
WINDOW_HEIGHT = 768

class GameWindow(object):
    def __init__(self):
        self.window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
        self.icon_img = pygame.image.load('res/app.ico')
        pygame.display.set_icon(self.icon_img)
        pygame.display.set_caption('飞机大战')
    def action(self):
        pass
    def draw(self):
        pass
    def event(self):
        pass
    def update(self):
        pass

    def run(self):
        while True:
            self.action()

            self.draw()

            self.event()

            self.update()
def main():
    game = GameWindow()

    game.run()

if __name__ == '__main__':
    main()




