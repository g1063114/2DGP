#################################################
############# GALLAGA_REMAKEver #################
# Start project in 2016-10-02
# 1. make code layout (2016-10-02)
#
# Made by Gunny
#################################################


from pico2d import *
import math

# Game object class here

#airplane class (player)
class airplane_player:
    def __init__(self):
        x = 0
        y = 0
        self.image = load_image('player_airplane.png')
    def draw(self):
        self.image.draw(x ,y)

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

def handle_events():
    #start var.
    global launching


    #define key
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            launching = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            launching = False



# initialization code
open_canvas()



# game main loop code





# finalization code
close_canvas()