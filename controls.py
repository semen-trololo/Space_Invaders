import random

import pygame
from bullet import Bullet
from ufo import Ufo


def events(screen, gun, bullets):
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gun.key_r = True
            elif event.key == pygame.K_LEFT:
                gun.key_l = True
            elif event.key == pygame.K_SPACE:
                # Создаем обьекты пули и добовляем его в список
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.key_r = False
            elif event.key == pygame.K_LEFT:
                gun.key_l = False
    return True


def update_screen(bg_collor, screen, gun, bullets, inos):
    screen.fill(bg_collor)
    inos.draw(screen)
    # Отрисовываем все спрайты пуль
    for bullet in bullets.sprites():
        bullet.draw()
    gun.draw()
    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()

def creat_ufos(screen, inos, WIDTH, HEIGHT):
    """
    Создание группы пришельцев
    :param screen:
    :param inos: Grup ufo object
    :return: None
    """
    ino = Ufo(screen, random.randint(0, 2))
    ino_width = ino.rect.width
    ino_height = ino.rect.height
    count_ufo_x = int((WIDTH - 2 * ino_width) / ino_width)
    count_ufo_y = int((HEIGHT - 100 - 2 * ino_height) / ino_height)
    for row_ino in range(count_ufo_y // 2):
        numer = random.randint(0, 2)
        for num_ino in range(count_ufo_x):
            ino = Ufo(screen, numer)
            ino.x = ino_width + ino_width * num_ino
            ino.y = ino_height + ino_height * row_ino
            ino.rect.x = ino.x
            ino.rect.y = ino.y
            inos.add(ino)
