
import pygame

class Background(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('./src/graphics/terrain/background.png').convert()
        self.image = pygame.transform.scale(self.image, (800, 400))
        self.rect = self.image.get_rect()
