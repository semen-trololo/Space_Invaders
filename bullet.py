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
        self.rect = pygame.Rect(0, 0, 4, 12)
        self.color = 255, 193, 7
        self.speed = 2.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """
        Update Y position buller
        Этот метод следует переопределить в производном от Sprite классе.
        Для работы с групами спрайтов.
        :return:
        """
        self.y -= self.speed
        if self.y >= 0:
            self.rect.y = self.y
        else:
            self.kill()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
