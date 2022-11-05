import pygame, sys
from pygame.locals import *

size = 0.02

class class_bullet:
    _destroy = False
    _time_of_destroy = 15
    _timer = _time_of_destroy


    def __init__(self, speed, angle, pos_i, direction):
        self._speed = speed
        self._position = pos_i
        self._direction = direction

        self._img = pygame.image.load("Assets/Bullet.png") # Load and set the image of the player 
        self._img = pygame.transform.scale(self._img, (int(800*size),int(800*size)))
        self._img = pygame.transform.rotate(self._img, angle)

        self._rect = self._img.get_rect()


    @property
    def destroy(self):
        return self._destroy

    def draw(self, surface, enemy, dt): # Update and draw a bullet
        self.update(enemy, dt)
        surface.blit(self._img, self._rect)




    def update(self, enemies, dt):
        self._position[0] += self._direction[0]*self._speed # direction of shoot
        self._position[1] += self._direction[1]*self._speed

        self._rect.center = self._position


        for enemy in enemies:       # Bullet collide with any enemy
            if self._rect.colliderect(enemy.rect):
                enemy.life -= 1
                self._destroy = True
        

        self._timer -= dt           # Destroy a bullet
        if self._timer <= 0:
            self._destroy = True





