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
        self.first = 0
        self.second = 0
        self.third = 0
        self.fourth = 0
        self.fifth = 0

        if self.number0_image == None:
            self.number0_image = load_image('resource/number_folder/numeral0.png')

        if self.number1_image == None:
          self.number1_image = load_image('resource/number_folder/numeral1.png')

        if self.number2_image == None:
          self.number2_image = load_image('resource/number_folder/numeral2.png')

        if self.number3_image == None:
          self.number3_image = load_image('resource/number_folder/numeral3.png')

        if self.number4_image == None:
          self.number4_image = load_image('resource/number_folder/numeral4.png')

        if self.number5_image == None:
          self.number5_image = load_image('resource/number_folder/numeral5.png')

        if self.number6_image == None:
          self.number6_image = load_image('resource/number_folder/numeral6.png')

        if self.number7_image == None:
          self.number7_image = load_image('resource/number_folder/numeral7.png')

        if self.number8_image == None:
          self.number8_image = load_image('resource/number_folder/numeral8.png')

        if self.number9_image == None:
          self.number9_image = load_image('resource/number_folder/numeral9.png')


    def update(self, frame_time, input_score):
        # 여기서부터 내가 코딩

        # 일의 자리
        self.first = input_score % 10

        # 십의 자리
        self.second = int((input_score % 100) / 10)       #----------------------------------여기부터 생각해야함

        # 백의 자리
        self.third = int((input_score % 1000)/100)

        # 천의 자리
        self.fourth = int((input_score & 10000)/1000)

        # 만의 자리
        self.fifth = int(input_score/10000)



        # 기존코드 삭제 해야함.

    def draw(self):
        # ont.draw(50, 550, 'score: %d' % score)
        # self.image.draw(self.x, self.y)

        # fifth
        if self.fifth is 0:
            self.number0_image.draw(100, 550)
        elif self.fifth is 1:
            self.number1_image.draw(100, 550)
        elif self.fifth is 2:
            self.number2_image.draw(100, 550)
        elif self.fifth is 3:
            self.number3_image.draw(100, 550)
        elif self.fifth is 4:
            self.number4_image.draw(100, 550)
        elif self.fifth is 5:
            self.number5_image.draw(100, 550)
        elif self.fifth is 0:
            self.number6_image.draw(100, 550)
        elif self.fifth is 0:
            self.number7_image.draw(100, 550)
        elif self.fifth is 0:
            self.number8_image.draw(100, 550)
        elif self.fifth is 0:
            self.number9_image.draw(100, 550)


        # fourth
        if self.fourth is 0:
            self.number0_image.draw(120, 550)
        elif self.fourth is 1:
            self.number1_image.draw(120, 550)
        elif self.fourth is 2:
            self.number2_image.draw(120, 550)
        elif self.fourth is 3:
            self.number3_image.draw(120, 550)
        elif self.fourth is 4:
            self.number4_image.draw(120, 550)
        elif self.fourth is 5:
            self.number5_image.draw(120, 550)
        elif self.fourth is 0:
            self.number6_image.draw(120, 550)
        elif self.fourth is 0:
            self.number7_image.draw(120, 550)
        elif self.fourth is 0:
            self.number8_image.draw(120, 550)
        elif self.fourth is 0:
            self.number9_image.draw(120, 550)

        # third
        if self.third is 0:
            self.number0_image.draw(140, 550)
        elif self.third is 1:
            self.number1_image.draw(140, 550)
        elif self.third is 2:
            self.number2_image.draw(140, 550)
        elif self.third is 3:
            self.number3_image.draw(140, 550)
        elif self.third is 4:
            self.number4_image.draw(140, 550)
        elif self.third is 5:
            self.number5_image.draw(140, 550)
        elif self.third is 0:
            self.number6_image.draw(140, 550)
        elif self.third is 0:
            self.number7_image.draw(140, 550)
        elif self.third is 0:
            self.number8_image.draw(140, 550)
        elif self.third is 0:
            self.number9_image.draw(140, 550)

        # second
        if self.second is 0:
            self.number0_image.draw(160, 550)
        elif self.second is 1:
            self.number1_image.draw(160, 550)
        elif self.second is 2:
            self.number2_image.draw(160, 550)
        elif self.second is 3:
            self.number3_image.draw(160, 550)
        elif self.second is 4:
            self.number4_image.draw(160, 550)
        elif self.second is 5:
            self.number5_image.draw(160, 550)
        elif self.second is 0:
            self.number6_image.draw(160, 550)
        elif self.second is 0:
            self.number7_image.draw(160, 550)
        elif self.second is 0:
            self.number8_image.draw(160, 550)
        elif self.second is 0:
            self.number9_image.draw(160, 550)


        # first
        if self.first is 0:
            self.number0_image.draw(180, 550)
        elif self.first is 1:
            self.number1_image.draw(180, 550)
        elif self.first is 2:
            self.number2_image.draw(180, 550)
        elif self.first is 3:
            self.number3_image.draw(180, 550)
        elif self.first is 4:
            self.number4_image.draw(180, 550)
        elif self.first is 5:
            self.number5_image.draw(180, 550)
        elif self.first is 0:
            self.number6_image.draw(180, 550)
        elif self.first is 0:
            self.number7_image.draw(180, 550)
        elif self.first is 0:
            self.number8_image.draw(180, 550)
        elif self.first is 0:
            self.number9_image.draw(180, 550)



    def handle_event(self, event):
        pass

    def stop(self):
        self.shooting = False
        self.y = -30