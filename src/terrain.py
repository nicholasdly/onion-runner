
from src.constants import *

import pygame

class Background(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('./src/graphics/terrain/background.png').convert()
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect()

class Ground(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('./src/graphics/terrain/ground.png').convert()
        self.rect = self.image.get_rect(top=350)
