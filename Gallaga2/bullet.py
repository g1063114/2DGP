# To do list    2016-11-24
#   add time_func
#
# enemies bullet sync
#
# ----------------------------------

from pico2d import*
import random



class Bullet:
    image = None

    PIXEL_PER_KMETER = (10.0 / 0.5)         # 10 pixel 0.5km
    RUN_SPEED_KMPH = 180000.0               # 180000km per hour
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60    # 3000km per min
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60    # 50km per sec
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER


    def __init__(self):
        self.x, self.y = -100, -30
        self.shooting = False
        self.shoot_start = False

        self.shoot_dir = -1
        if Bullet.image == None:
            # Bullet.image = load_image('resource/bullet_folder/fire.png')
            Bullet.image = load_image('resource/bullet_folder/fire.png')

    def update(self, frame_time, player_x):
        if self.shooting is True:
            if self.shoot_start is True:
                self.x = player_x
                self.shoot_start = False
            if self.y >= 630:
                self.y = self.shoot_dir * 30
                self.shooting = False

            distance = self.RUN_SPEED_PPS * frame_time
            self.y += distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        # return self.x - 7, self.y - 16, self.x + 7, self.y + 16
        return self.x - 6, self.y - 19, self.x + 6, self.y + 19

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.shooting is False:
                self.y = -30
                self.shooting = True
                self.shoot_start = True

    def stop(self):
        self.shooting = False
        self.y = -30



class EnemyBullet:
    image = None
    shooting_sound = None
    PIXEL_PER_KMETER = (10.0 / 0.5)         # 10 pixel 0.5km
    RUN_SPEED_KMPH = 108000.0                # 108000km per hour
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60    # 1800km per min
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60    # 30km per sec
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER


    def __init__(self):
        self.x, self.y = -100, 650
        self.shooting = False
        self.shoot_start = False
        self.shoot_dir = -1
        self.shooting_sound = load_wav('resource/sound/shooting.wav')
        self.shooting_sound.set_volume(128)

        if EnemyBullet.image == None:
            EnemyBullet.image = load_image('resource/bullet_folder/enemy_bullet.png')

    def update(self, frame_time, player_x, player_y):
        if self.shooting is True:
            if self.shoot_start is True:
                self.x = player_x
                self.y = player_y
                self.shoot_start = False
            if self.y >= 630:
                self.y = self.shoot_dir * 30
                self.shooting = False

            distance = self.RUN_SPEED_PPS * frame_time
            self.y -= distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        # return self.x - 7, self.y - 16, self.x + 7, self.y + 16
        return self.x - 6, self.y - 19, self.x + 6, self.y + 19

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

    def stop(self):
        self.shooting = False
        self.y = -30



class BossBullet:
    image = None
    shooting_sound = None
    PIXEL_PER_KMETER = (10.0 / 0.5)         # 10 pixel 0.5km
    RUN_SPEED_KMPH = 108000.0                # 108000km per hour
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60    # 1800km per min
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60    # 30km per sec
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER


    def __init__(self):
        self.x, self.y = -100, 650
        self.local = 0
        self.shooting = False
        self.shoot_start = False
        self.shoot_dir = -1
        self.shooting_sound = load_wav('resource/sound/shooting.wav')
        self.shooting_sound.set_volume(128)

        if BossBullet.image == None:
            BossBullet.image = load_image('resource/bullet_folder/boss_bullet.png')

    def update(self, frame_time, player_x, player_y):
        if self.shooting is True:
            if self.shoot_start is True:
                self.x = player_x
                self.y = player_y
                self.shoot_start = False
            if self.y >= 630:
                self.y = self.shoot_dir * 30
                self.shooting = False

            distance = self.RUN_SPEED_PPS * frame_time

            if self.local is 0:
                self.x -= distance
                self.y -= distance

            if self.local is 1:
                self.y -= distance
                print("보스 탄약1")


            if self.local is 2:
                self.x += distance
                self.y -= distance
                print("보스탄약2")


    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        # return self.x - 7, self.y - 16, self.x + 7, self.y + 16
        # return self.x - 6, self.y - 19, self.x + 6, self.y + 19
        return self.x - 24, self.y - 23, self.x + 24, self.y + 23


    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

    def stop(self):
        self.shooting = False
        self.y = -30
