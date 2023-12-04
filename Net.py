from pico2d import draw_rectangle, load_image


class Net:

    def __init__(self):
        self.image = load_image('Resource/Image/ball.png')
        self.x, self.y = 400, 100

    def draw(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 12, self.y +150, self.x + 10, self.y + 160

    def update(self):
        pass

    def handle_collision(self, group, other):
        match group:
            case 'ball:net':
                pass
