from pico2d import *
from Map import Sky
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
    global map

    Running = True

    sky = Sky()

    game_world.add_object(sky)

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
