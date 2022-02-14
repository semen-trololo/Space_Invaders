import pygame


class Ufo(pygame.sprite.Sprite):
    """
    Класс пришельцев
    """
    def __init__(self, screen, numer):
        super(Ufo, self).__init__()
        self.screen = screen
        tmp = ['image/ufo_1.png', 'image/ufo_2.png', 'image/ufo_3.png']
        self.image = pygame.image.load(tmp[numer])
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.speed = 0.08

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y
