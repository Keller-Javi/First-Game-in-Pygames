import pygame
import sys
import pygame_gui
from pygame.locals import *
import random

from class_player import ClassPlayer
from class_enemy import Enemy, EnemyRange
from small_classes import LifeBar, PoolsBlood, Hit


pygame.init()

"""     Screen    """
FPS = 60
FramePerSec = pygame.time.Clock()
pygame.display.set_caption("Game XD")
size_of_screen = width, height = 1280, 720
screen = pygame.display.set_mode((size_of_screen))
background_color = (50, 150, 30)
clock = pygame.time.Clock()

"""     Layout      """
manager_restart = pygame_gui.UIManager((width, height))

restart_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((width/2.2, height/2.2), (100, 50)),
    text='Restart',
    manager=manager_restart)


font = pygame.font.SysFont(None, 30)
font2 = pygame.font.SysFont(None, 60)

lbar = LifeBar()


"""     Variables used in game      """
life_of_player = 10
speed = 4
bullet_speed = 20
bullets_of_player = []
kills = 0

player = ClassPlayer(life_of_player)


life_of_enemy = 3
speed_of_enemy = 1
count_enemies = 0
enemies = []
list_pools_blood = []
timer_to_respawn = 0
amount_enemies = 7

bullets_of_enemies = []

time_hit = 0.1
hits = []

write_score = False

while True:
    # Need this for create an a timers
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == restart_button:
                player = ClassPlayer(life_of_player)
                list_pools_blood = []
                enemies = []
                count_enemies = 0

        if not player:
            # if player not exist, gets the events of manager restart
            manager_restart.process_events(event)

    for blood in list_pools_blood:  # Draw blood
        blood.draw(screen)

    if player:
        player.draw(screen)                             # Draw the player
        # Update movemento of the player and if exited display
        player.Movement(speed)

        # call update of shots an rotatio of the player
        player.Rotation_Shoot(pygame.mouse.get_pos(),
                              bullet_speed, dt, bullets_of_player)

        if player.death:
            list_pools_blood.append(PoolsBlood(player.position))
            kills = player.kills
            player = None
            write_score = True
            continue

        while count_enemies < amount_enemies and timer_to_respawn <= 0:  # Create N enemies, if is necessary
            point = [random.randint(0, width), random.randint(
                0, height)]  # random point for each enemy
            if random.randint(0, 3) == 2:
                enemies.append(EnemyRange(point, speed_of_enemy,
                                    life_of_enemy))  # Create range enemy
            else:
                enemies.append(Enemy(point, speed_of_enemy,
                                    life_of_enemy))  # Create normal enemy

            count_enemies += 1
            timer_to_respawn = random.uniform(1, 2.5)

        timer_to_respawn -= dt

        for enemy in enemies:  # Update all enemies (normal and range enemies)
            if enemy.type == 'N':
                enemy.update(player, dt)
            elif enemy.type == 'R':
                enemy.update(player, dt, bullets_of_enemies)

            enemy.draw(screen)

            if enemy.kill:
                list_pools_blood.append(PoolsBlood(enemy.position))
                enemies.remove(enemy)
                count_enemies -= 1
                player.kills += 1

        img = font.render('Kills: ' + str(player.kills), True, (255, 255, 255))
        screen.blit(img, (20, 20))

        lbar.draw(screen, width, player.life/life_of_player)

    else:  # if player not exists, draw ui to restart
        if write_score:
            arch = open("gamedata/score.txt", "a")
            arch.write(str(kills)+'\n')
            arch.close()
            arch = open("gamedata/score.txt", "r")
            lis = arch.readlines()
            lis = [int(x[0:len(x)-1]) for x in lis]
            best = max(lis)
            print(lis)

            write_score = False

            img = font2.render('Kills: ' + str(kills), True, (255, 255, 255))
            img2 = font2.render('Best score: ' + str(best), True, (255, 255, 255))

        manager_restart.update(dt)
        manager_restart.draw_ui(screen)

        
        screen.blit(img, (width/2.3, height/2.7))
        screen.blit(img2, (width/2.5, height/3.7))

    for bullet in bullets_of_player:  # Update bullets of player
        bullet.draw(screen, enemies, dt)

        if bullet.destroy:
            hits.append(Hit(time_hit, bullet.position))
            bullets_of_player.remove(bullet)

    for bullet in bullets_of_enemies:  # update bullets of enemies
        bullet.draw(screen, [player], dt)

        if bullet.destroy:
            hits.append(Hit(time_hit, bullet.position))
            bullets_of_enemies.remove(bullet)
    
    for h in hits:
        h.draw(screen, dt)

        if h.destroy:
            hits.remove(h)

    pygame.display.update()
    FramePerSec.tick(FPS)
    # Set the background color
    screen.fill(background_color)
