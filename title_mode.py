import pico2d
from pico2d import load_image, load_music, clear_canvas, update_canvas, get_events, load_wav
from sdl2 import SDL_QUIT, SDLK_ESCAPE, SDL_KEYDOWN, SDLK_SPACE

import game_framework
import play_mode


def init():
    global image
    global sound
    sound = load_wav('Resource/Sound/WAVE140.wav')
    image = load_image('Resource/Image/title.png')


def finish():
    global image
    del image


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            sound.play()
            game_framework.change_mode(play_mode)


def update():
    pass