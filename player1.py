from pico2d import (get_time, load_image, load_font, clamp, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT,
                    draw_rectangle, load_wav)
from sdl2 import SDLK_RETURN, SDLK_UP, SDLK_DOWN, SDLK_d, SDLK_a, SDLK_w, SDLK_s

import game_world
import game_framework

# player1 Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 30.0  # Km/ Hour
RUN_SPEED_MPH = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPH / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# player1 Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

# player1 Slide Action Speed
SLIDE_TIME_PER_ACTION = 0.75
SLIDE_ACTION_PER_TIME = 1.0 / SLIDE_TIME_PER_ACTION
SLIDE_FRAMES_PER_ACTION = 3

# player1 SLIDE Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
SLIDE_SPEED_KMPH = 10.0  # Km/ Hour
SLIDE_SPEED_MPH = (SLIDE_SPEED_KMPH * 1000.0 / 60.0)
SLIDE_SPEED_MPS = (SLIDE_SPEED_MPH / 60.0)
SLIDE_SPEED_PPS = (SLIDE_SPEED_MPS * PIXEL_PER_METER)

# player1 Jump Action Speed
JUMP_TIME_PER_ACTION = 0.25
JUMP_ACTION_PER_TIME = 1.0 / JUMP_TIME_PER_ACTION
JUMP_FRAMES_PER_ACTION = 3

# player1 JUMP Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
JUMP_SPEED_KMPH = 10.0  # Km/ Hour
JUMP_SPEED_MPH = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
JUMP_SPEED_MPS = (JUMP_SPEED_MPH / 60.0)
JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

PressRight = False
PressLeft = False


def enter_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RETURN


def right_stay(e):
    global PressRight
    if e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d:
        PressRight = True
    if e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d:
        PressRight = False
    return PressRight


def left_stay(e):
    global PressLeft
    if e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a:
        PressLeft = True
    if e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a:
        PressLeft = False
    return PressLeft


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a


def upkey_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_w


def upkey_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_w


def downkey_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_s


def downkey_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_s


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def time_out(e):
    return e[0] == 'TIME_OUT'


def on_land(e):
    return e[0] == 'ON_LAND'


