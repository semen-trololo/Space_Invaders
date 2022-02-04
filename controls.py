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
                # Создаем обьекты пули и добовляем его в список
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
    # Отрисовываем все спрайты пуль
    for bullet in bullets.sprites():
        bullet.draw()
    gun.draw()
    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()
