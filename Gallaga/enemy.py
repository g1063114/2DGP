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
    LEFT_RUN, RIGHT_RUN, UP_RUN, DOWN_RUN, STAND = 0, 1, 2, 3, 4

    def __init__(self):
        self.x, self.y = 0, 0
        self.arr_x, self.arr_y = 0, 0
        self.state = self.STAND
        self.dir_x = 1
        self.dir_y = 0
        self.image = load_image('resource/aircraft_folder/enemyBlack.png')
        self.x = 800 - self.arr_x * 40
        self.y = 600 - self.arr_y * 30

    def set_location(self, in_arr_x, in_arr_y):
        self.arr_x = in_arr_x
        self.arr_y = in_arr_y
        self.x = 800 - self.arr_x * 40
        self.y = 600 - self.arr_y * 30

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
        self.x = -100
        self.y = -100

# Boss. Son of Enemy class.
class Boss(Enemy):
    # pos, dir
    pass