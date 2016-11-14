#################################################
############# GALLAGA_REMAKEver #################
# Start project in 2016-10-02
# 1. make code layout (2016-10-02)
# 2. add resource(player)
# 3. add game_framework (2016.10.14)
# 4. optimize1 game_framework (2016.10.17)
# 5. enemy_setted (2016.10.20)
# 6. enemy_tile think (2016.10.25)
# 7. enemy_tile add (2016.10.27)
# 8. bullet add(2016.10.30)
# 9. collide check(2016-11-04~)
# 10. rank.py added(2016-11-07)
# 11. move while move (2016-11-08)
# 12. player, enemy .py added (2016-11-14)
#       main_state_test added working on this space!
# Made by Gunny
#################################################

from pico2d import *
import random
import os
import game_framework
import title_state
from player import Player
from enemy import Enemy


name = "MainState"
move_scale = 0.5
player = None
enemies = None
back_ground = None

# Game object class here
def create_world():
    global player, enemies
    player = Player()
    enemies = [Enemy() for i in range(40)]


def destroy_world():
    global player, enemies
    del(player)
    del(enemies)


def enter():
    global back_ground
    back_ground = backGround()

    # new added
    create_world()


def exit():
    destroy_world()


class bullet:
    def __init__(self):
        pass

    def draw(self):
        pass
    pass


# background image
class backGround:
    def __init__(self):
        # not yet!
        self.pagePoint = 3       # scroll the page
        self.pagePoint2 = 1
        self.image = load_image('background.png')
        self.image2 = load_image('background.png')
    def draw(self):
        self.image.draw(400, 300 * self.pagePoint);
        self.image2.draw(400, 300 * self.pagePoint2);
    def update(self):
        if self.pagePoint > -1:
            self.pagePoint -= 0.001
        else:
            self.pagePoint = 3

        if self.pagePoint2 > -1:
            self.pagePoint2 -= 0.001
        else:
            self.pagePoint2 = 3
        pass
    pass


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    # start var.
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                player.handle_event(event)


def update(frame_time):
    player.update(frame_time)
    for enemy in enemies:
        enemy.update(frame_time)
    back_ground.update()




def draw(frame_time):
    clear_canvas()
    # don't change
    back_ground.draw()

    # start
    # player.draw()
    player.draw()
    player.draw_bb()

    # enemies
    for enemy in enemies:
        enemy.draw()
        enemy.draw_bb()

    update_canvas()
