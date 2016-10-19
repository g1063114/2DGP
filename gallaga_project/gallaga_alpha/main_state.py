#################################################
############# GALLAGA_REMAKEver #################
# Start project in 2016-10-02
# 1. make code layout (2016-10-02)
# 2. add resource(player)
# 3. add game_framework (2016.10.14)
# 4. optimize1 game_framework (2016.10.17)
# 5.
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
        self.x, self.y = 0 , 10
        self.frame = 0
        self.image = load_image('player.png')

    def update(self):
        self.frame = (self.frame + 1) & 7
        self.x += 10

    def draw(self):
        self.image.clip_draw(self.frame*18, 10, 18, 18, self.x, self.y)

    pass

#airplane class (enemy)
class airplane_enemy:
    def __init_(self):
        x = 0
        y = 0
        self.image = load_image('enemy_airplane.png')
    def draw(self):
        self.image.draw(x ,y)

    pass

def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()
    pass


def exit():
    global boy, grass
    del(boy)
    del(grass)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    #start var.
    global running

    #define key
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


def update():
    boy.update()
    pass


def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()
    pass
