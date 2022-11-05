import pygame, sys
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
background_color = (50,150,30)
clock = pygame.time.Clock()


"""     Variables used in game      """
size_of_player = 0.3
speed = 4
bullet_speed = 20
player = class_player(size_of_player)


speed_of_enemy = 1.5
count_enemies = 0
enemies = []



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    player.draw(screen)                             # Draw the player
    player.Movement(speed, width, height)           # Update movemento of the player and if exited display

    dt = clock.tick(FPS) / 1000                      # Need this for create an a timer of bullets
    player.Rotation_Shoot(pygame.mouse.get_pos(), bullet_speed, screen, dt, enemies) # call update of shots an rotatio of the player
    



    while count_enemies < 2: # Create N enemies, if is necessary 
        point = [random.randint(0, width), random.randint(0, height)] # random point for each enemy
        enemies.append(class_enemy(point, speed_of_enemy)) # Create enemy
        count_enemies += 1
    
    for enemy in enemies: # Update all enemy classes
        enemy.update(player.position)
        enemy.draw(screen)

        if enemy.kill:
            enemies.remove(enemy)
            count_enemies -= 1




    pygame.display.update() 
    FramePerSec.tick(FPS)
    screen.fill(background_color)                       # Set the background color
