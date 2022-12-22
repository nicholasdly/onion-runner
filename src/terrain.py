
from src.constants import *

import pygame
import random

class Background(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 1
        self.image = pygame.image.load('./src/graphics/terrain/background.png').convert()
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect()

class Ground(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 3
        self.image = pygame.image.load('./src/graphics/terrain/ground.png').convert()
        self.rect = self.image.get_rect(top=350)

    def movement(self):
        self.rect.x -= self.velocity

    def destroy(self):
        if self.rect.right <= 0:
            self.kill()

    def update(self):
        self.movement()
        self.destroy()

class Foliage(pygame.sprite.Sprite):

    SPAWN_RANGE = (SCREEN_WIDTH + 100, SCREEN_WIDTH + 300)

    def __init__(self):
        super().__init__()
        self.velocity = 3

    def movement(self):
        pass

    def destroy(self):
        pass

    def update(self):
        self.movement()
        self.destroy()

class Grass(Foliage):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('src/graphics/terrain/grass.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(random.randint(*self.SPAWN_RANGE), GROUND_HEIGHT))
    
    def movement(self):
        self.rect.x -= self.velocity

    def destroy(self):
        if self.rect.right < 0:
            self.kill()

class Tree(Foliage):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('src/graphics/terrain/tree.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(random.randint(*self.SPAWN_RANGE), GROUND_HEIGHT))
    
    def movement(self):
        self.rect.x -= self.velocity

    def destroy(self):
        if self.rect.right < 0:
            self.kill()
