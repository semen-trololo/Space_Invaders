import random
import pygame
import sys
from bullet import Bullet
from ufo import Ufo
import time


def events(screen, gun, bullets):
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            sys.exit()
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


def update_screen(bg_collor, screen, gun, bullets, inos, stats):
    screen.fill(bg_collor)
    stats.show_stats()
    if collisions(screen, bullets, inos, gun, stats):
        gun_kill(stats, screen, gun, inos, bullets)
    # Отрисовываем все спрайты пуль
    for bullet in bullets.sprites():
        bullet.draw()
    inos.draw(screen)
    gun.draw()
    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()


def creat_ufos(screen, inos):
    """
    Создание группы пришельцев
    :param screen:
    :param inos: Grup ufo object
    :return: None
    """
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    ino = Ufo(screen, random.randint(0, 2))
    ino_width = ino.rect.width
    ino_height = ino.rect.height
    count_ufo_x = int((WIDTH - 2 * ino_width) / ino_width)
    count_ufo_y = int((HEIGHT - 100 - 2 * ino_height) / ino_height)
    for row_ino in range(int(float(count_ufo_y) / 1.2)):
        numer = random.randint(0, 2)
        for num_ino in range(count_ufo_x):
            ino = Ufo(screen, numer)
            ino.x = ino_width + ino_width * num_ino
            ino.y = ino_height + ino_height * row_ino
            ino.rect.x = ino.x
            ino.rect.y = ino.y
            inos.add(ino)


def collisions(screen, bullets, inos, gun, stats):
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        for y in collisions.values():
            stats.score += 2 * len(y)
        stats.image_score()
    if len(inos) == 0:
        stats.round += 1
        stats.image_round()
        stats.show_round()
        pygame.display.flip()
        time.sleep(2)
        pygame.event.clear()
        bullets.empty()
        creat_ufos(screen, inos)
        inos.draw(screen)
        gun.gun_reset()
        gun.draw()
        pygame.display.flip()
        return False
    if pygame.sprite.spritecollideany(gun, inos):
        return True
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            return True
    return False


def inos_update(inos):
    inos.update()


def gun_kill(stats, screen, gun, inos, bullets):
    """
    collis gun ena ino

    :param stats: start_stats
    :param screen:
    :param gun:
    :param inos:
    :param bullets:
    :return: None
    """

    stats.healf -= 1
    stats.image_half()
    if stats.healf == 0:
        bullets.empty()
        inos.empty()
        gun.gun_reset()
        gun.draw()
        stats.show_game_over()
        pygame.display.flip()
        time.sleep(3)
        pygame.event.clear()
        stats.run_game = False
    else:
        stats.round += 1
        stats.image_round()
        stats.show_round()
        pygame.display.flip()
        time.sleep(2)
        pygame.event.clear()
        bullets.empty()
        inos.empty()
        creat_ufos(screen, inos)
        gun.gun_reset()
        inos.draw(screen)
        gun.draw()
        pygame.display.flip()
