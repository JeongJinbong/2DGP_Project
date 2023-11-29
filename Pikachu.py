from pico2d import get_time, load_image, load_font, clamp, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT
from sdl2 import SDLK_RETURN, SDLK_UP, SDLK_DOWN

import game_world
import game_framework

# Pikachu Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km/ Hour
RUN_SPEED_MPH = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPH / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Pikachu Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

# Pikachu Slide Action Speed
SLIDE_TIME_PER_ACTION = 0.75
SLIDE_ACTION_PER_TIME = 1.0 / SLIDE_TIME_PER_ACTION
SLIDE_FRAMES_PER_ACTION = 3

# Pikachu SLIDE Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
SLIDE_SPEED_KMPH = 10.0  # Km/ Hour
SLIDE_SPEED_MPH = (SLIDE_SPEED_KMPH * 1000.0 / 60.0)
SLIDE_SPEED_MPS = (SLIDE_SPEED_MPH / 60.0)
SLIDE_SPEED_PPS = (SLIDE_SPEED_MPS * PIXEL_PER_METER)

# Pikachu Jump Action Speed
JUMP_TIME_PER_ACTION = 0.25
JUMP_ACTION_PER_TIME = 1.0 / JUMP_TIME_PER_ACTION
JUMP_FRAMES_PER_ACTION = 3

# Pikachu JUMP Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
JUMP_SPEED_KMPH = 10.0  # Km/ Hour
JUMP_SPEED_MPH = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
JUMP_SPEED_MPS = (JUMP_SPEED_MPH / 60.0)
JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

PressRight = False


def enter_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RETURN


def right_stay(e):
    global PressRight
    if e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT:
        PressRight = True
    if e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT:
        PressRight = True
    return PressRight


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


class Idle:
    @staticmethod
    def enter(pikachu, e):
        pikachu.frame = 0
        pikachu.action = 6
        pikachu.dir = 0
        pikachu.speed = 0

    @staticmethod
    def exit(pikachu, e):
        pass

    @staticmethod
    def do(pikachu):
        pikachu.frame = (pikachu.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

    @staticmethod
    def draw(pikachu):
        pikachu.image.clip_draw(int(pikachu.frame) * 65, pikachu.action * 66, 65, 66, pikachu.x, pikachu.y, 104, 105)


class RunRight:
    @staticmethod
    def enter(pikachu, e):
        pikachu.dir = 1
        pikachu.speed = RUN_SPEED_PPS
        pikachu.action = 6
        pikachu.frame = 0

    @staticmethod
    def exit(pikachu, e):
        pass

    @staticmethod
    def do(pikachu):
        pikachu.frame = (pikachu.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

    @staticmethod
    def draw(pikachu):
        pikachu.image.clip_draw(int(pikachu.frame) * 65, pikachu.action * 66, 65, 66, pikachu.x, pikachu.y, 104, 105)


class RunLeft:
    @staticmethod
    def enter(pikachu, e):
        pikachu.dir = -1
        pikachu.speed = RUN_SPEED_PPS
        pikachu.action = 6
        pikachu.frame = 0

    @staticmethod
    def exit(pikachu, e):
        pass

    @staticmethod
    def do(pikachu):
        pikachu.frame = (pikachu.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

    @staticmethod
    def draw(pikachu):
        pikachu.image.clip_draw(int(pikachu.frame) * 65, pikachu.action * 66, 65, 66, pikachu.x, pikachu.y, 104, 105)


class Slide:

    @staticmethod
    def enter(pikachu, e):
        pikachu.frame = 0
        pikachu.action = 3
        pikachu.velocity_y = 5

    @staticmethod
    def exit(pikachu, e):
        pikachu.velocity_y = 11

    @staticmethod
    def do(pikachu):
        pikachu.frame = (
                                    pikachu.frame + SLIDE_FRAMES_PER_ACTION * SLIDE_ACTION_PER_TIME * game_framework.frame_time) % 3
        pikachu.velocity_y = pikachu.velocity_y + pikachu.gravity * SLIDE_SPEED_PPS * game_framework.frame_time
        pikachu.y = pikachu.y + pikachu.velocity_y * SLIDE_SPEED_PPS * game_framework.frame_time

        if pikachu.y <= 110:
            pikachu.state_machine.handle_event(('ON_LAND', 0))

    @staticmethod
    def draw(pikachu):
        pikachu.image.clip_draw(int(pikachu.frame) * 64, pikachu.action * 70, 64, 62, pikachu.x, pikachu.y, 104,
                                105)


class Jump:

    @staticmethod
    def enter(pikachu, e):
        pikachu.frame = 0
        pikachu.wait_time = get_time()
        pikachu.action = 5

    @staticmethod
    def exit(pikachu, e):
        pikachu.velocity_y = 11

    @staticmethod
    def do(pikachu):
        pikachu.frame = (pikachu.frame + JUMP_FRAMES_PER_ACTION * JUMP_ACTION_PER_TIME * game_framework.frame_time) % 3
        pikachu.velocity_y = pikachu.velocity_y + pikachu.gravity * JUMP_SPEED_PPS * game_framework.frame_time
        pikachu.y = pikachu.y + pikachu.velocity_y * JUMP_SPEED_PPS * game_framework.frame_time

        if pikachu.y <= 110:
            pikachu.state_machine.handle_event(('ON_LAND', 0))

    @staticmethod
    def draw(pikachu):
        pikachu.image.clip_draw(int(pikachu.frame) * 65, pikachu.action * 66, 65, 66, pikachu.x, pikachu.y, 104, 105)


class StateMachine:
    def __init__(self, pikachu):
        self.pikachu = pikachu
        self.cur_state = Idle
        self.transitions = {
            Slide: {on_land: Idle},
            Idle: {space_down: Slide, right_down: RunRight, left_down: RunLeft, upkey_down: Jump, right_stay: RunRight},
            RunRight: {space_down: Slide, right_up: Idle, left_down: Idle, upkey_down: Jump},
            RunLeft: {space_down: Slide, left_up: Idle, right_down: Idle, upkey_down: Jump},
            Jump: {on_land: Idle}
        }

    def start(self):
        self.cur_state.enter(self.pikachu, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.pikachu)
        self.pikachu.x += self.pikachu.dir * self.pikachu.speed * game_framework.frame_time
        if self.pikachu.x > 350:
            self.pikachu.x = 350
        elif self.pikachu.x < 54:
            self.pikachu.x = 54

    def draw(self):
        self.cur_state.draw(self.pikachu)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.pikachu, e)
                self.cur_state = next_state
                self.cur_state.enter(self.pikachu, e)
                return True

        return False


class Pikachu:
    image = None

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

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def update(self):
        self.state_machine.handle_event(('None', ()))
        self.state_machine.update()

    def draw(self):
        self.state_machine.draw()

    def get_bb(self):
        pass

    def handle_collision(self, group, other):
        pass
