# ----------------------------------
# To do list    2016-11-24
#   add time_func
#
#
#
# ----------------------------------

from pico2d import*
import random



class Bullet:
    image = None

    def __init__(self):
        self.x, self.y = -100, -30
        self.shot_speed = 800
        self.shooting = False
        self.shoot_start = False
        self.shoot_dir = -1
        if Bullet.image == None:
            Bullet.image = load_image('resource/bullet_folder/fire.png')

    def update(self, frame_time, player_x):
        if self.shooting is True:
            if self.shoot_start is True:
                self.x = player_x
                self.shoot_start = False
            if self.y >= 630:
                self.y = self.shoot_dir * 30
                self.shooting = False

            distance = self.shot_speed * frame_time
            self.y += 1 * distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 7, self.y - 16, self.x + 7, self.y + 16

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



class EnemyBullet(Bullet):

    image = None

    def __init__(self):
        self.x, self.y = 100, 700

        # 500ms ~ 2000ms shooting time
        self.shooting_time = random.randint(500, 2000)
        # self.shooting
        if EnemyBullet.image == None:   # 13 * 37의 이미지
            EnemyBullet.image = load_image('resource/bullet_folder/enemy_bullet.png')

    def update(self, frame_time, enemy_x):
        pass

    def timer(self):
        pass

    def get_bb(self):
        return self.x - 6, self.y - 18, self.x + 6, self.y - 18


