import pygame,sys
pygame.init()

window = pygame.display.set_mode([512, 768])

pygame.display.set_caption('飞机大战')

icon_img = pygame.image.load('res/app.ico')

pygame.display.set_icon(icon_img)

bg_img = pygame.image.load('res/img_bg_level_1.jpg')

window.blit(bg_img, (0, 0))

hero_img = pygame.image.load('res/hero.png')

window.blit(hero_img, (600, 190))

plane_img_rect = hero_img.get_rect()

print(plane_img_rect)
bullet_img  = pygame.image.load('res/hero_bullet_7.png')
bullet_img_rect = bullet_img.get_rect()




while True:
    window.blit(bg_img, (0, 0))
    window.blit(hero_img, (plane_img_rect[0], plane_img_rect[1]))

    event_list = pygame.event.get()
    for event in event_list:
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                print('biubiubiu....')

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
        plane_img_rect.move_ip(0, -1)
    elif pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
        plane_img_rect.move_ip(0, 1)

    if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
        plane_img_rect.move_ip(-1, 0)
    elif pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
        plane_img_rect.move_ip(1, 0)

    if pressed_keys[pygame.K_SPACE]:
        window.blit(bullet_img, (int(plane_img_rect[0] + plane_img_rect[2] / 2 - bullet_img_rect[2] / 2), int(plane_img_rect[1] - 70)))

        for i in range(0, 768):
            window.blit(bullet_img,(bullet_img_rect[0], bullet_img_rect[1]))
            bullet_img_rect.move_ip(0,-1)




    pygame.display.update()

input()