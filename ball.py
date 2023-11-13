from pico2d import load_image
import game_world

class Ball:

    def __init__(self,x= 400, y= 300):
        self.image = load_image('Resource/Image/ball.png')
        self.x, self.y = x, y
        self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame*40,40,40,80,self.x, self.y, 80, 80)


    def update(self):
        self.frame = (self.frame + 1) % 5
