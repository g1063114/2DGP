from pico2d import*
import random

class Enemy:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
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
        self.dir_x = -1
        self.dir_y = 0
        self.image = load_image('enemyBlack.png')

    def update(self, frame_time):
        self.x = 800 - self.arr_x * 40
        self.y = 600 - self.arr_y * 30
        distance = Enemy.RUN_SPEED_PPS * frame_time
        #self.y += (self.dir_y * distance)

        #move left_right
        #if self.x <= self.arr_x * 1:
        #self.x += (self.dir_x * distance)
        self.y += 20
        #elif self.x > self.arr_x * 40:
        #self.x -= (self.dir_x * distance)

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y - 15, self.x + 20, self.y + 15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


#화면을 분할해서 배열에 넣어주고
#그 배열번호를 랜덤하게 들어가게 해야되는데... 물론 중복은 피하고
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
