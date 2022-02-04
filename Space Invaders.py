import pygame
import controls
from gun import Gun
from pygame.sprite import Group

WIDTH = 800  # ширина игрового окна
HEIGHT = 600 # высота игрового окна
BLACK = (0, 0, 0)


def run():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Invaders")
    game_loop(screen)


def game_loop(screen):
    gun = Gun(screen)
    bullets = Group()
    running = True
    while running:
        running = controls.events(screen, gun, bullets)
        gun.update()
        bullets.update()
        controls.update_screen(BLACK, screen, gun, bullets)


run()
pygame.quit()
