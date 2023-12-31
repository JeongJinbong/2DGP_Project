from pico2d import (get_time, load_image, load_font, clamp, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT,
                    draw_rectangle, load_wav)
from sdl2 import SDLK_RETURN, SDLK_UP, SDLK_DOWN

import game_world
import game_framework

# player2 Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 30.0  # Km/ Hour
RUN_SPEED_MPH = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPH / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# player2 Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

# player2 Player2Slide Action Speed
Player2Slide_TIME_PER_ACTION = 0.75
Player2Slide_ACTION_PER_TIME = 1.0 / Player2Slide_TIME_PER_ACTION
Player2Slide_FRAMES_PER_ACTION = 3

# player2 Player2Slide Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
Player2Slide_SPEED_KMPH = 10.0  # Km/ Hour
Player2Slide_SPEED_MPH = (Player2Slide_SPEED_KMPH * 1000.0 / 60.0)
Player2Slide_SPEED_MPS = (Player2Slide_SPEED_MPH / 60.0)
Player2Slide_SPEED_PPS = (Player2Slide_SPEED_MPS * PIXEL_PER_METER)

# player2 Player2Jump Action Speed
Player2Jump_TIME_PER_ACTION = 0.25
Player2Jump_ACTION_PER_TIME = 1.0 / Player2Jump_TIME_PER_ACTION
Player2Jump_FRAMES_PER_ACTION = 3

# player2 Player2Jump Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
Player2Jump_SPEED_KMPH = 10.0  # Km/ Hour
Player2Jump_SPEED_MPH = (Player2Jump_SPEED_KMPH * 1000.0 / 60.0)
Player2Jump_SPEED_MPS = (Player2Jump_SPEED_MPH / 60.0)
Player2Jump_SPEED_PPS = (Player2Jump_SPEED_MPS * PIXEL_PER_METER)

PressRight = False
PressLeft = False


def enter_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RETURN


def right_stay(e):
    global PressRight
    if e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT:
        PressRight = True
    if e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT:
        PressRight = False
    return PressRight


def left_stay(e):
    global PressLeft
    if e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT:
        PressLeft = True
    if e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT:
        PressLeft = False
    return PressLeft


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT


def upkey_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP


def upkey_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP


def downkey_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_DOWN


def downkey_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_DOWN


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def time_out(e):
    return e[0] == 'TIME_OUT'


def on_land(e):
    return e[0] == 'ON_LAND'


