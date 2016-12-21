from pico2d import *


class Background:
    PIXEL_PER_KMETER = (10.0 / 0.5)         # 10 pixel 0.5km
    RUN_SPEED_KMPH = 36000.0                # 36000km per hour
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60    # 600km per min
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60    # 10km per sec
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER

    def __init__(self, w, h):
        self.image = load_image('resource/background_folder/background.png')
        self.speed = 0
        self.bottom = 0
        self.screen_width = w
        self.screen_height = h

    def draw(self):
        y = int (self.bottom)
        h = min(self.image.h - y, self.screen_height)
        self.image.clip_draw_to_origin(0, y, self.screen_width, h, 0, 0)
        self.image.clip_draw_to_origin(0, 0, self.screen_width, self.screen_height - h, 0, h)

    def update(self, frame_time):
        self.speed = Background.RUN_SPEED_PPS
        self.bottom = (self.bottom + frame_time * self.speed) % self.image.h

class Background2:
    PIXEL_PER_KMETER = (10.0 / 0.5)         # 10 pixel 0.5km
    RUN_SPEED_KMPH = 36000.0                # 36000km per hour
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60    # 600km per min
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60    # 10km per sec
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER

    def __init__(self, w, h):
        self.image = load_image('resource/background_folder/background2.png')
        self.speed = 0
        self.bottom = 0
        self.screen_width = w
        self.screen_height = h

    def draw(self):
        y = int (self.bottom)
        h = min(self.image.h - y, self.screen_height)
        self.image.clip_draw_to_origin(0, y, self.screen_width, h, 0, 0)
        self.image.clip_draw_to_origin(0, 0, self.screen_width, self.screen_height - h, 0, h)

    def update(self, frame_time):
        self.speed = Background.RUN_SPEED_PPS
        self.bottom = (self.bottom + frame_time * self.speed) % self.image.h

class Background3:
    PIXEL_PER_KMETER = (10.0 / 0.5)         # 10 pixel 0.5km
    RUN_SPEED_KMPH = 36000.0                # 36000km per hour
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60    # 600km per min
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60    # 10km per sec
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER

    def __init__(self, w, h):
        self.image = load_image('resource/background_folder/background3.png')
        self.speed = 0
        self.bottom = 0
        self.screen_width = w
        self.screen_height = h

    def draw(self):
        y = int (self.bottom)
        h = min(self.image.h - y, self.screen_height)
        self.image.clip_draw_to_origin(0, y, self.screen_width, h, 0, 0)
        self.image.clip_draw_to_origin(0, 0, self.screen_width, self.screen_height - h, 0, h)

    def update(self, frame_time):
        self.speed = Background.RUN_SPEED_PPS
        self.bottom = (self.bottom + frame_time * self.speed) % self.image.h

