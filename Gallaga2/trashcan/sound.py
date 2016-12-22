# sound added. 2016.12-12
from pico2d import*

class HitSound:
    def __init__(self):
        self.bgm = load_music('resource/sound/shooting.ogg')
        self.bgm.set_volume(128)

class CrushSound:
    def __init__(self):
        self.bgm = load_music('resource/sound/break.ogg')
        self.bgm.set_volume(128)