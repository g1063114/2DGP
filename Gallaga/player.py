# player life should be added. 2016 - 12 - 15



from pico2d import *

class Player:
    image = None
    shooting_sound = None

    damaged_image = None
    crush_sound = None

    PIXEL_PER_KMETER = (10.0 / 0.5)         # 10 pixel 0.5km
    RUN_SPEED_KMPH = 36000.0                # 36000km per hour
    RUN_SPEED_KMPM = RUN_SPEED_KMPH / 60    # 600km per min
    RUN_SPEED_KMPS = RUN_SPEED_KMPM / 60    # 10km per sec
    RUN_SPEED_PPS = RUN_SPEED_KMPS * PIXEL_PER_KMETER



    #state define
    STAND, MOVE_LEFT, MOVE_RIGHT = 0, 1, 2


    def __init__(self):
        self.x, self.y = 400, 30
        self.next_stage = False
        self.dir = 0        # 0:stand 1:right 2:left
        self.state = self.STAND
        self.live = True
        self.shooting = False
        # frame added
        self.frame = -1

        self.shooting_sound = load_wav('resource/sound/player_shooting.wav')
        self.shooting_sound.set_volume(128)

        self.crush_sound = load_wav('resource/sound/break.wav')
        self.crush_sound.set_volume(128)

        self.image = load_image('resource/aircraft_folder/player.png')
        self.damaged_image = load_image('resource/aircraft_folder/player_damage_ani.png')

    def you_dead_huh(self, input):
        self.crush_sound.play()
        self.live = False
        pass


    def update(self, frame_time):

        #시간 동기화 시켜줘야한다. 컴퓨터마다 사양이 다르므로.
        distance = Player.RUN_SPEED_PPS * frame_time
        #distance = 10
        #self.total_frames += Player.FRAMES_PER_ACTION * Player.ACTION_PER_TIME * frame_time
        #self.frame = int(self.total_frames) % 8
        self.x += (self.dir * distance)
        if(self.next_stage is True):
            self.y += distance

        # if go next stage then aircraft y ++
    def go_next_stage(self):
        self.next_stage = True
        pass

    def draw(self):
        if self.live is True:
            self.image.draw(self.x, self.y)
        elif self.live is False:
            print("격추 이미지 호출")
            self.damaged_image.clip_draw(self.frame * 40, 0, 40, 30, self.x, self.y)
            if self.frame is 3:
                self.frame = -1
                self.live = True
                print("격추 이미지 호출 끝")

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
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            self.shooting = True
