from pico2d import *

from map import Map
import game_world
from pikachu import Pikachu
from ball import Ball


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            pikachu.handle_event(event)


def init():
    global running
    global BackGround
    global pikachu
    global ball

    running = True

    BackGround = Map()
    game_world.add_object(BackGround, 0)

    ball = Ball(400, 300)
    game_world.add_object(ball, 1)

    pikachu = Pikachu()
    game_world.add_object(pikachu, 1)


def finish():
    pass


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas()
init()
# game loop

while running:
    handle_events()
    update()
    draw()
    delay(0.1)
finish()
# finalization code
close_canvas()
