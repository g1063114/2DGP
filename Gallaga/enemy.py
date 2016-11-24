from pico2d import*
import random
from bullet import Bullet


class Enemy:
    image = None

    LEFT_RUN, RIGHT_RUN, UP_RUN, DOWN_RUN, STAND = 0, 1, 2, 3, 4

    def __init__(self):
        self.x, self.y = 0, 0
        self.move_speed = 50
        # This! i have to check
        self.arr_x, self.arr_y = random.randint(6, 20), random.randint(4, 8)
        # self.arr_x, self.arr_y = 0, 0
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
        distance = self.move_speed * frame_time

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
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.STAND, self.RIGHT_RUN):
                self.state = self.LEFT_RUN
                self.dir = -1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.STAND, self.LEFT_RUN):
                self.state = self.RIGHT_RUN
                self.dir = 1
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state = self.STAND
                self.dir = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state = self.STAND
                self.dir = 0

    def stop(self):
        self.x = -100
        self.y = -100
