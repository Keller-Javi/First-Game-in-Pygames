import pygame, sys
from pygame.locals import *

size_of_screen = width, height = 640, 480

pygame.init()


"""     Screen    """
pygame.display.set_caption("Game XD")
screen = pygame.display.set_mode((size_of_screen))
background_color = (120,250,250)


"""     Variables used in game      """
color = (255,0,0)

speed = 0.1
pos = [100,100]
vect_dir = [0,0]

while True:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(background_color) # Set the background color

    pygame.draw.rect(screen, color, (pos[0], pos[1], 50, 50)) # rect(Donde se dibuja, color, (pos_x, pos_y, alto, ancho))

    if pygame.key.get_pressed()[K_w]: # Direction of rect in Y axis
        vect_dir[1] = -1
    elif pygame.key.get_pressed()[K_s]:
        vect_dir[1] = 1
    else:
        vect_dir[1] = 0
    
    if pygame.key.get_pressed()[K_a]: # Direction of rect in X axis
        vect_dir[0] = -1
    elif pygame.key.get_pressed()[K_d]:
        vect_dir[0] = 1
    else:
        vect_dir[0] = 0
    
    pos[0] += vect_dir[0]*speed # Apply the movemento to the position
    pos[1] += vect_dir[1]*speed
