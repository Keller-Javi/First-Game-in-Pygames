import pygame
import sys
import pygame_gui
from pygame.locals import *
import random

from class_player import class_player
from class_enemy import class_enemy


pygame.init()

"""     Screen    """
FPS = 60
FramePerSec = pygame.time.Clock()
pygame.display.set_caption("Game XD")
size_of_screen = width, height = 1280, 720
screen = pygame.display.set_mode((size_of_screen))
background_color = (50, 150, 30)
clock = pygame.time.Clock()

"""     Layout      """
manager_restart = pygame_gui.UIManager((width, height))

restart_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((width/2.2, height/2.2), (100, 50)),
    text='Restart',
    manager=manager_restart)


font = pygame.font.SysFont(None, 30)

"""     Variables used in game      """
life_of_player = 5
speed = 4
bullet_speed = 20

player = class_player(life_of_player)


life_of_enemy = 3
speed_of_enemy = 1.5
count_enemies = 0
enemies = []

while True:
    # Need this for create an a timers
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == restart_button:
                player = class_player(life_of_player)

        manager_restart.process_events(event)

    if player:
        player.draw(screen)                             # Draw the player
        # Update movemento of the player and if exited display
        player.Movement(speed, width, height)

        # call update of shots an rotatio of the player
        player.Rotation_Shoot(pygame.mouse.get_pos(),
                              bullet_speed, screen, dt, enemies)

        if player.death:
            player = None
            continue

        while count_enemies < 4:  # Create N enemies, if is necessary
            point = [random.randint(0, width), random.randint(
                0, height)]  # random point for each enemy
            enemies.append(class_enemy(point, speed_of_enemy,
                                       life_of_enemy))  # Create enemy
            count_enemies += 1

        for enemy in enemies:  # Update all enemy classes
            enemy.update(player, dt)
            enemy.draw(screen)

            if enemy.kill:
                enemies.remove(enemy)
                count_enemies -= 1
                player.kills += 1

        img = font.render('Kills: ' + str(player.kills), True, (255, 255, 255))
        screen.blit(img, (20, 20))

    else:  # if player not exists, draw ui to restart
        manager_restart.update(dt)
        manager_restart.draw_ui(screen)
    pygame.display.update()
    FramePerSec.tick(FPS)
    # Set the background color
    screen.fill(background_color)
