from pico2d import *
from Map import Map
import game_world
from Pikachu import Pikachu
from ball import Ball

def handle_events():
    global Running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            Running = False
        else:
            Pikachu.handle_event(event)


def reset_world():
    global Running
    global BackGround

    Running = True

    BackGround = Map()

    game_world.add_object(BackGround, 0)

    ball = Ball(400, 300)

    game_world.add_object(ball, 1)

    pikachu = Pikachu()

    game_world.add_object(pikachu, 1)


def update_world():
    game_world.update()


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas()
reset_world()
# game loop

while Running:
    handle_events()
    update_world()
    render_world()
    delay(0.1)
# finalization code
close_canvas()
