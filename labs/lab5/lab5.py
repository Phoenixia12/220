"""
Name: Ashley Eidenberger
lab5.py

Problem: Create a series of programs that make use of the graphics library and manipulate strings

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

import math
import graphics


def triange():
    win = graphics.GraphWin("Triangle", 500, 500)
    instructions = graphics.Text(graphics.Point(5, 8), "Click three times to create triangle")
    win.setCoords(0, 0, 10, 10)
    instructions.draw(win)
    p1 = win.getMouse()
    point1_x = p1.getX()
    point1_y = p1.getY()
    p2 = win.getMouse()
    point2_x = p2.getX()
    point2_y = p2.getY()
    p3 = win.getMouse()
    point3_x = p3.getX()
    point3_y = p3.getY()

    side_a_x = (point1_x - point2_x) ** 2
    side_a_y = (point1_y - point2_y) ** 2
    side_a = math.sqrt(side_a_x + side_a_y)
    side_b_x = (point2_x - point3_x) ** 2
    side_b_y = (point2_y - point3_y) ** 2
    side_b = math.sqrt(side_b_x + side_b_y)
    side_c_x = (point1_x - point3_x) ** 2
    side_c_y = (point1_y - point3_y) ** 2
    side_c = math.sqrt(side_c_x + side_c_y)

    perimeter = side_a + side_b + side_c
    area_constant = perimeter / 2
    area = math.sqrt(area_constant * (area_constant - side_a) * (area_constant - side_b) * (area_constant * side_c))
    round(perimeter, 2)
    shape = graphics.Polygon(p1, p2, p3)
    shape.draw(win)

    perimeter_text = graphics.Text(graphics.Point(5, 2), "Perimeter:")
    perimeter_result = graphics.Text(graphics.Point(7.3, 2), "")
    perimeter_result.setText(perimeter)

    perimeter_text.draw(win)
    perimeter_result.draw(win)

    area_text = graphics.Text(graphics.Point(5, 1.5), "Area:")
    area_result = graphics.Text(graphics.Point(7.3, 1.5), "")
    area_result.setText(area)
    area_text.draw(win)
    area_result.draw(win)

    win.getMouse()
    win.close()


def color_shape():

    # create window
    win_width = 400
    win_height = 400
    win = graphics.GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = graphics.Text(graphics.Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = graphics.Circle(graphics.Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = graphics.Point(win_width / 2 - 50, win_height / 2 + 40)
    red_x = red_text_pt.getX()
    red_y = red_text_pt.getY()
    red_text = graphics.Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red = graphics.Entry(graphics.Point(red_x + 40, red_y), 5)
    red.draw(win)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_x = green_text_pt.getX()
    green_y = green_text_pt.getY()
    green_text = graphics.Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green = graphics.Entry(graphics.Point(green_x + 40, green_y), 5)
    green.draw(win)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_x = blue_text_pt.getX()
    blue_y = blue_text_pt.getY()
    blue_text = graphics.Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue = graphics.Entry(graphics.Point(blue_x + 40, blue_y), 5)
    blue.draw(win)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    instruct = graphics.Text(graphics.Point(200, 50), "Enter RGB values, then click, this can be done five times")
    instruct.draw(win)
    for i in range(4):
        win.getMouse()
        red_value = eval(red.getText())
        blue_value = eval(blue.getText())
        green_value = eval(green.getText())
        shape.setFill(graphics.color_rgb(red_value, green_value, blue_value))
    # Wait for another click to exit
    close = graphics.Text(graphics.Point(200, 350), "Click again to close")
    close.draw(win)
    win.getMouse()
    win.close()


def process_string():
    user_string = input("Please enter a string: ")
    first_char = user_string[0]
    print(first_char)
    last_char_len = len(user_string) - 1
    last_char = user_string[last_char_len]
    print(last_char)
    positions = user_string[1:6]
    print(positions)
    lastandfirst = first_char + last_char
    print(lastandfirst)
    first_three = user_string[0:3]
    first_three = first_three * 10
    print(first_three)
    length = len(user_string)
    for i in range(length):
        print(user_string[i])
    print(length)


def process_list():
    pt = graphics.Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2:5]
    print(x)
    x = values[2:4]
    x.append(values[0])
    print(x)
    x = [values[2]]
    x.append(values[0])
    float_6 = [float(values[5])]
    x = x + [float_6[0]]
    print(x)
    x = values[0] + values[2] + float_6[0]
    print(x)
    x = len(values)
    print(x)


def another_series():
    valuerange = [6, 12, 18]
    final_sum = 0
    terms = eval(input("How many terms would you like the value to add up to?: "))
    for i in range(terms):
        initial_val = valuerange[i % 3]
        final_sum = final_sum + initial_val
    print(final_sum)


def target():
    win = graphics.GraphWin("Target", 400, 400)
    radius = 200
    colors = ["black", "blue", "red", "yellow"]
    center = graphics.Circle(graphics.Point(200, 200), radius)
    center_coords = center.getCenter()
    center.setFill("white")
    center.draw(win)
    for i in range(4):
        radius = radius - 35
        ring = graphics.Circle(graphics.Point(center_coords.getX(), center_coords.getY()), radius)
        ring.setFill(colors[i])
        ring.draw(win)
    win.getMouse()
    win.close()
