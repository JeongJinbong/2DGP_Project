from pico2d import load_image

import game_framework
import game_world


# Ball Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km/ Hour
RUN_SPEED_MPH = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPH / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


# Ball Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Ball:

    def __init__(self,x= 400, y= 300):
        self.image = load_image('Resource/Image/ball.png')
        self.x, self.y = x, y
        self.dir = 1
        self.frame = 0
        self.gravity = -0.98

    def draw(self):
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.gravity* RUN_SPEED_PPS * game_framework.frame_time

        self.image.clip_draw(int(self.frame)*40,40,40,80,self.x, self.y, 80, 80)


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)%5
