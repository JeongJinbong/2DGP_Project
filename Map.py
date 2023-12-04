from pico2d import load_image, load_music


class Map:
    image = None

    def __init__(self, x=400, y=300):
        self.image = load_image('Resource/Image/BackGround.png')
        self.x, self.y = x, y
        self.bgm = load_music('Resource/Sound/battle.mp3')
        self.bgm.set_volume(20)
        self.bgm.repeat_play()


    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass
