
from src.constants import *

import pygame

pygame.font.init()

class DeathBackground(pygame.sprite.Sprite):

    COLOR = '#ff4040'
    ALPHA = 128

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.image.fill(self.COLOR)
        self.image.set_alpha(self.ALPHA)
        self.rect = self.image.get_rect()

class DeathText(pygame.sprite.Sprite):

    FONT = pygame.font.Font('src/font/PlayMeGames.ttf', 60)
    TEXT = 'GAME OVER'
    COLOR = '#202020'

    def __init__(self):
        super().__init__()
        self.image = self.FONT.render(self.TEXT, False, self.COLOR)
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, 190))

class DeathPlay(pygame.sprite.Sprite):

    FONT = pygame.font.Font('src/font/PlayMeGames.ttf', 35)
    TEXT = 'Press ESC to restart!'
    COLOR = '#202020'

    def __init__(self):
        super().__init__()
        self.image = self.FONT.render(self.TEXT, False, self.COLOR)
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, 240))