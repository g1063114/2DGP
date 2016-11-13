from pico2d import *

class Player:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None

    #state define
    STAND, MOVE_LEFT, MOVE_RIGHT = 0, 1, 2


    def __init__(self):
        self.x, self.y = 400, 30
        self.dir = 0        # 0:stand 1:right 2:left
        self.state = self.STAND
        self.image = load_image('player.png')

    def update(self, frame_time):
        #clamp 벽과 충돌 체크 ( 일단은 넣어놔 이거 두 줄)
        #def clamp(minimum, x, maximum):
        #    return max(minimum, min(x, maximum))


        #시간 동기화 시켜줘야한다. 컴퓨터마다 사양이 다르므로.
        distance = Player.RUN_SPEED_PPS * frame_time
        #distance = 10
        #self.total_frames += Player.FRAMES_PER_ACTION * Player.ACTION_PER_TIME * frame_time
        #self.frame = int(self.total_frames) % 8
        self.x += (self.dir * distance)


        #일단 클램프는 넣어놔
        #self.x = clamp(0, self.x, 800)


        #next i'll add frame

        # ----------------------------------------------
        #self.frame = (self.frame + 1) & 7
        #if (self.pressKey == 1) and (self.dir == 0):
        #    self.x += move_scale
        #elif (self.pressKey == 1) and (self.dir == 1):
        #    self.x -= move_scale
         #----------------------------------------------


    def draw(self):
        self.image.draw(self.x, self.y)


    def get_bb(self):
        #이미지 크기는 40*30
        return self.x - 20, self.y - 15, self.x + 20, self.y + 15

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.STAND, self.MOVE_RIGHT):
                self.state = self.MOVE_LEFT
                self.dir = -1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.STAND, self.MOVE_LEFT):
                self.state = self.MOVE_RIGHT
                self.dir = 1
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.MOVE_LEFT,):
                self.state = self.STAND
                self.dir = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.MOVE_RIGHT,):
                self.state = self.STAND
                self.dir = 0
