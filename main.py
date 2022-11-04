import pygame, sys
from pygame.locals import *
from class_player import class_player




pygame.init()

"""     Screen    """
FPS = 60
FramePerSec = pygame.time.Clock()
pygame.display.set_caption("Game XD")
size_of_screen = width, height = 1280, 720
screen = pygame.display.set_mode((size_of_screen))
background_color = (50,250,30)
clock = pygame.time.Clock()


"""     Variables used in game      """
size_of_player = 0.4
speed = 4

bullet_speed = 20

player = class_player(size_of_player)



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    player.draw(screen)                             # Draw the player
    player.Movement(speed, width, height)           # Update movemento of the player and if exited display

    dt = clock.tick(FPS) / 1000                      # Need this for create an a timer of bullets
    player.Rotation_Shoot(pygame.mouse.get_pos(), bullet_speed, screen, dt)
    


    pygame.display.update() 
    FramePerSec.tick(FPS)
    screen.fill(background_color)                       # Set the background color
