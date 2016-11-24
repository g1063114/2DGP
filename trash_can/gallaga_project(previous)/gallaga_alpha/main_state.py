#################################################
############# GALLAGA_REMAKEver #################
# Start project in 2016-10-02
# 1. make code layout (2016-10-02)
# 2. add resource(player)
# 3. add game_framework (2016.10.14)
# 4. optimize1 game_framework (2016.10.17)
# 5. enemy_setted (2016.10.20)
# Made by Gunny
#################################################

from pico2d import *
import random
import os
import game_framework
import title_state


name = "MainState"



# Game object class here

#airplane class (player)
class airplane_player:
    def __init__(self):
        self.x, self.y = 400 , 30
        self.pressKey = 0   # 0:stop  1:go
        self.dir = 0        # 0:right 1:left
        self.frame = 0
        self.image = load_image('player.png')

    def update(self):
        #next i'll add frame
        #self.frame = (self.frame + 1) & 7
        if (self.pressKey == 1) and (self.dir == 0):
            self.x += 1
        elif (self.pressKey == 1) and (self.dir == 1):
            self.x -= 1
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
    pass

#airplane class (enemy)
class airplane_enemy:
    def __init__(self):
        self.x = -50
        self.y = -50
        self.ownX = 0
        self.ownY = 0
        self.image = load_image('enemyBlack.png')

    def update(self):
        #enemy should find own place
        if (self.x != self.ownX) and (self.y != self.ownY):
            self.x += 0.5
            self.y += 0.5
        pass
    def draw(self):
        self.image.draw(self.x, self.y)
    pass

#background image
class backGround:
    def __init__(self):
        #not yet!
        self.image = load_image('background.png')
    def draw(self):
        self.image.draw(400, 300);
    pass



def enter():
    global air_player
    global back_ground
    global air_enemy
    global air_enemy2
    global air_enemy3
    global air_enemy4
    global air_enemy5

    back_ground = backGround()
    air_player = airplane_player()
    air_enemy = airplane_enemy()
    air_enemy2 = airplane_enemy()
    air_enemy3 = airplane_enemy()
    air_enemy4 = airplane_enemy()
    air_enemy5 = airplane_enemy()

    air_enemy.ownX = 400
    air_enemy.ownY = 300
    air_enemy2.ownX = 440
    air_enemy2.ownY = 300
    air_enemy3.ownX = 480
    air_enemy3.ownY = 300
    air_enemy4.ownX = 520
    air_enemy4.ownY = 300
    air_enemy5.ownX = 560
    air_enemy5.ownY = 300

    pass


def exit():
    global air_player, back_ground
    global air_enemy
    global air_enemy2
    global air_enemy3
    global air_enemy4
    global air_enemy5
    del(air_player)
    del(back_ground)
    del(air_enemy)
    del (air_enemy2)
    del (air_enemy3)
    del (air_enemy4)
    del (air_enemy5)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    #start var.
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

        #player--------------------------------------------------------
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            air_player.pressKey = 1
            air_player.dir = 1
        elif event.type == SDL_KEYUP and event.key == SDLK_LEFT:
            air_player.pressKey = 0
            air_player.dir = 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            air_player.pressKey = 1
            air_player.dir = 0
        elif event.type == SDL_KEYUP and event.key == SDLK_RIGHT:
            air_player.pressKey = 0
            air_player.dir = 0
        #---------------------------------------------------------------
    pass


def update():
    air_player.update()
    air_enemy.update()
    air_enemy2.update()
    air_enemy3.update()
    air_enemy4.update()
    air_enemy5.update()

    pass


def draw():
    clear_canvas()
    #don't change
    back_ground.draw()

    #start
    air_player.draw()
    air_enemy.draw()
    air_enemy2.draw()
    air_enemy3.draw()
    air_enemy4.draw()
    air_enemy5.draw()
    update_canvas()
    pass
