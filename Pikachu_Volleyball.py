from pico2d import *
from Map import Map
import game_world

def handle_events():
    global Running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            Running = False


def reset_world():
    global Running
    global BackGround

    Running = True

    BackGround = Map()

    game_world.add_object(BackGround)

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
    delay(0.01)
# finalization code
close_canvas()
