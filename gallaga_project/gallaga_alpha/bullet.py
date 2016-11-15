from pico2d import*

class Bullet:
    image = None

    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 40.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    def __init__(self):
        self.x, self.y = -100, -30
        self.shoot_speed = 100
        self.shooting = False
        self.shoot_start = False
        self.shoot_dir = -1
        if Bullet.image == None:
            Bullet.image = load_image('fire.png')

    def update(self, frame_time, inX):
        if self.shooting is True:
            if self.shoot_start is True:
                self.x = inX
                self.shoot_start = False
            if self.y >= 630:
                self.y = self.shoot_dir * 30
                self.shooting = False

            distance = Bullet.RUN_SPEED_PPS * frame_time
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



