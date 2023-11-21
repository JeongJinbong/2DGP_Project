from pico2d import get_time, load_image, load_font, clamp, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT
from sdl2 import SDLK_RETURN

import game_world
import game_framework


def enter_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RETURN


def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def time_out(e):
    return e[0] == 'TIME_OUT'


class Idle:
    @staticmethod
    def enter(pikachu, e):
        pikachu.frame = 0
        pikachu.action = 6
        pikachu.dir = 0

    @staticmethod
    def exit(pikachu, e):
        pass

    @staticmethod
    def do(pikachu):
        pikachu.frame = (pikachu.frame + 1) % 5

    @staticmethod
    def draw(pikachu):
        pikachu.image.clip_draw(pikachu.frame * 65, pikachu.action * 66, 65, 66, pikachu.x, pikachu.y, 104, 105)


class Slide:

    @staticmethod
    def enter(pikachu, e):
        pikachu.frame = 0
        pikachu.wait_time = get_time()
        pikachu.action = 3

    @staticmethod
    def exit(pikachu, e):
        pass

    @staticmethod
    def do(pikachu):
        pikachu.frame = (pikachu.frame + 1) % 3
        if get_time() - pikachu.wait_time > 0.3:
            pikachu.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def draw(pikachu):
        pikachu.image.clip_draw(pikachu.frame * 64, pikachu.action * 66 + 9, 64, 65, pikachu.x, pikachu.y, 104, 105)


class Run:
    @staticmethod
    def enter(pikachu, e):
        if right_down(e) or left_up(e):  # 오른쪽으로 RUN
            pikachu.dir, pikachu.action = 1, 6
        elif left_down(e) or right_up(e):  # 왼쪽으로 RUN
            pikachu.dir, pikachu.action = -1, 6

    @staticmethod
    def exit(pikachu, e):
        pass

    @staticmethod
    def do(pikachu):
        pikachu.frame = (pikachu.frame + 1) % 5
        pikachu.x += pikachu.dir * 5
        pass

    @staticmethod
    def draw(pikachu):
        pikachu.image.clip_draw(pikachu.frame * 65, pikachu.action * 66, 65, 66, pikachu.x, pikachu.y, 104, 105)


class StateMachine:
    def __init__(self, pikachu):
        self.pikachu = pikachu
        self.cur_state = Idle
        self.transitions = {
            Slide: {time_out: Idle},
            Idle: {space_down: Slide, right_down: Run, left_down: Run, left_up: Run, right_up: Run},
            Run: {space_down: Slide, right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle}
        }

    def start(self):
        self.cur_state.enter(self.pikachu, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.pikachu)

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
        self.image = load_image('Resource/Image/pikachu.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def update(self):
        self.state_machine.update()

    def draw(self):
        self.state_machine.draw()
