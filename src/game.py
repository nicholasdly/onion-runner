
from src.constants import *
from src.background import Background
from src.ground import Ground
from src.player import Player

import pygame

class Game:

    GAME_TITLE = 'Onion Runner'
    FPS = 60

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(self.GAME_TITLE)

        running = True
        screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT),
            flags=pygame.SCALED,
            vsync=1
        )
        clock = pygame.time.Clock()

        terrain = pygame.sprite.Group()
        terrain.add(Background())
        terrain.add(Ground())
        
        player = pygame.sprite.GroupSingle()
        player.add(Player())

        while running:
            pygame.display.update()
            clock.tick(self.FPS)

            terrain.draw(screen)
            player.draw(screen)

            player.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
