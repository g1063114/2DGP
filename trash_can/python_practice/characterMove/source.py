from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

x = 0
frame = 0
while ( x < 800 ):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()
    print('프레임은 : ',frame)
    frame = (frame + 1) % 8
    x += 5
    delay(0.05)
    get_events()

close_canvas()