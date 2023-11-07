from pico2d import load_image


class Idle:
    @staticmethod
    def enter():
        print('Idle Enter')

    @staticmethod
    def exit():
        print('Idle Exit')

    @staticmethod
    def do():
        print('Idle Do')

    @staticmethod
    def draw():
        pass


class StateMachine:
    def __init__(self):
        self.cur_state = Idle

    def start(self):
        self.cur_state.enter()

    def update(self):
        self.cur_state.do()

    def draw(self):
        self.cur_state.draw()

class Pikachu:
    image = None

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        if Pikachu.image == None:
            Pikachu.image = load_image('Resource/Image/sprite_sheet.png')
        self.state_machine = StateMachine()
        self.state_machine.start()

    def update(self):
        self.state_machine.update()

    def draw(self):
        self.state_machine.draw()

    def handle_event(self, event):
        pass


