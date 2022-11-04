import pygame, sys
from pygame.locals import *

size = 0.03

class class_bullet:
    def __init__(self, speed, angle, pos_i, direction):
        self._speed = speed
        self._position = pos_i
        self._direction = direction

        self._img = pygame.image.load("Assets/Bullet.png") # Load and set the image of the player 
        self._img = pygame.transform.scale(self._img, (int(800*size),int(800*size)))
        self._img = pygame.transform.rotate(self._img, angle)

        self._rect = self._img.get_rect()




    def draw(self, surface):
        self.update()
        surface.blit(self._img, self._rect)




    def update(self):
        self._position[0] += self._direction[0]*self._speed
        self._position[1] += self._direction[1]*self._speed

        self._rect.center = self._position




