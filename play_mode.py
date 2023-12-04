from pico2d import *

import game_framework
import title_mode
from map import Map
import game_world
from pikachu import Pikachu
from ball import Ball
from net import Net
from leftnet import Leftnet
from rightnet import Rightnet
from score import Score
from enemy import Enemy

PAUSE_DURATION = 0.5
slow_motion_time = None
is_paused = False


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
    global pikachu
    global ball
    global score
    global enemy

    BackGround = Map()
    game_world.add_object(BackGround, 0)

    ball = Ball(50, 500)
    game_world.add_object(ball, 2)

    pikachu = Pikachu()
    game_world.add_object(pikachu, 1)

    net = Net()
    game_world.add_object(net, 0)

    leftnet = Leftnet()
    game_world.add_object(leftnet, 0)

    rightnet = Rightnet()
    game_world.add_object(rightnet, 0)

    score = Score()
    game_world.add_object(score, 0)

    enemy = Enemy()
    game_world.add_object(enemy,1)

    game_world.add_collision_pair('pikachu:ball', pikachu, ball)
    game_world.add_collision_pair('ball:net', ball, net)
    game_world.add_collision_pair('ball:leftnet', ball, leftnet)
    game_world.add_collision_pair('ball:rightnet', ball, rightnet)
    game_world.add_collision_pair('enemy:ball', enemy, ball)


def finish():
    game_world.clear()


def update():
    global slow_motion_time, is_paused

    game_world.update()
    game_world.handle_collisions()

    if ball.y <= 60 + ball.radius and not is_paused:
        # Apply pause or slow-motion effect
        is_paused = True
        slow_motion_time = get_time()
        Ball.score_ball_sound.play()

    # If there is an active slow-motion effect, check the elapsed time
    if is_paused and get_time() - slow_motion_time >= PAUSE_DURATION:
        is_paused = False  # Reset the pause state

        if ball.x <= 400:
            score.player2_score += 1
            ball.serve_p1()
            pikachu.init_position()
            enemy.init_position()

        elif ball.x > 400:
            score.player1_score += 1
            ball.serve_p2()
            pikachu.init_position()
            enemy.init_position()

    if score.player1_score >= 10 or score.player2_score >= 10:
        game_framework.change_mode(title_mode)
def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass


