import pygame
from pygame.locals import *
import random


class pools_blood:
    def __init__(self, position):
        self._img = pygame.image.load(
            "Assets/Blood/Blood-%s.png" % (str(random.randint(1, 3))))
        self._img = pygame.transform.scale(
            self._img, (int(100), int(100)))
        self._rect = self._img.get_rect()
        self._rect.center = position

    def draw(self, surface):
        surface.blit(self._img, self._rect)


class life_bar:
    def __init__(self):
        self._maxwidth = 200
        self._height = 30

    def draw(self, surface, width, progress):
        pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(
            width-self._maxwidth-50, 20, self._maxwidth, self._height))
        pygame.draw.rect(surface, (100, 255, 255), pygame.Rect(
            width-self._maxwidth-50, 20, self._maxwidth*progress, self._height))
