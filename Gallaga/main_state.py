#################################################
############# GALLAGA_REMAKEver #################
# Start project in 2016-10-02
# 1. make code layout (2016-10-02)
# 2. add resource(player)
# 3. add game_framework (2016.10.14)
# 4. optimize1 game_framework (2016.10.17)
# 5. enemy_setted (2016.10.20)
# 6. enemy_tile think (2016.10.25)
# 7. enemy_tile add (2016.10.27)
# 8. bullet add(2016.10.30)
# 9. collide check(2016-11-04~)
# 10. rank.py added(2016-11-07)
# 11. move while move (2016-11-08)
# 12. player, enemy .py added (2016-11-14)
#       main_state_test added working on this space!
# 13. Framework well optimized
#   ranking_state working well
#   collide_well
#   bullet_well
#   (2016-11-15)
# 14. Enemy starting attack! (2016-11-17~)
#   attack....(2016-11-19)
# 15. stage2.py added (2016-11-23)
#     enemy can't attack yet...
# 16. pass stage1 score to stage2
#               (2016-11-23)   all-round ver
#   draw_score.py added
# 17. refectoring all these files! (2016-11-24~)
# 18. error edit (2016-11-26)
# 19. admit stage2 (2016-11-28)
# Made by Gunny　
#################################################

from pico2d import *
import random
import os
import game_framework
import title_state
from player import Player
from enemy import Enemy
from bullet import Bullet, EnemyBullet
import ranking_state
import enter_stage2_state
from enter_stage2_state import Getting_score
from draw_score import ScoreDraw

name = "MainState"
move_scale = 0.5
player = None
enemies = None
player_bullet = None
enemy_bullets = None
# enemy_bullet = None
back_ground = None
score = 0
enemy_kill_count = 0
font = None
score_data = None
goto_next_stage = False
push_next_stage_score = None
draw_score = None

# Game object class here
def create_world():
    global player, enemies, player_bullet, enemy_bullets
    global push_next_stage_score
    global draw_score

    draw_score = ScoreDraw()

    push_next_stage_score = Getting_score()
    player = Player()

    # Generate enemies 60!
    enemies = [Enemy() for i in range(60)]

    x = 6
    y = 4
    i = 0
    # set location!
    for y in range(4, 8):
        for x in range(6, 21):
            # print("x,y :: ", x," ", y)
            enemies[i].set_location(x, y)
            i += 1


    player_bullet = Bullet()


def destroy_world():
    global player, enemies, player_bullet, enemy_bullets, font, push_next_stage_score
    global draw_score
    del(player)
    del(enemies)
    del(player_bullet)
    del (enemy_bullets)
    del (font)
    del (push_next_stage_score)
    del (draw_score)


def enter():
    global back_ground, font
    back_ground = backGround()
    font = load_font('resource/ENCR10B.TTF')

    # new added
    create_world()


def exit():
    global score_data, score, font

    f = open('resource/data_file.txt', 'r')
    score_data = json.load(f)
    f.close()

    score_data.append({'score':score})

    print(score_data)

    f = open('resource/data_file.txt', 'w')
    json.dump(score_data, f)
    f.close()

    destroy_world()

# background image
class backGround:
    def __init__(self):
        # not yet!
        self.pagePoint = 3       # scroll the page
        self.pagePoint2 = 1
        self.image = load_image('resource/background_folder/background.png')
        self.image2 = load_image('resource/background_folder/background.png')
    def draw(self):
        self.image.draw(400, 300 * self.pagePoint);
        self.image2.draw(400, 300 * self.pagePoint2);
    def update(self):
        if self.pagePoint > -1:
            self.pagePoint -= 0.001
        else:
            self.pagePoint = 3

        if self.pagePoint2 > -1:
            self.pagePoint2 -= 0.001
        else:
            self.pagePoint2 = 3
        pass
    pass


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
    events = get_events()
    # start var.
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if goto_next_stage is True:
                    # next_stage_score = score
                    # get_stage1_score(score)
                    push_next_stage_score.get_stage1_score(score)
                    game_framework.change_state(enter_stage2_state)
                else:
                    player_bullet.handle_event(event)
            # ranking state
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
                game_framework.change_state(ranking_state)
            else:
                player.handle_event(event)


def update(frame_time):
    global score
    global enemy_kill_count
    global goto_next_stage
    global draw_score

    # global player_bullet

    player.update(frame_time)
    player_bullet.update(frame_time, player.x)

    #for enemy in enemies:
    #    for bullets in enemy_bullets:
    #        bullets.update(frame_time, enemy.x)

    back_ground.update()
    draw_score.update(frame_time, score)

    for enemy in enemies:
        enemy.update(frame_time)
    for enemy in enemies:
        if collide(enemy, player_bullet):
            print("collision")
            player_bullet.stop()
            enemy.stop()
            score = score + 10
            print("score : ", score)
            enemy_kill_count += 1
            print("kill_count : ", enemy_kill_count)
            # 임시 테스트용 - 원래는 40
            if enemy_kill_count == 3:
                goto_next_stage = True
                pass


#    for Ebullet in enemy_bullet:
#        if collide(player, Ebullet):
#            pass






def draw(frame_time):
    # global draw_score
    clear_canvas()
    # don't change
    back_ground.draw()

    # ------------------------------------------------------
    # font.draw(50, 550, 'score: %d' %score)

    # start
    # player.draw()
    player.draw()
    player.draw_bb()
    player_bullet.draw()
    player_bullet.draw_bb()

    draw_score.draw()

    # enemies
    for enemy in enemies:
        enemy.draw()
        enemy.draw_bb()
    # enemies bullet
    #for bullets in enemy_bullets:
    #    bullets.draw()

    if goto_next_stage is True:
        font.draw(200, 300, 'Press SpaceBar to go to NextStage!!')
        # print("Press SpaceBar to go to NextStage!!")

    update_canvas()
