import game_framework
from pico2d import *
import json

import title_state
import main_state_test


name = "TitleState"
image = None
font = None

def enter():
    global image
    image = load_image('blackboard.png')
    global font
    font = load_font('ENCR10B.TTF', 40)

def exit():
    global image
    del(image)


def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)



def update(frame_time):
    pass

def bubble_sort(data):
    for i in range(0, len(data)):
        for j in range(i+1, len(data)):
           if data[i]['score'] < data[j]['score']:
                #헐 대박 이게 되다니
                #스왑이 이렇게 간단하게 되다니
                data[i]['score'], data[j]['score']= data[j]['score'], data[i]['score']


# redible upgrade!
def draw_ranking():
    f = open('data_file.txt', 'r')
    score_data = json.load(f)
    f.close()

    bubble_sort(score_data)
    score_data = score_data[:10]
    font.draw(300, 500, '[RANKING]', (200, 100, 50))

    y = 0
    for y in range(len(score_data)):
        font.draw(50, 400-40*y, 'score : %d' %
                  (score_data[y]['score']), (125, 100, 50))


def draw(frame_time):
    global image
    global font
    clear_canvas()
    image.draw(400, 300)
    draw_ranking()

    update_canvas()
