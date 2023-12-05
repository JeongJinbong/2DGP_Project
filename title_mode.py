import pico2d
from pico2d import load_image, load_music, clear_canvas, update_canvas, get_events, load_wav
from sdl2 import SDL_QUIT, SDLK_ESCAPE, SDL_KEYDOWN, SDLK_SPACE, SDLK_UP, SDLK_DOWN

import game_framework
import play_mode
import twoplayer_mode


def init():
    global image
    global image2
    global sound
    global mode_select
    global select_sound

    sound = load_wav('Resource/Sound/WAVE140.wav')
    image = load_image('Resource/Image/title.png')
    image2 = load_image('Resource/Image/title2.png')
    select_sound = load_wav('Resource/Sound/WAVE143.wav')

    mode_select = True


def finish():
    global image
    global image2
    del image
    del image2


def draw():
    global mode_select
    clear_canvas()
    if mode_select == True:
        image.draw(400, 300)
    elif mode_select == False:
        image2.draw(400, 300)
    update_canvas()


def handle_events():
    global mode_select
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            sound.play()
            if mode_select == True:
                game_framework.change_mode(play_mode)
            elif mode_select == False:
                game_framework.change_mode(twoplayer_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            select_sound.play()
            mode_select = 1 - mode_select
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            select_sound.play()
            mode_select = 1 - mode_select


def update():
    pass
