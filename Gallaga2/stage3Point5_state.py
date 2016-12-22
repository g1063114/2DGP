from pico2d import *
import game_framework
from player import Player
from bullet import Bullet, BossBullet
import stage2_state
from draw_score import ScoreDraw
from background import Background3
from player_life import Player_life
import threading
import random
import win_state
import gameover_state
from enemy import Boss3



name = "MainState"
player = None
player_life = None
life = 3
player_bullet = None
score = 0
enemy_kill_count = 0
font = None
score_data = None
goto_next_stage = False
draw_score = None
scrolling_background = None
enemy_shoot_ok = None
boss = None
boss_bullets = None


def create_world():
    global player, player_bullet
    global draw_score
    global scrolling_background
    global player_life
    global boss
    global boss_bullets

    boss_bullets = [BossBullet() for i in range(3)]
    boss_bullets[0].local = 0
    boss_bullets[1].local = 1
    boss_bullets[2].local = 2

    boss = Boss3()
    boss.set_location(1,3)
    Timer_function(0)
    player_life = Player_life()

    scrolling_background = Background3(800,600)

    draw_score = ScoreDraw()

    player = Player()

    # Generate enemies 60!


    player_bullet = Bullet()

def get_score(input):
    global score
    score = input

def get_life(input):
    global life
    life = input
    print("life : ", life)



def Timer_function(count):
    global enemy_shoot_ok
    global timer

    count += 1
    timer = threading.Timer(0.4, Timer_function, args=[count])
    #print("타이머 호출")
    # 여기에 적들이 총알 쏘게 해야함.
    enemy_shoot_ok = True
    if count<5000 :
        timer.start()

def frame_timer_function(count):
    global timer
    global player

    player.frame += 1
    count += 1
    timer = threading.Timer(0.3, frame_timer_function, args=[count])
    print("타이머 호출")
    if count<4 :
        timer.start()


def destroy_world():
    global player, player_bullet, font
    global draw_score
    global scrolling_background
    global player_life
    global timer
    global boss
    global boss_bullets


    timer.cancel()

    del (boss_bullets)
    del (boss)
    del (player_life)
    del (scrolling_background)
    del (player)
    del (player_bullet)
    del (font)
    del (draw_score)



def enter():
    global back_ground, font
    font = load_font('resource/kenvector_future.TTF')

    # new added
    create_world()


def exit():
    destroy_world()

def save_score():
    global score_data, score

    f = open('resource/data_file.txt', 'r')
    score_data = json.load(f)
    f.close()

    score_data.append({'score':score})

    print(score_data)

    f = open('resource/data_file.txt', 'w')
    json.dump(score_data, f)
    f.close()



def pause():
    pass


def resume():
    pass

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False
    return True


def handle_events(frame_time):
    global player_bullet
    global goto_next_stage
    global next_stage_score
    global score
    global timer
    events = get_events()
    # start var.
    if life is 0:
        game_framework.push_state(gameover_state)
    for event in events:
        if event.type == SDL_QUIT:
            save_score()
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                save_score()
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if goto_next_stage is True:
                    # next_stage_score = score
                    # get_stage1_score(score)
                    score += 1000
                    game_framework.change_state(win_state)
                else:
                    player_bullet.handle_event(event)
                    player.shooting_sound.play()
            # ranking state
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_c):
                timer.cancel()
                goto_next_stage = True
            else:
                player.handle_event(event)


def update(frame_time):
    global score
    global enemy_kill_count
    global goto_next_stage
    global draw_score
    global player_life
    global enemy_shoot_ok
    global life
    global boss
    global boss_bullets


    scrolling_background.update(frame_time)

    player.update(frame_time)
    player_bullet.update(frame_time, player.x)
    player_life.update(frame_time, life)
    #for enemy in enemies:
    #    for bullets in enemy_bullets:
    #        bullets.update(frame_time, enemy.x)
    if collide(player_bullet, boss):
        player_bullet.stop()
        boss.life -= 1

    for bullet in boss_bullets:
        if collide(player, bullet):
            bullet.stop()
            print("격추됬다 넌 사망했따")
            player.you_dead_huh(True)
            frame_timer_function(0)
            life -= 1


    for i in range(3):
        if enemy_shoot_ok is True:
            boss_bullets[i].shooting = True
            boss_bullets[i].shoot_start = True
            # enemy_bullets[select_enemy].shooting_sound.play()

    enemy_shoot_ok = False

    for i in range(3):
        boss_bullets[i].update(frame_time, boss.x, boss.y - 42)

    boss.update(frame_time)
    draw_score.update(frame_time, score)

    if boss.life is 0:
        boss.stop()
        goto_next_stage = True




def draw(frame_time):
    clear_canvas()
    scrolling_background.draw()
    player_life.draw()
    player.draw()
    draw_score.draw()
    player_bullet.draw()
    boss.draw()

    for bullets in boss_bullets:
        bullets.draw()

    if goto_next_stage is True:
        font.draw(200, 300, 'Press SpaceBar to go to NextStage!!', (255, 0, 0))
        player.go_next_stage()

    update_canvas()