import game_framework
import main_state
from pico2d import *
import stage2_state


name = "TitleState"
image = None
nextStage_score = None
font = None
score = None


class Getting_score:
    def __init__(self):
        self.score = 0

    def get_stage1_score(self, stage1_score):
        self.score = stage1_score

    def get_score(self):
        return self.score
    pass



#def get_stage1_score(stage1_score):
#

def enter():
    global image
    global nextStage_score
    global font
    global score
    score = Getting_score()
    # score.
    font = load_font('resource/ENCR10B.TTF')
    # print("%d" %nextStage_score)
    image = load_image('resource/background_folder/background2.png')
    pass


def exit():
    global image, font, score
    del(font)
    del(image)
    del(score)
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(stage2_state)
    pass


def draw(frame_time):
    temp = score.get_score()
    clear_canvas()
    image.draw(400, 300)
    font.draw(200, 300, 'Stage2 Start! Press space bar to start game.')
    font.draw(200, 400, 'Score : %d' %temp)
    #  print('%d' %score1)
    update_canvas()
    pass

def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass



