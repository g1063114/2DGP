# boss added 2016-12-15
# enemy animation add 2016-12-18
# boss animation added 2016-12-19

from pico2d import*
import random
from bullet import Bullet


class Enemy:
    image = None

    PIXEL_PER_KMETER = (10.0 / 0.5)  # 10 pixel 0.5km
    RUN_SPEED_KMPH = 18000.0  # 18000km per hour
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60  # 300km per min
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60  # 5km per sec
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER

    def __init__(self):
        self.x, self.y = 0, 0
        self.arr_x, self.arr_y = 0, 0
        self.dir_x = 1
        self.dir_y = 0
        self.is_dead = False
        self.shooting = False
        self.image = load_image('resource/aircraft_folder/enemyBlack.png')
        self.x = 800 - self.arr_x * 40
        self.y = 600 - self.arr_y * 30

    def set_location(self, in_arr_x, in_arr_y):
        self.arr_x = in_arr_x
        self.arr_y = in_arr_y
        self.x = 800 - self.arr_x * 40
        self.y = 600 - self.arr_y * 30

    def set_shooting(self,input):   #input = True or False
        self.shooting = input

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.x < 800 - (self.arr_x) * 40:
            self.dir_x = +1
        elif self.x >= 800 - (self.arr_x - 4) * 40:
            self.dir_x = -1
        self.x += (self.dir_x * distance)

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y - 15, self.x + 20, self.y + 15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

    def stop(self):
        self.is_dead = True
        self.x = -100
        self.y = -100


class Boss:
    image = None

    PIXEL_PER_KMETER = (10.0 / 0.5)  # 10 pixel 0.5km
    RUN_SPEED_KMPH = 18000.0  # 18000km per hour
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60  # 300km per min
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60  # 5km per sec
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER

    def __init__(self):
        self.x, self.y = 0, 0
        self.arr_x, self.arr_y = 0, 0
        self.dir_x = 1
        self.dir_y = 0
        ###
        self.life = 5
        ###
        self.is_dead = False
        self.shooting = False
        self.image = load_image('resource/aircraft_folder/enemyBlackBoss.png')
        self.x = 800 - self.arr_x * 82
        self.y = 600 - self.arr_y * 84

    def set_location(self, in_arr_x, in_arr_y):
        self.arr_x = in_arr_x
        self.arr_y = in_arr_y
        self.x = 800 - self.arr_x * 82
        self.y = 600 - self.arr_y * 84

    def set_shooting(self,input):   #input = True or False
        self.shooting = input

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.x < 800 - (self.arr_x + 8) * 82:
            self.dir_x = +1
        elif self.x >= 800 - (self.arr_x) * 82:
            self.dir_x = -1
        self.x += (self.dir_x * distance)

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 41, self.y - 42, self.x + 41, self.y + 42

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

    def stop(self):
        self.is_dead = True
        self.x = -100
        self.y = -100

    pass


class Enemy2:
    image = None

    PIXEL_PER_KMETER = (10.0 / 0.5)  # 10 pixel 0.5km
    RUN_SPEED_KMPH = 18000.0  # 18000km per hour
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60  # 300km per min
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60  # 5km per sec
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER

    def __init__(self):
        self.x, self.y = 0, 0
        self.arr_x, self.arr_y = 0, 0
        self.dir_x = 1
        self.dir_y = 0
        self.is_dead = False
        self.shooting = False
        self.image = load_image('resource/aircraft_folder/enemyBlue.png')
        self.x = 800 - self.arr_x * 40
        self.y = 600 - self.arr_y * 30

    def set_location(self, in_arr_x, in_arr_y):
        self.arr_x = in_arr_x
        self.arr_y = in_arr_y
        self.x = 800 - self.arr_x * 40
        self.y = 600 - self.arr_y * 30

    def set_shooting(self,input):   #input = True or False
        self.shooting = input

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.x < 800 - (self.arr_x) * 40:
            self.dir_x = +1
        elif self.x >= 800 - (self.arr_x - 4) * 40:
            self.dir_x = -1
        self.x += (self.dir_x * distance)

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y - 15, self.x + 20, self.y + 15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

    def stop(self):
        self.is_dead = True
        self.x = -100
        self.y = -100