class Player2Idle:
    @staticmethod
    def enter(player2, e):
        player2.frame = 0
        player2.action = 6
        player2.dir = 0
        player2.speed = 0

    @staticmethod
    def exit(player2, e):
        pass

    @staticmethod
    def do(player2):
        player2.frame = (player2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

    @staticmethod
    def draw(player2):
        player2.image.clip_composite_draw(int(player2.frame) * 65, player2.action * 66, 65, 66, 0, 'h',
                                          player2.x, player2.y, 104, 105)

class Player2RunRight:
    @staticmethod
    def enter(player2, e):
        player2.dir = 1
        player2.speed = RUN_SPEED_PPS
        player2.action = 6
        player2.frame = 0

    @staticmethod
    def exit(player2, e):
        pass

    @staticmethod
    def do(player2):
        player2.frame = (player2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

    @staticmethod
    def draw(player2):
        player2.image.clip_composite_draw(int(player2.frame) * 65, player2.action * 66, 65, 66, 0, 'h',
                                          player2.x, player2.y, 104, 105)

class Player2RunLeft:
    @staticmethod
    def enter(player2, e):
        player2.dir = -1
        player2.speed = RUN_SPEED_PPS
        player2.action = 6
        player2.frame = 0

    @staticmethod
    def exit(player2, e):
        pass

    @staticmethod
    def do(player2):
        player2.frame = (player2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

    @staticmethod
    def draw(player2):
        player2.image.clip_composite_draw(int(player2.frame) * 65, player2.action * 66, 65, 66,0, 'h' ,
                                          player2.x, player2.y, 104, 105)

class Player2Slide:

    @staticmethod
    def enter(player2, e):
        player2.frame = 0
        player2.action = 3
        player2.velocity_y = 5
        player2.Player2Slide_sound.play()


    @staticmethod
    def exit(player2, e):
        player2.velocity_y = 11

    @staticmethod
    def do(player2):
        player2.frame = ((player2.frame + Player2Slide_FRAMES_PER_ACTION * Player2Slide_ACTION_PER_TIME * game_framework.frame_time)
                         % 3)
        player2.velocity_y = player2.velocity_y + player2.gravity * Player2Slide_SPEED_PPS * game_framework.frame_time
        player2.y = player2.y + player2.velocity_y * Player2Slide_SPEED_PPS * game_framework.frame_time

        if player2.y <= 110:
            player2.state_machine.handle_event(('ON_LAND', 0))

    @staticmethod
    def draw(player2):
        if player2.dir >= 0.0:
            player2.image.clip_draw(int(player2.frame) * 64, player2.action * 70, 64, 62, player2.x, player2.y, 104,
                                105)
        elif player2.dir < 0.0:
            player2.image.clip_composite_draw(int(player2.frame) * 64, player2.action * 70, 64, 62, 0, 'h', player2.x,
                                              player2.y, 104, 105)

class Player2Jump:

    @staticmethod
    def enter(player2, e):
        player2.frame = 0
        player2.wait_time = get_time()
        player2.action = 5
    @staticmethod
    def exit(player2, e):
        if on_land(e):
            player2.velocity_y = 11
    @staticmethod
    def do(player2):
        player2.frame = (player2.frame + Player2Jump_FRAMES_PER_ACTION * Player2Jump_ACTION_PER_TIME * game_framework.frame_time) % 3
        player2.velocity_y = player2.velocity_y + player2.gravity * Player2Jump_SPEED_PPS * game_framework.frame_time
        player2.y = player2.y + player2.velocity_y * Player2Jump_SPEED_PPS * game_framework.frame_time

        if player2.y <= 110:
            player2.state_machine.handle_event(('ON_LAND', 0))

    @staticmethod
    def draw(player2):
        player2.image.clip_composite_draw(int(player2.frame) * 65, player2.action * 66, 65, 66, 0, 'h',
                                          player2.x, player2.y, 104, 105)

class Player2Spike:

    @staticmethod
    def enter(player2, e):
        player2.frame = 0
        player2.wait_time = get_time()
        player2.action = 4
        player2.Player2Spike_sound.play()

    @staticmethod
    def exit(player2, e):
        pass

    @staticmethod
    def do(player2):
        player2.frame = (player2.frame + Player2Jump_FRAMES_PER_ACTION * Player2Jump_ACTION_PER_TIME * game_framework.frame_time) % 3
        player2.velocity_y = player2.velocity_y + player2.gravity * Player2Jump_SPEED_PPS * game_framework.frame_time
        player2.y = player2.y + player2.velocity_y * Player2Jump_SPEED_PPS * game_framework.frame_time

        if player2.y <= 110:
            player2.state_machine.handle_event(('ON_LAND', 0))

        if get_time() - player2.wait_time > 0.5:
            player2.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def draw(player2):
        player2.image.clip_composite_draw(int(player2.frame) * 64, player2.action * 68, 65, 64, 0, 'h',
                                          player2.x, player2.y, 104, 105)

class StateMachine:
    def __init__(self, player2):
        self.player2 = player2
        self.cur_state = Player2Idle
        self.transitions = {
            Player2Slide: {on_land: Player2Idle},
            Player2Idle: {enter_down: Player2Slide, right_down: Player2RunRight, left_down: Player2RunLeft, upkey_down: Player2Jump, right_stay: Player2RunRight,
                   left_stay: Player2RunLeft},
            Player2RunRight: {enter_down: Player2Slide, right_up: Player2Idle, left_down: Player2Idle, upkey_down: Player2Jump},
            Player2RunLeft: {enter_down: Player2Slide, left_up: Player2Idle, right_down: Player2Idle, upkey_down: Player2Jump},
            Player2Jump: {on_land: Player2Idle, enter_down: Player2Spike},
            Player2Spike: {on_land: Player2Idle, time_out: Player2Jump}
        }

    def start(self):
        self.cur_state.enter(self.player2, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.player2)
        self.player2.x += self.player2.dir * self.player2.speed * game_framework.frame_time
        if self.player2.x < 450:
            self.player2.x = 450
        if self.player2.x > 750:
            self.player2.x = 750

    def draw(self):
        self.cur_state.draw(self.player2)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.player2, e)
                self.cur_state = next_state
                self.cur_state.enter(self.player2, e)
                return True

        return False


class Player2:
    image = None
    Player2Spike_sound= None
    Player2Slide_sound= None

    def __init__(self):
        self.x, self.y = 750, 110
        self.frame = 0
        self.action = 6
        self.dir = 0
        self.gravity = -0.25
        self.velocity_y = 11.0
        self.image = load_image('Resource/Image/pikachu.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

        if not Player2.Player2Spike_sound:
            Player2.Player2Spike_sound = load_wav('Resource/Sound/WAVE141.wav')
            Player2.Player2Slide_sound = load_wav('Resource/Sound/WAVE142.wav')
            Player2.Player2Slide_sound.set_volume(32)
            Player2.Player2Spike_sound.set_volume(32)

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
            case 'player2:ball':
                pass

    def init_position(self):
        self. x = 750

