import pygame.font


class Stats():
    """Stats games"""

    def __init__(self, screen):
        self.round = 1
        self.healf = 3
        self.run_game = True
        self.score = 0
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image_score()
        self.image_half()
        self.image_geme_over()

    def image_score(self):
        self.font = pygame.font.Font('image/font.ttf', 26)
        self.text_collor = 255, 193, 7
        self.img_score = self.font.render(str(self.score), True, self.text_collor, (0, 0, 0))
        self.scor_rect = self.img_score.get_rect()
        self.scor_rect.right = self.screen_rect.right - 40
        self.scor_rect.top = 20

    def image_half(self):
        self.font = pygame.font.Font('image/font.ttf', 26)
        self.text_collor = 255, 193, 7
        self.img_healf = self.font.render('Life : ' + str(self.healf), True, self.text_collor, (0, 0, 0))
        self.healf_rect = self.img_healf.get_rect()
        self.healf_rect.left = self.screen_rect.left + 20
        self.healf_rect.top = 20

    def image_geme_over(self):
        self.font = pygame.font.Font('image/font.ttf', 60)
        self.text_collor = 255, 193, 7
        self.img_game_over = self.font.render('GAME OVER!', True, self.text_collor, (255, 0, 0))
        self.game_over_rect = self.img_game_over.get_rect()
        self.game_over_rect.center = self.screen_rect.center

    def image_round(self):
        self.font = pygame.font.Font('image/font.ttf', 60)
        self.text_collor = 255, 193, 7
        self.img_round = self.font.render(f' ROUND {self.round} ', True, self.text_collor, (255, 0, 0))
        self.roud_rect = self.img_round.get_rect()
        self.roud_rect.center = self.screen_rect.center

    def show_stats(self):
        self.screen.blit(self.img_score, self.scor_rect)
        self.screen.blit(self.img_healf, self.healf_rect)

    def show_game_over(self):
        self.screen.blit(self.img_game_over, self.game_over_rect)

    def show_round(self):
        self.screen.blit(self.img_round, self.roud_rect)
