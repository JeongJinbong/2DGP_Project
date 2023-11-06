from pico2d import load_image


class Pikachu:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame =0
        self.image = load_image('Resource/Image/sprite_sheet.png')

    def update(self):
        self.frame =(self.frame+1)%5
        self.x += 5

    def draw(self):
        self.image.clip_draw(2+ self.frame*66,885-1-332,66,66,self.x,self.y,132,132)