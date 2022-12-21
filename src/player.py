
import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('./src/graphics/player1.png').convert_alpha()
        self.image = pygame.transform.scale(
            self.image,
            (self.image.get_width() * 4, self.image.get_height() * 4)
        )
        self.rect = self.image.get_rect(center=(400, 200))

    def update(self):
        pass
