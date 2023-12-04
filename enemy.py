import math

from pico2d import get_time, load_image, load_font, clamp, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT, \
    draw_rectangle
from sdl2 import SDLK_RETURN, SDLK_UP, SDLK_DOWN
import game_world
import game_framework
import play_mode
from behavior_tree import BehaviorTree, Action, Sequence, Condition, Selector

# enemy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 30.0  # Km/ Hour
RUN_SPEED_MPH = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPH / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# enemy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

# enemy Slide Action Speed
SLIDE_TIME_PER_ACTION = 0.75
SLIDE_ACTION_PER_TIME = 1.0 / SLIDE_TIME_PER_ACTION
SLIDE_FRAMES_PER_ACTION = 3

# enemy SLIDE Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
SLIDE_SPEED_KMPH = 10.0  # Km/ Hour
SLIDE_SPEED_MPH = (SLIDE_SPEED_KMPH * 1000.0 / 60.0)
SLIDE_SPEED_MPS = (SLIDE_SPEED_MPH / 60.0)
SLIDE_SPEED_PPS = (SLIDE_SPEED_MPS * PIXEL_PER_METER)

# enemy Jump Action Speed
JUMP_TIME_PER_ACTION = 0.25
JUMP_ACTION_PER_TIME = 1.0 / JUMP_TIME_PER_ACTION
JUMP_FRAMES_PER_ACTION = 3

# enemy JUMP Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
JUMP_SPEED_KMPH = 10.0  # Km/ Hour
JUMP_SPEED_MPH = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
JUMP_SPEED_MPS = (JUMP_SPEED_MPH / 60.0)
JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

animation_names = {'Run', 'Idle'}


class Enemy:
    def __init__(self):
        self.x, self.y = 750, 110
        self.frame = 0
        self.action = 6
        self.speed = 0.0

        self.dir = 0
        self.gravity = -0.25
        self.velocity_y = 11.0
        self.state = 'Idle'
        self.build_behavior_tree()
        self.image = load_image('Resource/Image/pikachu.png')

        self.tx, self.ty = 100, 100

    def get_bb(self):
        return self.x - 45, self.y - 45, self.x + 45, self.y + 45

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        if self.x < 450:
            self.x = 450
        if self.x > 750:
            self.x = 750
        self.bt.run()

    def draw(self):
        self.image.clip_composite_draw(int(self.frame) * 65, self.action * 66, 65, 66, 0, 'h', self.x,
                                       self.y, 104, 105)

        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

    def handle_collision(self, group, other):
        match group:
            case 'enemy:ball':
                pass

    def distance_less_than(self, x1, y1, x2, y2, r):
        distance2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
        return distance2 < (PIXEL_PER_METER * r) ** 2

    def move_slightly_to(self, tx, ty):
        self.dir = math.atan2(ty - self.y, tx - self.x)
        self.speed = RUN_SPEED_PPS
        self.x += (self.speed * math.cos(self.dir) * game_framework.frame_time)

    def move_to_ball(self, r=1):
        self.state = 'Walk'
        if self.x > play_mode.ball.x:
            self.move_slightly_to(play_mode.ball.x-200, play_mode.ball.y)
        elif self.x < play_mode.ball.x:
            self.move_slightly_to(play_mode.ball.x+200, play_mode.ball.y)

        if self.distance_less_than(play_mode.ball.x, play_mode.ball.y, self.x, self.y, r):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING

    def is_ball_nearby(self, distance):
        if self.distance_less_than(play_mode.ball.x, play_mode.ball.y, self.x, self.y, distance):
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL

    def build_behavior_tree(self):
        c1 = Condition("공이 근처에 있는가?", self.is_ball_nearby,15)
        a1 = Action("공으로 이동",self.move_to_ball)

        root = SEQ_chase_ball = Sequence("공을 추적", c1, a1)
        self.bt = BehaviorTree(root)

    def init_position(self):
        self.x = 750
