from pico2d import *

import game_framework
import title_mode
from map import Map
import game_world
from pikachu import Pikachu
from ball import Ball


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        else:
            pikachu.handle_event(event)


def init():
    global BackGround
    global pikachu
    global ball

    BackGround = Map()
    game_world.add_object(BackGround, 0)

    ball = Ball(400, 300)
    game_world.add_object(ball, 1)

    pikachu = Pikachu()
    game_world.add_object(pikachu, 1)


def finish():
    game_world.clear()


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

