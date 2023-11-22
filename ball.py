from pico2d import load_image

import game_framework
import game_world


# Ball Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Ball:

    def __init__(self,x= 400, y= 300):
        self.image = load_image('Resource/Image/ball.png')
        self.x, self.y = x, y
        self.frame = 0

    def draw(self):
        self.image.clip_draw(int(self.frame)*40,40,40,80,self.x, self.y, 80, 80)


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)%5
