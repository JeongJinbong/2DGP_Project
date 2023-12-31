from pico2d import load_image, draw_rectangle, delay, load_wav

import game_framework
import game_world
import score
from pikachu import Slide, RunLeft, RunRight, Idle, Jump, Spike
from player1 import Player1Slide, Player1RunLeft, Player1RunRight, Player1Idle, Player1Jump, Player1Spike
from player2 import Player2Slide, Player2RunLeft, Player2RunRight, Player2Idle, Player2Jump, Player2Spike

# Ball Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 13.0  # Km/ Hour
RUN_SPEED_MPH = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPH / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Ball Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class Ball:
    spike_ball_sound = None
    score_ball_sound = None

    def __init__(self, x=400, y=300):
        self.image = load_image('Resource/Image/ball.png')
        self.x, self.y = x, y
        self.frame = 0
        self.gravity = -0.25
        self.radius = 40
        self.elasticity = 1.0
        self.velocity_x = 0.0
        self.velocity_y = 1.0

        if not Ball.spike_ball_sound:
            Ball.spike_ball_sound = load_wav('Resource/Sound/WAVE145.wav')
            Ball.score_ball_sound = load_wav('Resource/Sound/WAVE146.wav')
            Ball.spike_ball_sound.set_volume(32)
            Ball.score_ball_sound.set_volume(32)

    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 40, 40, 80, self.x, self.y, 80, 80)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

        self.velocity_y = self.velocity_y + self.gravity * RUN_SPEED_PPS * game_framework.frame_time

        self.x = self.x + self.velocity_x * RUN_SPEED_PPS * game_framework.frame_time
        self.y = self.y + self.velocity_y * RUN_SPEED_PPS * game_framework.frame_time

        if 800 - self.x <= self.radius:
            self.x = 800 - self.radius

            if self.velocity_x >= 0:
                self.velocity_x *= -1.0 * self.elasticity

        if self.x <= 0 + self.radius:
            self.x = 0 + self.radius

            if self.velocity_x <= 0:
                self.velocity_x *= -1.0 * self.elasticity

        if self.y <= 60 + self.radius:
            self.velocity_x *= 0.1  # 공의 속도를 줄임
            self.velocity_y *= 0.1
            self.gravity *= 0.1  # 중력도 줄임

    def get_bb(self):
        return self.x - 40, self.y - 40, self.x + 40, self.y + 40

    def handle_collision(self, group, other):
        match group:
            case 'ball:net':
                self.velocity_x *= 1.0
                self.velocity_y *= -1.0
                self.y += 2
                self.gravity *= 1.0

            case 'ball:leftnet':
                self.velocity_x *= -1.0
                self.gravity *= 1.0

            case 'ball:rightnet':
                self.velocity_x *= -1.0
                self.gravity *= 1.0

            case 'enemy:ball':
                self.velocity_x = -1.5
                self.velocity_y *= -1.0
                self.y += 5
                self.gravity = -0.25
            case 'pikachu:ball':
                if other.state_machine.cur_state == RunRight:
                    self.velocity_x = 1.5
                    self.velocity_y *= -1.0
                    self.y += 3
                    self.gravity = -0.25

                elif other.state_machine.cur_state == RunLeft:
                    self.velocity_x = -1.5
                    self.velocity_y *= -1.0
                    self.y += 3
                    self.gravity = -0.25

                elif other.state_machine.cur_state == Idle:
                    self.velocity_x = 1.0
                    self.velocity_y *= -1.0
                    self.y += 3
                    self.gravity = -0.25

                elif other.state_machine.cur_state == Jump:
                    if other.dir > 0.0:
                        self.velocity_x = 1.5
                        self.velocity_y *= -1.0
                        self.y += 5
                        self.gravity = -0.25

                    elif other.dir == 0.0:
                        self.velocity_y *= -1.0
                        self.y += 5
                        self.gravity = -0.25

                    elif other.dir < 0.0:
                        self.velocity_x = -1.5
                        self.velocity_y *= -1.0
                        self.y += 5
                        self.gravity = -0.25

                elif other.state_machine.cur_state == Slide:
                    self.velocity_x = 0.0
                    self.velocity_y *= -1.0
                    self.y += 3
                    self.gravity = -0.2

                elif other.state_machine.cur_state == Spike:
                    Ball.spike_ball_sound.play()
                    self.velocity_x = 12.0
                    self.velocity_y *= -1.0
                    self.gravity = -0.4
                    self.y += 3

            case 'player1:ball':
                if other.state_machine.cur_state == Player1RunRight:
                    self.velocity_x = 1.5
                    self.velocity_y *= -1.0
                    self.y += 3
                    self.gravity = -0.25

                elif other.state_machine.cur_state == Player1RunLeft:
                    self.velocity_x = -1.5
                    self.velocity_y *= -1.0
                    self.y += 3
                    self.gravity = -0.25

                elif other.state_machine.cur_state == Player1Idle:
                    self.velocity_x = 1.0
                    self.velocity_y *= -1.0
                    self.y += 3
                    self.gravity = -0.25

                elif other.state_machine.cur_state == Player1Jump:
                    if other.dir > 0.0:
                        self.velocity_x = 1.5
                        self.velocity_y *= -1.0
                        self.y += 5
                        self.gravity = -0.25

                    elif other.dir == 0.0:
                        self.velocity_y *= -1.0
                        self.y += 5
                        self.gravity = -0.25

                    elif other.dir < 0.0:
                        self.velocity_x = -1.5
                        self.velocity_y *= -1.0
                        self.y += 5
                        self.gravity = -0.25

                elif other.state_machine.cur_state == Player1Slide:
                    self.velocity_x = 0.0
                    self.velocity_y *= -1.0
                    self.y += 3
                    self.gravity = -0.2

                elif other.state_machine.cur_state == Player1Spike:
                    Ball.spike_ball_sound.play()
                    self.velocity_x = 12.0
                    self.velocity_y *= -1.0
                    self.gravity = -0.4
                    self.y += 3
            case 'player2:ball':
                if other.state_machine.cur_state == Player2RunRight:
                    self.velocity_x = 1.5
                    self.velocity_y *= -1.0
                    self.y += 3
                    self.gravity = -0.25

                elif other.state_machine.cur_state == Player2RunLeft:
                    self.velocity_x = -1.5
                    self.velocity_y *= -1.0
                    self.y += 3
                    self.gravity = -0.25

                elif other.state_machine.cur_state == Player2Idle:
                    self.velocity_x = 1.0
                    self.velocity_y *= -1.0
                    self.y += 3
                    self.gravity = -0.25

                elif other.state_machine.cur_state == Player2Jump:
                    if other.dir > 0.0:
                        self.velocity_x = 1.5
                        self.velocity_y *= -1.0
                        self.y += 5
                        self.gravity = -0.25

                    elif other.dir == 0.0:
                        self.velocity_y *= -1.0
                        self.y += 5
                        self.gravity = -0.25

                    elif other.dir < 0.0:
                        self.velocity_x = -1.5
                        self.velocity_y *= -1.0
                        self.y += 5
                        self.gravity = -0.25

                elif other.state_machine.cur_state == Player2Slide:
                    self.velocity_x = 0.0
                    self.velocity_y *= -1.0
                    self.y += 3
                    self.gravity = -0.2

                elif other.state_machine.cur_state == Player2Spike:
                    Ball.spike_ball_sound.play()
                    self.velocity_x = -12.0
                    self.velocity_y *= -1.0
                    self.gravity = -0.4
                    self.y += 3

    def serve_p1(self):
        self.x, self.y = 50, 500
        self.frame = 0
        self.gravity = -0.25
        self.radius = 40
        self.elasticity = 1.0
        self.velocity_x = 0.0
        self.velocity_y = 1.0

    def serve_p2(self):
        self.x, self.y = 750, 500
        self.frame = 0
        self.gravity = -0.25
        self.radius = 40
        self.elasticity = 1.0
        self.velocity_x = 0.0
        self.velocity_y = 1.0
