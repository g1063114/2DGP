from pico2d import*



class ScoreDraw:
    image = None
    number0_image = None
    number1_image = None
    number2_image = None
    number3_image = None
    number4_image = None
    number5_image = None
    number6_image = None
    number7_image = None
    number8_image = None
    number9_image = None

    def __init__(self):
        # 여기서부터 내가 코딩
        self.draw_x, self.draw_y = 50, 550

        if ScoreDraw.number0_image == None:
            ScoreDraw.number0_image = load_image('numeral0.png')

        elif ScoreDraw.number1_image == None:
            ScoreDraw.number1_image = load_image('numeral1.png')

        elif ScoreDraw.number2_image == None:
            ScoreDraw.number2_image = load_image('numeral2.png')

        elif ScoreDraw.number3_image == None:
            ScoreDraw.number3_image = load_image('numeral3.png')

        elif ScoreDraw.number4_image == None:
            ScoreDraw.number4_image = load_image('numeral4.png')

        elif ScoreDraw.number5_image == None:
            ScoreDraw.number5_image = load_image('numeral5.png')

        elif ScoreDraw.number6_image == None:
            ScoreDraw.number6_image = load_image('numeral6.png')

        elif ScoreDraw.number7_image == None:
            ScoreDraw.number7_image = load_image('numeral7.png')

        elif ScoreDraw.number8_image == None:
            ScoreDraw.number8_image = load_image('numeral8.png')

        elif ScoreDraw.number9_image == None:
            ScoreDraw.number9_image = load_image('numeral9.png')


    def update(self, frame_time, Score):
        # 여기서부터 내가 코딩

        # 일의 자리
        draw_first = Score % 10

        # 십의 자리
        draw_second = Score % 100       #----------------------------------여기부터 생각해야함

        # 백의 자리
        draw_third = None

        # 천의 자리
        draw_fourth = None

        # 만의 자리
        draw_fifth = None



        # 기존코드 삭제 해야함.

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