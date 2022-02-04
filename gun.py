import pygame

class Gun():

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('image/pixil-frame.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Флаг нажатия клавиши для движения пушки
        self.key_r = False
        self.key_l = False

    def draw(self):
        """
        Draw Gun
        :return: None
        """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """
        Update x position gun
        :return: None
        """
        if self.key_r and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.key_l and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 1
