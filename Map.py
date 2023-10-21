from pico2d import load_image

class Sky:
    def __init__(self, x= 400, y= 30):
        self.image = load_image('Resource/Image/Bitmap106.bmp')
        self.x, self.y = x, y

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass