from pico2d import *
import game_framework
from player import Player
from enemy import Enemy
from bullet import Bullet, EnemyBullet
import ranking_state
from draw_score import ScoreDraw
import main_state

name = "MainState"
move_scale = 0.5
player = None
enemies = None
bullet = None
enemy_bullets = None
# enemy_bullet = None
back_ground = None
enemy_kill_count = 0
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
    #x, y = 1, 1
    #for enemy in enemies:
    #    enemy.set_location(x, y)
    #    x = x + 1
    #    y = y + 1


def destroy_world():
    global player, enemies, bullet, enemy_bullets
    del(player)
    del(enemies)
    del(bullet)
    del (enemy_bullets)


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
        self.image = load_image('resource/background_folder/background2.png')
        self.image2 = load_image('resource/background_folder/background2.png')
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
    global enemy_kill_count

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
            enemy_kill_count += 1
            print("kill_count : ", enemy_kill_count)
            #임시 테스트용
            if enemy_kill_count == 10:

                pass


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
