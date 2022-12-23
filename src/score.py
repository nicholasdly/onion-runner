
from src.constants import *

import pygame

pygame.font.init()

class Score(pygame.sprite.Sprite):

    FONT = pygame.font.Font('src/font/PlayMeGames.ttf', 35)
    TEXT_COLOR = '#202020'

    def __init__(self):
        super().__init__()
        self.score = 0
        self.image = self.FONT.render(f'Score: {int(self.score)}', False, self.TEXT_COLOR)
        self.rect = self.image.get_rect(topleft = (15, 15))

    def update(self):
        self.score += 0.1
        self.image = self.FONT.render(f'Score: {int(self.score)}', False, self.TEXT_COLOR)

    def reset(self):
        self.score = 0