class Boss2:
    image = None

    PIXEL_PER_KMETER = (10.0 / 0.5)  # 10 pixel 0.5km
    RUN_SPEED_KMPH = 18000.0  # 18000km per hour
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60  # 300km per min
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60  # 5km per sec
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER

    def __init__(self):
        self.x, self.y = 0, 0
        self.arr_x, self.arr_y = 0, 0
        self.dir_x = 1
        self.dir_y = 0
        ###
        self.life = 5
        ###
        self.is_dead = False
        self.shooting = False
        self.image = load_image('resource/aircraft_folder/enemyBlueBoss.png')
        self.x = 800 - self.arr_x * 82
        self.y = 600 - self.arr_y * 84

    def set_location(self, in_arr_x, in_arr_y):
        self.arr_x = in_arr_x
        self.arr_y = in_arr_y
        self.x = 800 - self.arr_x * 82
        self.y = 600 - self.arr_y * 84

    def set_shooting(self,input):   #input = True or False
        self.shooting = input

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.x < 800 - (self.arr_x + 8) * 82:
            self.dir_x = +1
        elif self.x >= 800 - (self.arr_x) * 82:
            self.dir_x = -1
        self.x += (self.dir_x * distance)

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 41, self.y - 42, self.x + 41, self.y + 42

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

    def stop(self):
        self.is_dead = True
        self.x = -100
        self.y = -100



class Enemy3:
    image = None

    PIXEL_PER_KMETER = (10.0 / 0.5)  # 10 pixel 0.5km
    RUN_SPEED_KMPH = 18000.0  # 18000km per hour
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60  # 300km per min
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60  # 5km per sec
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER

    def __init__(self):
        self.x, self.y = 0, 0
        self.arr_x, self.arr_y = 0, 0
        self.dir_x = 1
        self.dir_y = 0
        self.is_dead = False
        self.shooting = False
        self.image = load_image('resource/aircraft_folder/enemyGreen.png')
        self.x = 800 - self.arr_x * 40
        self.y = 600 - self.arr_y * 30

    def set_location(self, in_arr_x, in_arr_y):
        self.arr_x = in_arr_x
        self.arr_y = in_arr_y
        self.x = 800 - self.arr_x * 40
        self.y = 600 - self.arr_y * 30

    def set_shooting(self,input):   #input = True or False
        self.shooting = input

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.x < 800 - (self.arr_x) * 40:
            self.dir_x = +1
        elif self.x >= 800 - (self.arr_x - 4) * 40:
            self.dir_x = -1
        self.x += (self.dir_x * distance)

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y - 15, self.x + 20, self.y + 15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

    def stop(self):
        self.is_dead = True
        self.x = -100
        self.y = -100


class Boss3:
    image = None

    PIXEL_PER_KMETER = (10.0 / 0.5)  # 10 pixel 0.5km
    RUN_SPEED_KMPH = 18000.0  # 18000km per hour
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60  # 300km per min
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60  # 5km per sec
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER

    def __init__(self):
        self.x, self.y = 0, 0
        self.arr_x, self.arr_y = 0, 0
        self.dir_x = 1
        self.dir_y = 0
        ###
        self.life = 5
        ###
        self.is_dead = False
        self.shooting = False
        self.image = load_image('resource/aircraft_folder/enemyGreenBoss.png')
        self.x = 800 - self.arr_x * 82
        self.y = 600 - self.arr_y * 84

    def set_location(self, in_arr_x, in_arr_y):
        self.arr_x = in_arr_x
        self.arr_y = in_arr_y
        self.x = 800 - self.arr_x * 82
        self.y = 600 - self.arr_y * 84

    def set_shooting(self,input):   #input = True or False
        self.shooting = input

    def update(self, frame_time):
        distance = self.RUN_SPEED_PPS * frame_time
        if self.x < 800 - (self.arr_x + 8) * 82:
            self.dir_x = +1
        elif self.x >= 800 - (self.arr_x) * 82:
            self.dir_x = -1
        self.x += (self.dir_x * distance)

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 41, self.y - 42, self.x + 41, self.y + 42

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

    def stop(self):
        self.is_dead = True
        self.x = -100
        self.y = -100
