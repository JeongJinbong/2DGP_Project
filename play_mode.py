from pico2d import *

import game_framework
import title_mode
from map import Map
import game_world
from pikachu import Pikachu
from ball import Ball
from net import Net
from score import Score


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
    global net
    global score

    BackGround = Map()
    game_world.add_object(BackGround, 0)

    ball = Ball(50, 500)
    game_world.add_object(ball, 2)

    pikachu = Pikachu()
    game_world.add_object(pikachu, 1)

    net = Net()
    game_world.add_object(net, 0)

    score = Score()
    game_world.add_object(score, 0)

    game_world.add_collision_pair('pikachu:ball', pikachu, ball)
    game_world.add_collision_pair('ball:net', ball, net)


def finish():
    game_world.clear()


def update():
    game_world.update()
    game_world.handle_collisions()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

