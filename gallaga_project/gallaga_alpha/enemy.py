from pico2d import*
import random

class Enemy:
    def __init__(self):
        self.x, self.y = 0, 0
    def update(self, frash_time):
        pass
    def get_bb(self):
        pass
    pass


#화면을 분할해서 배열에 넣어주고
#그 배열번호를 랜덤하게 들어가게 해야되는데... 물론 중복은 피하고
class airplane_enemy:
    def __init__(self):
        self.x, self.y = random.randint(-100, 800), random.randint(-100, 600)
        self.ownX = random.randint(100, 700)
        self.ownY = random.randint(300, 500)

        #Add tile set.
        #To deny overact
        self.tileX = 0
        self.tileY = 0
        #self.ownX = 0
        #self.ownY = 0
        self.image = load_image('enemyBlack.png')

    def update(self):
        #enemy should find own place
        if (self.x > self.ownX):
            self.x -= move_scale
        elif self.x < self.ownX:
            self.x += move_scale
        elif self.y > self.ownY:
            self.y -= move_scale
        elif self.y < self.ownY:
            self.y += move_scale
        pass
    def draw(self):
        self.image.draw(self.x, self.y)
    pass

class bullet:
    def __init__(self):

        pass
    def draw(self):
        pass
    pass