class Idle:
    @staticmethod
    def enter(player1, e):
        player1.frame = 0
        player1.action = 6
        player1.dir = 0
        player1.speed = 0

    @staticmethod
    def exit(player1, e):
        pass

    @staticmethod
    def do(player1):
        player1.frame = (player1.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

    @staticmethod
    def draw(player1):
        player1.image.clip_draw(int(player1.frame) * 65, player1.action * 66, 65, 66, player1.x, player1.y, 104, 105)


class RunRight:
    @staticmethod
    def enter(player1, e):
        player1.dir = 1
        player1.speed = RUN_SPEED_PPS
        player1.action = 6
        player1.frame = 0

    @staticmethod
    def exit(player1, e):
        pass

    @staticmethod
    def do(player1):
        player1.frame = (player1.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

    @staticmethod
    def draw(player1):
        player1.image.clip_draw(int(player1.frame) * 65, player1.action * 66, 65, 66, player1.x, player1.y, 104, 105)


class RunLeft:
    @staticmethod
    def enter(player1, e):
        player1.dir = -1
        player1.speed = RUN_SPEED_PPS
        player1.action = 6
        player1.frame = 0

    @staticmethod
    def exit(player1, e):
        pass

    @staticmethod
    def do(player1):
        player1.frame = (player1.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

    @staticmethod
    def draw(player1):
        player1.image.clip_draw(int(player1.frame) * 65, player1.action * 66, 65, 66, player1.x, player1.y, 104, 105)


class Slide:

    @staticmethod
    def enter(player1, e):
        player1.frame = 0
        player1.action = 3
        player1.velocity_y = 5
        player1.slide_sound.play()


    @staticmethod
    def exit(player1, e):
        player1.velocity_y = 11

    @staticmethod
    def do(player1):
        player1.frame = ((player1.frame + SLIDE_FRAMES_PER_ACTION * SLIDE_ACTION_PER_TIME * game_framework.frame_time)
                         % 3)
        player1.velocity_y = player1.velocity_y + player1.gravity * SLIDE_SPEED_PPS * game_framework.frame_time
        player1.y = player1.y + player1.velocity_y * SLIDE_SPEED_PPS * game_framework.frame_time

        if player1.y <= 110:
            player1.state_machine.handle_event(('ON_LAND', 0))

    @staticmethod
    def draw(player1):
        if player1.dir >= 0.0:
            player1.image.clip_draw(int(player1.frame) * 64, player1.action * 70, 64, 62, player1.x, player1.y, 104,
                                105)
        elif player1.dir < 0.0:
            player1.image.clip_composite_draw(int(player1.frame) * 64, player1.action * 70, 64, 62, 0, 'h', player1.x,
                                              player1.y, 104, 105)

class Jump:

    @staticmethod
    def enter(player1, e):
        player1.frame = 0
        player1.wait_time = get_time()
        player1.action = 5
    @staticmethod
    def exit(player1, e):
        if on_land(e):
            player1.velocity_y = 11
    @staticmethod
    def do(player1):
        player1.frame = (player1.frame + JUMP_FRAMES_PER_ACTION * JUMP_ACTION_PER_TIME * game_framework.frame_time) % 3
        player1.velocity_y = player1.velocity_y + player1.gravity * JUMP_SPEED_PPS * game_framework.frame_time
        player1.y = player1.y + player1.velocity_y * JUMP_SPEED_PPS * game_framework.frame_time

        if player1.y <= 110:
            player1.state_machine.handle_event(('ON_LAND', 0))

    @staticmethod
    def draw(player1):
        player1.image.clip_draw(int(player1.frame) * 65, player1.action * 66, 65, 66, player1.x, player1.y, 104, 105)


class Spike:

    @staticmethod
    def enter(player1, e):
        player1.frame = 0
        player1.wait_time = get_time()
        player1.action = 4
        player1.spike_sound.play()

    @staticmethod
    def exit(player1, e):
        pass

    @staticmethod
    def do(player1):
        player1.frame = (player1.frame + JUMP_FRAMES_PER_ACTION * JUMP_ACTION_PER_TIME * game_framework.frame_time) % 3
        player1.velocity_y = player1.velocity_y + player1.gravity * JUMP_SPEED_PPS * game_framework.frame_time
        player1.y = player1.y + player1.velocity_y * JUMP_SPEED_PPS * game_framework.frame_time

        if player1.y <= 110:
            player1.state_machine.handle_event(('ON_LAND', 0))

        if get_time() - player1.wait_time > 0.5:
            player1.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def draw(player1):
        player1.image.clip_draw(int(player1.frame) * 64, player1.action * 68, 65, 64, player1.x, player1.y+5, 104, 105)


class StateMachine:
    def __init__(self, player1):
        self.player1 = player1
        self.cur_state = Idle
        self.transitions = {
            Slide: {on_land: Idle},
            Idle: {space_down: Slide, right_down: RunRight, left_down: RunLeft, upkey_down: Jump, right_stay: RunRight,
                   left_stay: RunLeft},
            RunRight: {space_down: Slide, right_up: Idle, left_down: Idle, upkey_down: Jump},
            RunLeft: {space_down: Slide, left_up: Idle, right_down: Idle, upkey_down: Jump},
            Jump: {on_land: Idle, space_down: Spike},
            Spike: {on_land: Idle, time_out: Jump}
        }

    def start(self):
        self.cur_state.enter(self.player1, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.player1)
        self.player1.x += self.player1.dir * self.player1.speed * game_framework.frame_time
        if self.player1.x > 350:
            self.player1.x = 350
        elif self.player1.x < 54:
            self.player1.x = 54

    def draw(self):
        self.cur_state.draw(self.player1)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.player1, e)
                self.cur_state = next_state
                self.cur_state.enter(self.player1, e)
                return True

        return False


class Player1:
    image = None
    spike_sound= None
    slide_sound= None

    def __init__(self):
        self.x, self.y = 50, 110
        self.frame = 0
        self.action = 6
        self.dir = 0
        self.gravity = -0.25
        self.velocity_y = 11.0
        self.image = load_image('Resource/Image/pikachu.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

        if not Player1.spike_sound:
            Player1.spike_sound = load_wav('Resource/Sound/WAVE141.wav')
            Player1.slide_sound = load_wav('Resource/Sound/WAVE142.wav')
            Player1.slide_sound.set_volume(32)
            Player1.spike_sound.set_volume(32)

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def update(self):
        self.state_machine.handle_event(('None', ()))
        self.state_machine.update()

    def draw(self):
        self.state_machine.draw()

    def get_bb(self):
        return self.x - 45, self.y - 45, self.x + 45, self.y + 45

    def handle_collision(self, group, other):
        match group:
            case 'player1:ball':
                pass

    def init_position(self):
        self. x = 50

