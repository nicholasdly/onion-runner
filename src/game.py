
from src.constants import *
from src.title import TitleBackground, TitleText, TitlePlay, TitlePause
from src.pause import PauseBackground, PauseText, PausePlay
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

    #
    # Game State
    #

    running = True  # Game active state (open, closed)
    state = 'menu'  # Game instance state (title menu, gameplay, pause menu)

    #
    # Audio
    #

    background_music = pygame.mixer.Sound('src/audio/music.wav')
    background_music.set_volume(0.3)
    background_music.play(loops=-1)

    collision_sound = pygame.mixer.Sound('src/audio/reset.wav')

    #
    # Sprites
    #

    title_menu = pygame.sprite.Group()
    title_menu.add(TitleBackground())
    title_menu.add(TitleText())
    title_menu.add(TitlePlay())
    title_menu.add(TitlePause())

    pause_menu = pygame.sprite.Group()
    pause_menu.add(PauseBackground())
    pause_menu.add(PauseText())
    pause_menu.add(PausePlay())

    background = pygame.sprite.Group()
    background.add(Background())
    
    ground = pygame.sprite.Group()
    ground.add(Ground())

    foliage = pygame.sprite.Group()
    
    player = pygame.sprite.GroupSingle()
    player.add(Player())

    enemies = pygame.sprite.Group()

    score = pygame.sprite.GroupSingle()
    score.add(Score())

    #
    # Gameplay Events
    #

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
            background.draw(screen)
            ground.draw(screen)
            player.draw(screen)
            title_menu.draw(screen)

            # Allows for infinitely scrolling ground
            if len(ground.sprites()) < 2:
                new_ground = Ground()
                new_ground.rect.left = ground.sprites()[0].rect.right
                ground.add(new_ground)

            ground.update()
            player.update()

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
                collision_sound.play()

        # Pause Menu State
        elif state == 'pause':

            background.draw(screen)
            ground.draw(screen)
            foliage.draw(screen)
            player.draw(screen)
            enemies.draw(screen)
            score.draw(screen)
            pause_menu.draw(screen)

        # Death Menu State
        elif state == 'death':
            pass

        # Invalid Game State
        else:
            raise AttributeError('Invalid game state!')

        # Event Loop
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if state == 'menu':

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    state = 'play'

            elif state == 'play':

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    state = 'pause'

                if event.type == spawn_enemy:
                    enemies.add(random.choice([
                        Slime(),
                        Pumpkin(),
                        Cactus(),
                        Radish()
                    ]))
                
                if event.type == spawn_tree:
                    foliage.add(Tree())
                
                if event.type == spawn_grass:
                    foliage.add(Grass())
            
            elif state == 'pause':
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    state = 'play'

            elif state == 'dead':
                pass

