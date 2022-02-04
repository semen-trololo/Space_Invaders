import pygame


def events(gun):
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gun.key_r = True
            elif event.key == pygame.K_LEFT:
                gun.key_l = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.key_r = False
            elif event.key == pygame.K_LEFT:
                gun.key_l = False
    return True
