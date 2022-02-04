import pygame

# Наследуем методы от родительского класса pygame.sprite.Sprite


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """
        задаем позицию пули на экране с привязкой к Gun
        :param screen:
        :param gun:
        """
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 10)
        self.color = 255, 193, 7
        self.speed = 1
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = self.rect.y

    def update(self):
        """
        Update y position buller
        :return:
        """
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
