import pygame, sys
from pygame.locals import *

class class_player:
    _pos = [100,100]
    _vect_dir = [0,0]

    def __init__(self, size):
        self._size = size

    def player_Draw(self):  #color, (pos_x, pos_y, alto, ancho)
        return (self._pos[0], self._pos[1], self._size, self._size)

    def movement (self, speed):
        if pygame.key.get_pressed()[K_w]: # Direction of rect in Y axis
            self._vect_dir[1] = -1
        elif pygame.key.get_pressed()[K_s]:
            self._vect_dir[1] = 1
        else:
            self._vect_dir[1] = 0
    
        if pygame.key.get_pressed()[K_a]: # Direction of rect in X axis
            self._vect_dir[0] = -1
        elif pygame.key.get_pressed()[K_d]:
            self._vect_dir[0] = 1
        else:
            self._vect_dir[0] = 0
        
        self._pos[0] += self._vect_dir[0]*speed # Apply the movemento to the position
        self._pos[1] += self._vect_dir[1]*speed
    

    def exit_window(self, width, height):
        if self._pos[0] > width+self._size: # If player exit the window in axis X
            self._pos[0] = -self._size
        elif self._pos[0] < -self._size:
            self._pos[0] = width+self._size

        if self._pos[1] > height+self._size: # If player exit the window in axis Y
            self._pos[1] = -self._size
        elif self._pos[1] < -self._size:
            self._pos[1] = height+self._size