import pygame
from bullet import Bullet

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
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.key_r = False
            elif event.key == pygame.K_LEFT:
                gun.key_l = False
    return True


def update_screen(bg_collor, screen, gun, bullets):
    screen.fill(bg_collor)
    for bullet in bullets.sprites():
        bullet.draw()
    gun.draw()
    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()
