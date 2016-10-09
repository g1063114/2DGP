#################################################
############# GALLAGA_REMAKEver #################
# Start project in 2016-10-02
# 1. make code layout (2016-10-02)
# 2. add resource(player)
# Made by Gunny
#################################################


from pico2d import *
import math

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



# initialization code
open_canvas()
running = True
player = airplane_player()
menu = 0


# game main loop code

#init screen



#entering game
while running:
    handle_events()
    player.update()

    player.draw()
    update_canvas()
    delay(0.05)

# finalization code
close_canvas()