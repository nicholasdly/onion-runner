
from src.constants import *

import pygame

pygame.font.init()

class TitleBackground(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('src/graphics/misc/menu_background.png').convert()
        self.rect = self.image.get_rect(center=(469, 176))

class TitleText(pygame.sprite.Sprite):

    FONT = pygame.font.Font('src/font/PlayMeGames.ttf', 50)
    COLOR = '#202020'

    def __init__(self):
        super().__init__()
        self.image = self.FONT.render(GAME_TITLE, False, self.COLOR)
        self.rect = self.image.get_rect(center=(469, 140))

class TitleDescription(pygame.sprite.Sprite):

    FONT = pygame.font.Font('src/font/PlayMeGames.ttf', 35)
    TEXT = 'Press SPACE to play!'
    COLOR = '#202020'

    def __init__(self):
        super().__init__()
        self.image = self.FONT.render(self.TEXT, False, self.COLOR)
        self.rect = self.image.get_rect(center=(469, 210))