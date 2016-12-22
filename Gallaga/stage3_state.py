from pico2d import *
import game_framework
from player import Player
from enemy import Enemy3
from bullet import Bullet, EnemyBullet
import stage3Point5_state
from draw_score import ScoreDraw
from background import Background3
from player_life import Player_life
import threading
import random
import gameover_state



name = "MainState"
player = None
player_life = None
life = 3
enemies = None
player_bullet = None
enemy_bullets = None
score = 0
enemy_kill_count = 0
font = None
score_data = None
goto_next_stage = False
draw_score = None
scrolling_background = None
enemy_shoot_ok = None

def create_world():
    global player, enemies, player_bullet, enemy_bullets
    global draw_score
    global scrolling_background
    global player_life

    Timer_function(0)
    player_life = Player_life()

    scrolling_background = Background3(800,600)

    draw_score = ScoreDraw()

    player = Player()

    # Generate enemies 60!
    enemies = [Enemy3() for i in range(60)]

    i = 0
    for y in range(4, 8):
        for x in range(6, 21):
            enemies[i].set_location(x, y)
            i += 1


    player_bullet = Bullet()
    enemy_bullets = [EnemyBullet() for i in range(60)]

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
    timer = threading.Timer(0.15, Timer_function, args=[count])
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
    # 여기에 적들이 총알 쏘게 해야함.
    if count<4 :
        timer.start()


def destroy_world():
    global player, enemies, player_bullet, enemy_bullets, font
    global draw_score
    global scrolling_background
    global player_life
    global timer

    for bullet in enemy_bullets:
        if bullet.shooting is True:
            bullet.shooting = False

    timer.cancel()
    del (player_life)
    del (scrolling_background)
    del (player)
    del (enemies)
    del (player_bullet)
    del (enemy_bullets)
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
    global timer
    events = get_events()
    # start var.
    for event in events:
        if life is 0:
            game_framework.push_state(gameover_state)

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
                    stage3Point5_state.get_life(life)
                    stage3Point5_state.get_score(score)
                    game_framework.change_state(stage3Point5_state)
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
    global timer
    scrolling_background.update(frame_time)

    player.update(frame_time)
    player_bullet.update(frame_time, player.x)
    player_life.update(frame_time, life)
    #for enemy in enemies:
    #    for bullets in enemy_bullets:
    #        bullets.update(frame_time, enemy.x)

    draw_score.update(frame_time, score)

    while True:
        select_enemy = random.randrange(1, 60)
        if enemies[select_enemy].is_dead is False:
            break


    if enemy_shoot_ok is True:
        enemies[select_enemy].set_shooting(True)
        enemy_bullets[select_enemy].shooting = True
        enemy_bullets[select_enemy].shoot_start = True
        # enemy_bullets[select_enemy].shooting_sound.play()
        enemy_bullets[select_enemy].update(frame_time, enemies[select_enemy].x, enemies[select_enemy].y)

        print("에너미 슛~, ", select_enemy)
        enemy_shoot_ok = False

    i = 0
    for bullet in enemy_bullets:
        if bullet.shooting is True:
            bullet.update(frame_time, enemies[i].x, enemies[i].y)
            i += 1

    for enemy in enemies:
        enemy.update(frame_time)

    for enemy in enemies:
        if collide(enemy, player_bullet):
            print("collision")
            player_bullet.stop()
            enemy.shooting = False
            enemy.shoot_start = False
            enemy.stop()
            score = score + 100
            print("score : ", score)
            enemy_kill_count += 1
            print("kill_count : ", enemy_kill_count)
            # 임시 테스트용 - 원래는 60
            if enemy_kill_count == 40:
                timer.cancel()
                goto_next_stage = True
                pass

    for bullet in enemy_bullets:
        if collide(player, bullet):
            bullet.stop()
            print("격추됬다 넌 사망했따")
            player.you_dead_huh(True)
            frame_timer_function(0)
            life -= 1

def draw(frame_time):
    clear_canvas()
    scrolling_background.draw()
    player_life.draw()
    player.draw()
    draw_score.draw()
    for enemy in enemies:
        enemy.draw()
    for bullet in enemy_bullets:
        bullet.draw()
    player_bullet.draw()

    if goto_next_stage is True:
        font.draw(200, 330, 'Ready  For  the  Boss!!', (255, 255, 255))
        font.draw(200, 300, 'Press  SpaceBar  to  go  to  Boss  Room', (255, 0, 0))
        player.go_next_stage()

    update_canvas()