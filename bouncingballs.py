import pgzrun
# https://stackoverflow.com/questions/74817115/resizing-a-sprite-with-pygame-zero
from pgzhelper import *

import random

# window size
WIDTH = 800
HEIGHT = 600
GRAY = (100,100,120)

BALL_FIELD = 0
X_FIELD = 1
Y_FIELD = 2


balls = []

# create ball on click
def on_mouse_down(pos, button):
    if button == mouse.LEFT:
        x, y = pos
        new_ball = Actor('ball', pos=(x, y))        
        new_ball.scale = 0.05 #pgzhelper

        y_velo = random.randint(-8, 8)
        x_velo = random.randint(-8, 8)
        balls.append([new_ball, x_velo, y_velo])

# update position of balls
def update():
    for i, (ball, x_velo, y_velo) in enumerate(balls):
        ball.x += x_velo
        ball.y += y_velo

        # update direction when colliding with wall
        if ball.left <= 0 or ball.right >= WIDTH:
            balls[i][X_FIELD] *= -1
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            balls[i][Y_FIELD] *= -1

# Render screen and items
def draw():
    screen.clear()
    screen.fill(GRAY)
    for ball in balls:
        ball[BALL_FIELD].draw()

# Run game
pgzrun.go()
