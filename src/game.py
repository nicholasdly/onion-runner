
from src.constants import *
from src.terrain import Background, Ground, Grass, Tree
from src.player import Player
from src.enemy import Slime, Pumpkin, Cactus, Radish
from src.score import Score

import pygame
import random

def colliding(sprite: pygame.sprite, sprite_group: pygame.sprite.Group) -> bool:
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

    background = pygame.sprite.GroupSingle()
    background.add(Background())
    
    ground = pygame.sprite.Group()
    ground.add(Ground())

    foliage = pygame.sprite.Group()
    
    player = pygame.sprite.GroupSingle()
    player.add(Player())

    enemies = pygame.sprite.Group()

    score = pygame.sprite.GroupSingle()
    score.add(Score())

    spawn_enemy = pygame.USEREVENT + 1
    pygame.time.set_timer(spawn_enemy, ENEMY_SPAWN_RATE)

    spawn_grass = pygame.USEREVENT + 2
    pygame.time.set_timer(spawn_grass, GRASS_SPAWN_RATE)

    spawn_tree = pygame.USEREVENT + 3
    pygame.time.set_timer(spawn_tree, TREE_SPAWN_RATE)

    while running:
        pygame.display.update()
        clock.tick(FPS)

        # Main Menu State
        if state == 'menu':
            pass

        # Gameplay State
        elif state == 'play':

            background.draw(screen)
            ground.draw(screen)
            foliage.draw(screen)
            player.draw(screen)
            enemies.draw(screen)
            score.draw(screen)

            # Allows for infinitely scrolling ground
            if len(ground.sprites()) < 2:
                new_ground = Ground()
                new_ground.rect.left = ground.sprites()[0].rect.right
                ground.add(new_ground)
            
            ground.update()
            foliage.update()
            player.update()
            enemies.update()
            score.update()

            # Check for player-enemy collisions
            if colliding(player.sprite, enemies):
                score.sprite.reset()
                enemies.empty()

        # Pause Menu State
        elif state == 'pause':
            pass

        # Event Loop
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if state == 'play' and event.type == spawn_enemy:
                enemies.add(random.choice([
                    Slime(),
                    Pumpkin(),
                    Cactus(),
                    Radish()
                ]))
            
            if state == 'play' and event.type == spawn_tree:
                foliage.add(Tree())
            
            if state == 'play' and event.type == spawn_grass:
                foliage.add(Grass())

