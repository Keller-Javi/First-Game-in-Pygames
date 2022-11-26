import pygame
from pygame.locals import *
import random


class PoolsBlood:
    def __init__(self, position):
        self._img = pygame.image.load(
            "Assets/Blood/Blood-%s.png" % (str(random.randint(1, 3))))
        self._rect = self._img.get_rect()
        self._rect.center = position

    def draw(self, surface):
        surface.blit(self._img, self._rect)


class LifeBar:
    def __init__(self):
        self._maxwidth = 200
        self._height = 30

    def draw(self, surface, width, progress):
        pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(
            width-self._maxwidth-50, 20, self._maxwidth, self._height))
        pygame.draw.rect(surface, (100, 255, 255), pygame.Rect(
            width-self._maxwidth-50, 20, self._maxwidth*progress, self._height))

class Hit:
    def __init__(self, time_hit, position):
        self._timer_hit = time_hit
        self._hit_effect = pygame.image.load("Assets/hit.png")
        self._rect = self._hit_effect.get_rect()
        self._rect.center = position
        self.destroy = False
    
    def draw(self, surface, dt):
        self._timer_hit -= dt

        if self._timer_hit <= 0:
            self.destroy = True

        surface.blit(self._hit_effect, self._rect)