from pico2d import *
import game_framework
from player import Player
from enemy import Enemy
from bullet import Bullet, EnemyBullet
import ranking_state
import stage3Point5_state
from draw_score import ScoreDraw
from background import Background3
from player_life import Player_life



name = "MainState"
player = None
enemies = None
player_bullet = None
enemy_bullets = None
back_ground = None
score = 0
player_life = None
life = 0
enemy_kill_count = 0
font = None
score_data = None
goto_next_stage = False
draw_score = None
scrolling_background = None

# Game object class here
def create_world():
    global player, enemies, player_bullet, enemy_bullets
    global draw_score
    global scrolling_background
    global player_life

    player_life = Player_life()

    scrolling_background = Background3(800,600)

    draw_score = ScoreDraw()

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
    global scrolling_background
    global player_life

    del(player_life)
    del(scrolling_background)
    del(player)
    del(enemies)
    del(player_bullet)
    del (enemy_bullets)
    del (font)
    del (draw_score)

def get_score(input):
    global score
    score = input

def get_life(input):
    global life
    life = input
    print("life : ", life)

def enter():
    global back_ground, font
    back_ground = backGround()
    font = load_font('resource/ENCR10B.TTF')

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
            else:
                player.handle_event(event)


def update(frame_time):
    global score
    global enemy_kill_count
    global goto_next_stage
    global draw_score
    global player_life

    player_life.update(frame_time, life)


    scrolling_background.update(frame_time)

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
            score = score + 100
            print("score : ", score)
            enemy_kill_count += 1
            print("kill_count : ", enemy_kill_count)
            # 임시 테스트용 - 원래는 40
            if enemy_kill_count == 5:
                goto_next_stage = True
                pass


#    for Ebullet in enemy_bullet:
#        if collide(player, Ebullet):
#            pass






def draw(frame_time):
    # global draw_score
    clear_canvas()
    # don't change
    # back_ground.draw()
    scrolling_background.draw()
    # ------------------------------------------------------
    # font.draw(50, 550, 'score: %d' %score)
    player_life.draw()

    # start
    player.draw()
    # player.draw_bb()
    player_bullet.draw()
    # player_bullet.draw_bb()

    draw_score.draw()

    # enemies
    for enemy in enemies:
        enemy.draw()
        # enemy.draw_bb()
    # enemies bullet
    #for bullets in enemy_bullets:
    #    bullets.draw()

    if goto_next_stage is True:
        font.draw(200, 330, 'Get Ready For the Boss!!')
        font.draw(200, 300, 'Press SpaceBar to go to Boss Room')
        player.go_next_stage()
        # print("Press SpaceBar to go to NextStage!!")

    update_canvas()
