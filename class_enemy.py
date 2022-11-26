import pygame
from pygame.locals import *
from pygame import Vector2
import math

from class_bullet import ClassBullet


bullet_img = pygame.image.load("Assets/Stone.png")


class ClassEnemy:
    def __init__(self, position, speed, life):
        self._kill = False
        self._move = True
        self._time_to_damage = 0.7
        self._timer = self._time_to_damage

        self._type = 'N'  # If is a normal enemy type is = 'N', is a range enemy type is = 'R'

        self._vec_player = Vector2(0, 0)
        self._angle_to_player = 0

        # Load and set the image of the enemy
        self._img = pygame.image.load("Assets/Enemy.png")

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

    @life.setter  # Need to apply damago with a bullet
    def life(self, value):
        self._life = value

    @property
    def position(self):
        return self._position

    @property
    def type(self):
        return self._type

    def draw(self, surface):  # Draw enemy
        surface.blit(self._img_rot, self._rect)

    def update(self, player, dt):
        self._vec_player = player.position[0] - \
            self._position[0], player.position[1] - self._position[1]

        dir_normalized = pygame.math.Vector2.normalize(
            Vector2(self._vec_player))

        if self._move:
            self._position[0] += dir_normalized[0] * \
                self._speed  # Movement of enemy
            self._position[1] += dir_normalized[1]*self._speed

        self._angle_to_player = 360 - \
            math.atan2(
                self._vec_player[1], self._vec_player[0])*180/math.pi         # Rotation
        self._img_rot = pygame.transform.rotate(
            self._img, self._angle_to_player)
        self._rect = self._img_rot.get_rect()

        self._rect.center = self._position  # Update position

        if self._life <= 0:  # Set death state
            self._kill = True


class Enemy(ClassEnemy):
    def update(self, player, dt):
        super().update(player, dt)
        self._timer -= dt

        if self._rect.colliderect(player.rect):
            self._move = False
            if self._timer <= 0:
                player.life -= 1
                self._timer = self._time_to_damage
        else:
            self._move = True


class EnemyRange(ClassEnemy):
    def __init__(self, position, speed, life):
        super().__init__(position, speed, life)
        self._speed_projectil = 5
        self._type = 'R'

    def update(self, player, dt, bullet_list):
        super().update(player, dt)

        self._timer -= dt

        if math.hypot(self._vec_player[0], self._vec_player[1]) <= 200:
            self._move = False
            if self._timer <= 0:
                self._timer = self._time_to_damage
                direction = pygame.math.Vector2.normalize(
                    Vector2(self._vec_player))

                bullet_list.append(ClassBullet(bullet_img, self._speed_projectil,
                                   self._angle_to_player, self._position.copy(), direction))
        else:
            self._move = True
