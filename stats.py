import pygame.font


class Stats():
    """Stats games"""

    def __init__(self, screen):
        self.healf = 3
        self.run_game = True
        self.score = 0
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text_collor = 255, 193, 7
        self.font = pygame.font.Font('image/font.ttf', 30)
        self.image_score()
        self.image_half()

    def image_score(self):
        self.img_score = self.font.render(str(self.score), True, self.text_collor, (0, 0, 0))
        self.scor_rect = self.img_score.get_rect()
        self.scor_rect.right = self.screen_rect.right - 40
        self.scor_rect.top = 20

    def image_half(self):
        self.img_healf = self.font.render('Life : ' + str(self.healf), True, self.text_collor, (0, 0, 0))
        self.healf_rect = self.img_healf.get_rect()
        self.healf_rect.left = self.screen_rect.left + 20
        self.healf_rect.top = 20

    def show_stats(self):
        self.screen.blit(self.img_score, self.scor_rect)
        self.screen.blit(self.img_healf, self.healf_rect)
