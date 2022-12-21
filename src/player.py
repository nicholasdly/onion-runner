
from src.constants import *

import pygame

class Player(pygame.sprite.Sprite):

    STAND_HEIGHT = 354

    def __init__(self):
        super().__init__()

        self.walking_index = 0
        self.player_walk = [
            pygame.image.load('src/graphics/player/player_walk1.png').convert_alpha(),
            pygame.image.load('src/graphics/player/player_walk2.png').convert_alpha(),
            pygame.image.load('src/graphics/player/player_walk3.png').convert_alpha(),
            pygame.image.load('src/graphics/player/player_walk4.png').convert_alpha(),
        ]
        self.player_jump = pygame.image.load('src/graphics/player/player_jump.png').convert_alpha()

        self.image = self.player_walk[self.walking_index]
        self.rect = self.image.get_rect(midbottom=(100, self.STAND_HEIGHT))

        self.velocity = 0
        self.gravity = 1

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= self.STAND_HEIGHT:
            self.velocity = -20

    def physics(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity
        if self.rect.bottom >= self.STAND_HEIGHT:
            self.rect.bottom = self.STAND_HEIGHT
            self.velocity = 0

    def animate(self):
        if self.rect.bottom < self.STAND_HEIGHT:
            self.image = self.player_jump
        else:
            self.walking_index += 0.1
            if self.walking_index >= len(self.player_walk):
                self.walking_index = 0
            self.image = self.player_walk[int(self.walking_index)]

    def update(self):
        self.input()
        self.physics()
        self.animate()
        