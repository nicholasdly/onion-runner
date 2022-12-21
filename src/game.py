
from src.background import Background
from src.ground import Ground
from src.player import Player

import pygame

class Game:

    SIZE = (800, 400)
    TITLE = 'Onion Runner'

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(self.TITLE)

        running = True
        screen = pygame.display.set_mode(self.SIZE)
        clock = pygame.time.Clock()

        # player = pygame.sprite.GroupSingle()
        # player.add(Player())
        # player.draw(screen)

        terrain = pygame.sprite.Group()
        terrain.add(Background())
        terrain.add(Ground())
        terrain.draw(screen)

        while running:
            pygame.display.update()
            clock.tick(60)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
