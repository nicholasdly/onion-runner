
from src.constants import *

import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.frame = 0
        self.walk = (
            pygame.image.load('src/graphics/player/player_walk1.png').convert_alpha(),
            pygame.image.load('src/graphics/player/player_walk2.png').convert_alpha(),
            pygame.image.load('src/graphics/player/player_walk3.png').convert_alpha(),
            pygame.image.load('src/graphics/player/player_walk4.png').convert_alpha(),
        )
        self.jump = pygame.image.load('src/graphics/player/player_jump.png').convert_alpha()
        self.death = pygame.image.load('src/graphics/player/player_death.png').convert_alpha()

        self.jump_sound = pygame.mixer.Sound('src/audio/jump.wav')

        self.image = self.walk[self.frame]
        self.rect = self.image.get_rect(midbottom=(100, GROUND_HEIGHT))

        self.velocity = 0
        self.gravity = 1

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= GROUND_HEIGHT:
            self.velocity = -20
            self.jump_sound.play()

    def physics(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity
        if self.rect.bottom >= GROUND_HEIGHT:
            self.rect.bottom = GROUND_HEIGHT
            self.velocity = 0

    def animate(self):
        if self.rect.bottom < GROUND_HEIGHT:
            self.image = self.jump
        else:
            self.frame += 0.13
            if self.frame >= len(self.walk):
                self.frame = 0
            self.image = self.walk[int(self.frame)]

    def update(self):
        self.input()
        self.physics()
        self.animate()

    def die(self):
        self.image = self.death

    def reset(self):
        self.velocity = 0
        self.rect.bottom = GROUND_HEIGHT
        