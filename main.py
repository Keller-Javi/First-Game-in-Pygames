import pygame, sys

from pygame.locals import *

from class_player import class_player




pygame.init()

"""     Screen    """
pygame.display.set_caption("Game XD")
size_of_screen = width, height = 640, 480
screen = pygame.display.set_mode((size_of_screen))
background_color = (120,250,250)


"""     Variables used in game      """
color = (255,0,0)
size_of_player = 20
speed = 0.05


player = class_player(size_of_player)


while True:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(background_color) # Set the background color


    pygame.draw.rect(screen, color, player.player_Draw()) # Draw the player                             rect(Donde se dibuja, color, (pos_x, pos_y, alto, ancho))
    player.movement(speed)              # Call a movement of the player
    player.exit_window(width, height)   # Check if the player exited the window
    
    """if pygame.mouse.get_pressed() == (1,0,0):
        print("Fire!")
    
    print(pygame.mouse.get_pos())"""