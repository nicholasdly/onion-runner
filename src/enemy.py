
from src.constants import *

import pygame
import random

class Enemy(pygame.sprite.Sprite):

    SPAWN_RANGE = (SCREEN_WIDTH + 100, SCREEN_WIDTH + 300)

    def __init__(self):
        super().__init__()
        self.velocity = 6

    def animate(self):
        pass

    def movement(self):
        pass

    def destroy(self):
        pass

    def update(self):
        self.animate()
        self.movement()
        self.destroy()

class Slime(Enemy):

    def __init__(self):
        super().__init__()
        self.frame = 0
        self.walk = (
            pygame.image.load('src/graphics/slime/slime_walk1.png').convert_alpha(),
            pygame.image.load('src/graphics/slime/slime_walk2.png').convert_alpha()
        )

        self.image = self.walk[self.frame]
        self.rect = self.image.get_rect(midbottom=(random.randint(*self.SPAWN_RANGE), GROUND_HEIGHT))

    def animate(self):
        self.frame += 0.1
        if self.frame >= len(self.walk):
            self.frame = 0
        self.image = self.walk[int(self.frame)]

    def movement(self):
        self.rect.x -= self.velocity

    def destroy(self):
        if self.rect.right < 0:
            self.kill()

class Pumpkin(Enemy):

    def __init__(self):
        super().__init__()
        self.frame = 0
        self.walk = (
            pygame.image.load('src/graphics/pumpkin/pumpkin_walk1.png').convert_alpha(),
            pygame.image.load('src/graphics/pumpkin/pumpkin_walk2.png').convert_alpha(),
            pygame.image.load('src/graphics/pumpkin/pumpkin_walk3.png').convert_alpha(),
            pygame.image.load('src/graphics/pumpkin/pumpkin_walk2.png').convert_alpha(),
        )

        self.image = self.walk[self.frame]
        self.rect = self.image.get_rect(midbottom=(random.randint(*self.SPAWN_RANGE), GROUND_HEIGHT))

    def animate(self):
        self.frame += 0.075
        if self.frame >= len(self.walk):
            self.frame = 0
        self.image = self.walk[int(self.frame)]
        self.rect.bottom = GROUND_HEIGHT

    def movement(self):
        self.rect.x -= self.velocity

    def destroy(self):
        if self.rect.right < 0:
            self.kill()

class Cactus(Enemy):

    def __init__(self):
        super().__init__()
        self.frame = 0
        self.walk = (
            pygame.image.load('src/graphics/cactus/cactus_walk1.png').convert_alpha(),
            pygame.image.load('src/graphics/cactus/cactus_walk2.png').convert_alpha(),
            pygame.image.load('src/graphics/cactus/cactus_walk3.png').convert_alpha(),
            pygame.image.load('src/graphics/cactus/cactus_walk2.png').convert_alpha()
        )

        self.image = self.walk[self.frame]
        self.rect = self.image.get_rect(midbottom=(random.randint(*self.SPAWN_RANGE), GROUND_HEIGHT))

    def animate(self):
        self.frame += 0.075
        if self.frame >= len(self.walk):
            self.frame = 0
        self.image = self.walk[int(self.frame)]
        self.rect.bottom = GROUND_HEIGHT

    def movement(self):
        self.rect.x -= self.velocity

    def destroy(self):
        if self.rect.right < 0:
            self.kill()

class Radish(Enemy):

    def __init__(self):
        super().__init__()
        self.frame = 0
        self.walk = (
            pygame.image.load('src/graphics/radish/radish_fly1.png').convert_alpha(),
            pygame.image.load('src/graphics/radish/radish_fly2.png').convert_alpha()
        )

        self.image = self.walk[self.frame]
        self.rect = self.image.get_rect(midbottom=(random.randint(*self.SPAWN_RANGE), SKY_HEIGHT))

    def animate(self):
        self.frame += 0.1
        if self.frame >= len(self.walk):
            self.frame = 0
        self.image = self.walk[int(self.frame)]
        self.rect.bottom = SKY_HEIGHT

    def movement(self):
        self.rect.x -= self.velocity

    def destroy(self):
        if self.rect.right < 0:
            self.kill()