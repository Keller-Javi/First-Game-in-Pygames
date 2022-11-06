import pygame, sys
from pygame.locals import *
import math
from class_bullet import class_bullet


class class_player(pygame.sprite.Sprite):
    _pos = [200,200]
    _vect_dir = [0,0]
    _size = 100
    _bullets = []
    _time_to_shoot = 0.5
    _timer = _time_to_shoot
    _kill = False

    def __init__(self, size, life):
        self._img = pygame.image.load("Assets/Player.gif") # Load and set the image of the player 
        self._img = pygame.transform.scale(self._img, (int(250*size),int(213*size)))

        self._img_rot = self._img               #Set a copy of the original image
        self._rect = self._img_rot.get_rect()
        self._rect.center = self._pos
        self._life = life
    


    #                   Draw a player image on the screen

    def draw (self, surface):
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
        self._life  = value
    
    @property
    def kill(self):
        return self._kill



    #               Movement of the player

    def Movement (self, speed, width, height): # Update player actions
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

        self._rect.center = self._pos


        #           Check if the player exited the window

        if self._pos[0] > width+self._size: # If player exit the window in axis X
            self._pos[0] = -self._size
        elif self._pos[0] < -self._size:
            self._pos[0] = width+self._size

        if self._pos[1] > height+self._size: # If player exit the window in axis Y
            self._pos[1] = -self._size
        elif self._pos[1] < -self._size:
            self._pos[1] = height+self._size
        

        if self._life <= 0:
            self._kill = True




    #               Rotate player respectively to position of mouse

    def Rotation_Shoot(self, pos_of_mouse, bullet_speed, screen, dt, enemy_instances):
        xp, yp = pos_of_mouse[0] - self._pos[0], pos_of_mouse[1] - self._pos[1] # Vector of mouse relative to player

        mod = math.hypot(xp, yp)
        angle = 360 - math.atan2(yp,xp)*180/math.pi                 # Get angle of mouse relative to player

        self._img_rot = pygame.transform.rotate(self._img, angle)   # Set a rotation on a imagen 
        self._rect = self._img_rot.get_rect()
        self._rect.center = self._pos


        #           Instantiate a bullet
        self._timer -= dt

        if (pygame.mouse.get_pressed() == (1, 0, 0)) and self._timer <= 0:
            dir_normalized = (xp/math.hypot(xp, yp), yp/math.hypot(xp, yp))

            self._bullets.append(class_bullet(bullet_speed, angle, [self._pos[0],self._pos[1]], dir_normalized))

            self._timer = self._time_to_shoot
        

        for bullet in self._bullets:
            bullet.draw(screen, enemy_instances, dt)

            if bullet.destroy:
                self._bullets.remove(bullet)
