from pico2d import load_image

class Map:
    image = None
    def __init__(self, x= 400, y= 300):
        if self.image == None:
            self.image = load_image('Resource/Image/BackGround.png')
        self.x, self.y = x, y

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

