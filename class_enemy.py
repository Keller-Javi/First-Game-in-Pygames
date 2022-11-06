import pygame, sys
from pygame.locals import *
import math


size = 0.2

class class_enemy:
    _kill = False
    _move = True
    _time_to_damage = 0.7
    _timer = _time_to_damage

    def __init__(self, position, speed, life):
        self._img = pygame.image.load("Assets/Enemy.png") # Load and set the image of the enemy
        self._img = pygame.transform.scale(self._img, (int(318*size),int(294*size)))

        self._speed = speed
        self._position = position
        self._life = life

        self._img_rot = self._img
        self._rect = self._img_rot.get_rect()



    @property
    def rect(self):
        return self._rect


    @property
    def kill(self):
        return self._kill


    @property
    def life(self):
        return self._life
    @life.setter # Need to apply damago with a bullet 
    def life(self, value):
        self._life = value




    def draw(self, surface): # Draw enemy
        surface.blit(self._img_rot, self._rect)

    



    def update(self, position_of_player, player, dt):
        xp, yp = position_of_player[0] - self._position[0], position_of_player[1] - self._position[1]

        dist = math.hypot(xp, yp)

        dir_normalized = xp/dist, yp/dist

        if self._move:
            self._position[0] += dir_normalized[0]*self._speed # Movement of enemy
            self._position[1] += dir_normalized[1]*self._speed

        
        angle = 360 - math.atan2(yp,xp)*180/math.pi         # Rotation
        self._img_rot = pygame.transform.rotate(self._img, angle)
        self._rect = self._img_rot.get_rect()

        self._rect.center = self._position # Update position



        if self._life <= 0: # Set death state
            self._kill = True


        self._timer -= dt           # Destroy a bullet
    
        if self._rect.colliderect(player.rect):
            self._move = False
            if self._timer <= 0:
                player.life -= 1
                self._timer = self._time_to_damage

        else:
            self._move = True
