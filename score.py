from pico2d import draw_rectangle, load_image


class Score:

    def __init__(self):
        self.image = load_image('Resource/Image/Score_number.png')
        self.player1x, self.player1y = 100, 500
        self.player2x, self.player2y = 700, 500
        self.player1_score = 0
        self.player2_score = 0

    def draw(self):
        self.image.clip_draw(self.player1_score * 32, 0, 30, 30, self.player1x, self.player1y, 66, 60)
        self.image.clip_draw(self.player2_score * 32, 0, 30, 30, self.player2x, self.player2y, 66, 60)

    def update(self):
        pass
