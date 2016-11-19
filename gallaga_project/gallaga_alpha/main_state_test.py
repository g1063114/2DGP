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

name = "MainState"
move_scale = 0.5
player = None
enemies = None
bullet = None
enemy_bullets = None
# enemy_bullet = None
back_ground = None
score = 0
font = None
score_data = None


# Game object class here
def create_world():
    global player, enemies, bullet, enemy_bullets
    player = Player()
    enemies = [Enemy() for i in range(40)]
    bullet = Bullet()
    enemy_bullets = [EnemyBullet() for i in range(40)]
#    x, y = 4, 4
#    for enemy in enemies:
#        enemy.set_location(x,y)
#        x = x + 1
#        y = y + 1


def destroy_world():
    global player, enemies, bullet, enemy_bullets
    del(player)
    del(enemies)
    del(bullet)
    del (enemy_bullets)


def enter():
    global back_ground, font
    back_ground = backGround()
    font = load_font('ENCR10B.TTF')

    # new added
    create_world()


def exit():
    global score_data, score, font

    f = open('data_file.txt', 'r')
    score_data = json.load(f)
    f.close()

    score_data.append({'score':score})

    print(score_data)

    f = open('data_file.txt', 'w')
    json.dump(score_data, f)
    f.close()

    destroy_world()

# background image
class backGround:
    def __init__(self):
        # not yet!
        self.pagePoint = 3       # scroll the page
        self.pagePoint2 = 1
        self.image = load_image('background.png')
        self.image2 = load_image('background.png')
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
    global bullet
    events = get_events()
    # start var.
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                bullet.handle_event(event)
            # ranking state
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
                game_framework.change_state(ranking_state)
            else:
                player.handle_event(event)


def update(frame_time):
    global score

    player.update(frame_time)
    bullet.update(frame_time, player.x)

    for enemy in enemies:
        for bullets in enemy_bullets:
            bullets.update(frame_time, enemy.x)

    back_ground.update()

    for enemy in enemies:
        enemy.update(frame_time)
    for enemy in enemies:
        if collide(enemy, bullet):
            print("collision")
            bullet.stop()
            enemy.stop()
            score = score + 100
            print("score : ", score)
#    for Ebullet in enemy_bullet:
#        if collide(player, Ebullet):
#            pass






def draw(frame_time):
    clear_canvas()
    # don't change
    back_ground.draw()
    font.draw(50, 550, 'score: %d' %score)

    # start
    # player.draw()
    player.draw()
    player.draw_bb()
    bullet.draw()
    bullet.draw_bb()

    # enemies
    for enemy in enemies:
        enemy.draw()
        enemy.draw_bb()
    # enemies bullet
    for bullets in enemy_bullets:
        bullets.draw()

    update_canvas()
