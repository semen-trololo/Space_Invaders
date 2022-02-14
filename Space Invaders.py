import time

import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
#  pygame-2.1.2
WIDTH = 500  # ширина игрового окна
HEIGHT = 600  # высота игрового окна
BLACK = (0, 0, 0)


def run():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Invaders")
    while game_loop(screen):
        pass


def game_loop(screen):
    start_stats = Stats(screen)
    gun = Gun(screen)
    # pygame.sprite.Group()
    bullets = Group()
    inos = Group()
    screen.fill(BLACK)
    start_stats.image_round()
    start_stats.show_round()
    pygame.display.flip()
    time.sleep(2)
    controls.creat_ufos(screen, inos)
    while True:
        if start_stats.run_game == False:
            return True
        controls.events(screen, gun, bullets)
        gun.update()
        '''У групп есть методы update() и draw(). Метод update() группы вызывает методы update()
         всех входящих в нее объектов. А метод draw() выполняет метод blit(). '''
        bullets.update()
        controls.inos_update(inos)
        controls.update_screen(BLACK, screen, gun, bullets, inos, start_stats)


run()
pygame.quit()
