from pico2d import *


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

    Running = True


def update_world():
    pass


def render_world():
    clear_canvas()
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
