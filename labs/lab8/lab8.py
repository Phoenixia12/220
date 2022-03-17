"""
Name: Ashley Eidenberger
lab8.py

Problem: Create a program that simulates two bumper cars hitting and bouncing off the other

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math
import graphics
from random import randint
import time


def get_random(move_amount):
    move_amount_neg = move_amount * -1
    return randint(move_amount_neg, move_amount)


def did_collide(ball_1, ball_2):
    ball_1_center = ball_1.getCenter()
    ball_2_center = ball_2.getCenter()
    ball_1_radius = ball_1.getRadius()
    ball_2_radius = ball_2.getRadius()
    dist_x = ((ball_1_center.getX() - ball_2_center.getX()) ** 2)
    dist_y = ((ball_1_center.getY() - ball_2_center.getY()) ** 2)
    dist_tot = math.sqrt(dist_x + dist_y)
    radius_sum = ball_1_radius + ball_2_radius
    return dist_tot <= radius_sum


def hit_vertical(ball, window):
    window_height_max = window.getHeight()
    window_height_min = window_height_max - window_height_max
    ball_center_y = ball.getCenter()
    ball_center_y = ball_center_y.getY()
    ball_radius = ball.getRadius()
    ball_tot = ball_center_y + ball_radius
    return ball_tot >= window_height_max or ball_tot <= window_height_min


def hit_horizontal(ball, window):
    window_width_max = window.getWidth()
    window_width_min = window_width_max - window_width_max
    ball_center_x = ball.getCenter()
    ball_center_x = ball_center_x.getX()
    ball_radius = ball.getRadius()
    ball_tot = ball_center_x + ball_radius
    return ball_tot >= window_width_max or ball_tot <= window_width_min


def get_random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    color = graphics.color_rgb(red, blue, green)
    return color


def bumper():
    window = graphics.GraphWin("Joyride", 400, 400)
    bumper_1 = graphics.Circle(graphics.Point(randint(0, 390), randint(0, 390)), 10)
    bumper_1.setFill(get_random_color())
    bumper_1.draw(window)
    bumper_2 = graphics.Circle(graphics.Point(randint(0, 390), randint(0, 390)), 10)
    bumper_2.setFill(get_random_color())
    bumper_2.draw(window)
    bumper_1_move_x, bumper_1_move_y = get_random(50), get_random(50)
    bumper_2_move_x, bumper_2_move_y = get_random(50), get_random(50)

    while not window.checkMouse():
        time.sleep(.1)
        bumper_1.move(bumper_1_move_x, bumper_1_move_y)
        bumper_2.move(bumper_2_move_x, bumper_2_move_y)
        if did_collide(bumper_1, bumper_2):
            bumper_1_move_x, bumper_1_move_y = (bumper_1_move_x * -1), (bumper_1_move_y * -1)
            bumper_2_move_x, bumper_2_move_y = (bumper_2_move_x * -1), (bumper_2_move_y * -1)
        if hit_horizontal(bumper_1, window):
            bumper_1_move_x = (bumper_1_move_x * -1)
        if hit_horizontal(bumper_2, window):
            bumper_2_move_x = (bumper_2_move_x * -1)
        if hit_vertical(bumper_1, window):
            bumper_1_move_y = (bumper_1_move_y * -1)
        if hit_vertical(bumper_2, window):
            bumper_2_move_y = (bumper_2_move_y * -1)
    window.close()


bumper()






















