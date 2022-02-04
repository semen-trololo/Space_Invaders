import pygame
from gun import Gun

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
    running = True
    while running:
        for event in pygame.event.get():
            # проверить закрытие окна
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLACK)
        gun.draw()
        # после отрисовки всего, переворачиваем экран
        pygame.display.flip()

run()
