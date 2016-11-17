from pico2d import*
import random
from bullet import Bullet


class Enemy:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 5.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None

    LEFT_RUN, RIGHT_RUN, UP_RUN, DOWN_RUN, STAND = 0, 1, 2, 3, 4

    def __init__(self):
        self.x, self.y = 0, 0
        #self.gen_x, self.gen_y = random.randint(-200,1000), random.randint(-100,700)
        self.arr_x, self.arr_y = random.randint(1,20), random.randint(1,4)
        self.state = self.STAND
        self.dir_x = 1
        self.dir_y = 0
        self.image = load_image('enemyBlack.png')
        self.x = 800 - self.arr_x * 40
        self.y = 500 - self.arr_y * 30

    def update(self, frame_time):

        distance = Enemy.RUN_SPEED_PPS * frame_time
        #self.y += (self.dir_y * distance)

        #move left_right
        #if self.x <= self.arr_x * 1:
        #self.x = self.x + 10
        #self.x += (self.dir_x * distance)
        if self.x < 800 - (self.arr_x + 3) * 40:
            self.dir_x = +1
        elif self.x >= 800 - (self.arr_x - 3) * 40:
            self.dir_x = -1
        self.x += (self.dir_x * distance)
        #self.y += 20
        #elif self.x > self.arr_x * 40:
        #self.x -= (self.dir_x * distance)

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
