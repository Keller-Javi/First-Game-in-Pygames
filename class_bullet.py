import pygame
from pygame.locals import *


class ClassBullet:
    def __init__(self, image, speed, angle, pos_i, direction):
        self._destroy = False
        self._time_of_destroy = 10
        self._timer = self._time_of_destroy

        self._speed = speed
        self._position = pos_i
        self._direction = direction

        # Load and set the image of the player
        self._img = image
        self._img = pygame.transform.rotate(self._img, angle)

        self._rect = self._img.get_rect()

    @property
    def destroy(self):
        return self._destroy
    
    @property
    def position(self):
        return self._position

    def draw(self, surface, enemy, dt):  # Update and draw a bullet
        self.update(enemy, dt)
        surface.blit(self._img, self._rect)

    def update(self, enemies, dt):
        self._position[0] += self._direction[0] * \
            self._speed  # direction of shoot
        self._position[1] += self._direction[1]*self._speed

        self._rect.center = self._position

        for instance in enemies:       # Bullet collide with any enemy
            if instance and self._rect.colliderect(instance.rect):
                instance.life -= 1
                self._destroy = True

        self._timer -= dt           # Destroy a bullet
        if self._timer <= 0:
            self._destroy = True
