import pygame
from pygame.locals import *
import math
from class_bullet import ClassBullet


size = 0.3
bullet_img = pygame.image.load("Assets/Bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (int(730*0.02), int(172*0.02)))


class ClassPlayer(pygame.sprite.Sprite):
    def __init__(self, life):
        self._pos = [200, 200]
        self._vect_dir = [0, 0]
        self._size = 100
        self._time_to_shoot = 0.5
        self._timer = self._time_to_shoot
        self._death = False
        self.kills = 0

        # Load and set the image of the player
        self._img = pygame.image.load("Assets/Player.gif")
        self._img = pygame.transform.scale(
            self._img, (int(194*size), int(147*size)))

        self._img_rot = self._img  # Set a copy of the original image
        self._rect = self._img_rot.get_rect()
        self._rect.center = self._pos
        self._life = life

    #                   Draw a player image on the screen

    def draw(self, surface):
        surface.blit(self._img_rot, self._rect)

    #                   Return position of the player

    @property
    def position(self):
        return self._pos

    @property
    def rect(self):
        return self._rect

    @property
    def life(self):
        return self._life

    @life.setter
    def life(self, value):
        self._life = value

    @property
    def death(self):
        return self._death

    @property
    def kills(self):
        return self._kills

    @kills.setter
    def kills(self, value):
        self._kills = value

    #               Movement of the player

    def Movement(self, speed):  # Update player actions
        if pygame.key.get_pressed()[K_w]:  # Direction of rect in Y axis
            self._vect_dir[1] = -1
        elif pygame.key.get_pressed()[K_s]:
            self._vect_dir[1] = 1
        else:
            self._vect_dir[1] = 0

        if pygame.key.get_pressed()[K_a]:  # Direction of rect in X axis
            self._vect_dir[0] = -1
        elif pygame.key.get_pressed()[K_d]:
            self._vect_dir[0] = 1
        else:
            self._vect_dir[0] = 0

        # Apply the movemento to the position
        self._pos[0] += self._vect_dir[0]*speed
        self._pos[1] += self._vect_dir[1]*speed

        self._rect.center = self._pos

        if self._life <= 0:
            self._death = True

    #               Rotate player respectively to position of mouse

    def Rotation_Shoot(self, pos_of_mouse, bullet_speed, dt, bullet_list):
        # Vector of mouse relative to player
        xp, yp = pos_of_mouse[0] - self._pos[0], pos_of_mouse[1] - self._pos[1]

        # Get angle of mouse relative to player
        angle = 360 - math.atan2(yp, xp)*180/math.pi

        self._img_rot = pygame.transform.rotate(
            self._img, angle)   # Set a rotation on a imagen
        self._rect = self._img_rot.get_rect()
        self._rect.center = self._pos

        #           Instantiate a bullet
        self._timer -= dt

        if (pygame.mouse.get_pressed() == (1, 0, 0)) and self._timer <= 0:
            dir_normalized = (xp/math.hypot(xp, yp), yp/math.hypot(xp, yp))

            bullet_list.append(ClassBullet(
                bullet_img, bullet_speed, angle, self._pos.copy(), dir_normalized))

            self._timer = self._time_to_shoot
