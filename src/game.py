
from src.constants import *
from src.terrain import Background, Ground
from src.player import Player
from src.enemy import Slime, Pumpkin, Cactus, Radish

import pygame
import random

def has_collided(sprite: pygame.sprite, sprite_group: pygame.sprite.Group):
    if pygame.sprite.spritecollide(sprite, sprite_group, False):
        return True
    return False

def game():
    pygame.init()
    pygame.display.set_caption(GAME_TITLE)

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT),
        flags=pygame.SCALED,
        vsync=1
    )

    running = True
    state = 'play'

    terrain = pygame.sprite.Group()
    terrain.add(Background())
    terrain.add(Ground())
    
    player = pygame.sprite.GroupSingle()
    player.add(Player())

    enemies = pygame.sprite.Group()

    spawn_enemy = pygame.USEREVENT + 1
    pygame.time.set_timer(spawn_enemy, SPAWN_RATE)

    while running:
        pygame.display.update()
        clock.tick(FPS)

        terrain.draw(screen)
        player.draw(screen)
        enemies.draw(screen)

        player.update()
        enemies.update()

        if state == 'play':
            if has_collided(player.sprite, enemies):
                print('collision')
                enemies.empty()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if state == 'play':
                if event.type == spawn_enemy:
                    enemies.add(random.choice([
                        Slime(),
                        Pumpkin(),
                        Cactus(),
                        Radish()
                    ]))
