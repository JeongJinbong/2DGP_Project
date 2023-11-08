from pico2d import load_image

def enter_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE

def time_out(e):
    return e[0] == 'TIME_OUT'


class Idle:
    @staticmethod
    def enter(pikachu):
        pikachu.frame = 5

    @staticmethod
    def exit(pikachu):
        pass

    @staticmethod
    def do(pikachu):
        pikachu.frame = (pikachu.frame - 1)
        if pikachu.frame < 0:
            pikachu.frame =5

    @staticmethod
    def draw(pikachu):
        pikachu.image.clip_draw(2 + pikachu.frame * 66, 885 - 1 - 332, 66, 66, pikachu.x, pikachu.y, 132, 132)

class Slide:

    @staticmethod
    def enter(pikachu):
        pikachu.frame = 5

    @staticmethod
    def exit(pikachu):
        pass

    @staticmethod
    def do(pikachu):
        pikachu.frame = (pikachu.frame - 1)
        if pikachu.frame < 0:
            pikachu.frame = 5

    @staticmethod
    def draw(pikachu):
        pikachu.image.clip_draw(2 + pikachu.frame * 66, 885 - 1 - 332, 66, 66, pikachu.x, pikachu.y, 132, 132)


class StateMachine:
    def __init__(self, pikachu):
        self.pikachu = pikachu
        self.cur_state = Idle

    def start(self):
        self.cur_state.enter(self.pikachu)

    def update(self):
        self.cur_state.do(self.pikachu)

    def draw(self):
        self.cur_state.draw(self.pikachu)


class Pikachu:
    image = None

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        if Pikachu.image == None:
            Pikachu.image = load_image('Resource/Image/sprite_sheet.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def draw(self):
        self.state_machine.draw()

    def handle_event(self, event):
        pass
