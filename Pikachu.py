from pico2d import load_image


class Pikachu:
    image = None

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        if Pikachu.image == None:
            Pikachu.image = load_image('Resource/Image/sprite_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 5
        self.x += 5

    def draw(self):
        self.image.clip_draw(2 + self.frame * 66, 885 - 1 - 332, 66, 66, self.x, self.y, 132, 132)

    def handle_event(self, event):
        pass


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