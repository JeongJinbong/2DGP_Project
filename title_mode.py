from pico2d import get_time, load_image, clear_canvas, update_canvas, get_events


def init():
    global image
    image = load_image('Resource/Image/title.png')



def finish():
    global image
    del image


def update():
    global running
    global logo_start_time
    if get_time() - logo_start_time >= 2.0:
        logo_start_time = get_time()
        running = False


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework
