from pico2d import load_image
import game_world

class Ball:
    image = None

    def __init__(self,x= 400, y= 300):
        if Ball.image == None:
            Ball.image = load_image('Resource/Image/sprite_sheet.png')
        self.x, self.y = x, y
        self.frame = 0

    def draw(self):
        self.image.clip_draw(88+self.frame*42,885-1-198,40,45,self.x, self.y, 80, 90)


    def update(self):
        self.frame = (self.frame + 1) % 5
