import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats

WIDTH = 500  # ширина игрового окна
HEIGHT = 600  # высота игрового окна
BLACK = (0, 0, 0)


def run():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Invaders")
    game_loop(screen)


def game_loop(screen):
    start_stats = Stats(screen)
    gun = Gun(screen)
    # pygame.sprite.Group()
    bullets = Group()
    inos = Group()
    controls.creat_ufos(screen, inos)
    running = True
    while running:
        if start_stats.run_game == False:
            break
        running = controls.events(screen, gun, bullets)
        gun.update()
        '''У групп есть методы update() и draw(). Метод update() группы вызывает методы update()
         всех входящих в нее объектов. А метод draw() выполняет метод blit(). '''
        bullets.update()
        controls.inos_update(inos)
        controls.update_screen(BLACK, screen, gun, bullets, inos, start_stats)


run()
pygame.quit()
