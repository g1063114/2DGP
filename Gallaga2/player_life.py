from pico2d import*

class Player_life:
    image = None

    def __init__(self):
        # 여기서부터 내가 코딩
        self.draw_x, self.draw_y = 550, 50
        self.life = 0


        if self.image == None:
          self.image = load_image('resource/aircraft_folder/pill.png')


    def update(self, frame_time, input_life):
        self.life = input_life
        pass



    def draw(self):
        if self.life is 3:
            self.image.draw(700, 50)
            self.image.draw(720, 50)
            self.image.draw(740, 50)

        elif self.life is 2:

            self.image.draw(700, 50)
            self.image.draw(720, 50)

        elif self.life is 1:
            self.image.draw(700, 50)



    def handle_event(self, event):
        pass

    def stop(self):
        pass
