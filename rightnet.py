from pico2d import draw_rectangle, load_image


class Rightnet:

    def __init__(self):
        self.image = load_image('Resource/Image/ball.png')
        self.x, self.y = 400, 100

    def draw(self):
        pass

    def get_bb(self):
        return self.x , self.y -50, self.x +10, self.y + 140

    def update(self):
        pass

    def handle_collision(self, group, other):
        match group:
            case 'ball:net':
                pass

