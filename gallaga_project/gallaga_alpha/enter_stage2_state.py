import game_framework
# import main_state
import main_state_test
# from main_state_test import score
from pico2d import *
import stage2_state


name = "TitleState"
image = None
nextStage_score = None

def enter():
    global image
    global nextStage_score

    print("%d" %nextStage_score)
    image = load_image('background2.png')
    pass


def exit():
    global image
    del(image)
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
                #game_framework.change_state(main_state)
                game_framework.change_state(stage2_state)
    pass


def draw(frame_time):
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    pass

def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass



