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


name = "MainState"
move_scale = 0.5
player = None

# Game object class here
def create_world():
    global player
    player = Player()

def destroy_world():
    global player
    del(player)

def enter():
    global back_ground
    global air_enemy
    global air_enemy2
    global air_enemy3
    global air_enemy4
    global air_enemy5
    global team
    back_ground = backGround()

    #new added
    create_world()

    team = [airplane_enemy() for i in range(20)]

    for enemy in team:
        enemy.x = random.randint(100, 700)
        enemy.y = random.randint(100, 600)
        pass


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

def exit():
    global back_ground
    global air_enemy
    global air_enemy2
    global air_enemy3
    global air_enemy4
    global air_enemy5
    del(back_ground)
    del(air_enemy)
    del (air_enemy2)
    del (air_enemy3)
    del (air_enemy4)
    del (air_enemy5)



    destroy_world()

#airplane class (enemy)
class airplane_enemy:
    def __init__(self):
        self.x, self.y = random.randint(-100, 800), random.randint(-100, 600)
        self.ownX = random.randint(100, 700)
        self.ownY = random.randint(300, 500)

        #Add tile set.
        #To deny overact
        self.tileX = 0
        self.tileY = 0
        #self.ownX = 0
        #self.ownY = 0
        self.image = load_image('enemyBlack.png')

    def update(self):
        #enemy should find own place
        if (self.x > self.ownX):
            self.x -= move_scale
        elif self.x < self.ownX:
            self.x += move_scale
        elif self.y > self.ownY:
            self.y -= move_scale
        elif self.y < self.ownY:
            self.y += move_scale
        pass
    def draw(self):
        self.image.draw(self.x, self.y)
    pass

class bullet:
    def __init__(self):

        pass
    def draw(self):
        pass
    pass


#background image
class backGround:
    def __init__(self):
        #not yet!
        self.pagePoint = 3       #scroll the page
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
    #start var.
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
    back_ground.update()

    for air_enemyt in team:
        air_enemyt.update()
    pass


def draw(frame_time):
    clear_canvas()
    #don't change
    back_ground.draw()

    #start
    #air_player.draw()
    player.draw()
    player.draw_bb()

    for air_enemyt in team:
        air_enemyt.draw()

    air_enemy.draw()
    air_enemy2.draw()
    air_enemy3.draw()
    air_enemy4.draw()
    air_enemy5.draw()
    update_canvas()
    pass
