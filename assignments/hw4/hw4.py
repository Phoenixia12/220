"""
Name: Ashley Eidenberger
hw4.py

Problem: Create a series of programs that make use of the graphics libary
and approximate pi

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math
import graphics


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = graphics.GraphWin("Clicks", width, height)

    num_clicks = 5

    inst_pt = graphics.Point(width / 2, height - 10)
    instructions = graphics.Text(inst_pt, "Click to move square")
    instructions.draw(win)

    shape = graphics.Rectangle(graphics.Point(0, 50), graphics.Point(50, 100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    for _ in range(num_clicks):
        click = win.getMouse()
        new_shape = shape.clone()
        new_shape.draw(win)
        center = new_shape.getCenter()  # center of circle
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        new_shape.move(change_x, change_y)

    inst_pt_final = graphics.Point(width / 2, height - 200)
    instructions_final = graphics.Text(inst_pt_final, "Click to close window")
    instructions_final.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    win = graphics.GraphWin("Rectangle", 400, 400)

    point_1 = win.getMouse()
    point_2 = win.getMouse()

    rect = graphics.Rectangle(point_1, point_2)
    rect.setFill("green")
    rect.draw(win)

    rect_center = rect.getCenter()
    rect_x = rect_center.getX()
    rect_y = rect_center.getY()

    rect_area = (rect_x * 2) * (rect_y * 2)
    area_text = graphics.Text(graphics.Point(200, 345), "Area:")
    area_result = graphics.Text(graphics.Point(275, 345), " ")
    area_result.setText(rect_area)

    rect_perimeter = (rect_x * 4) + (rect_y * 4)
    perimeter_text = graphics.Text(graphics.Point(200, 385), "Perimeter:")
    perimeter_result = graphics.Text(graphics.Point(275, 385), " ")
    perimeter_result.setText(rect_perimeter)
    area_text.draw(win)
    area_result.draw(win)
    perimeter_text.draw(win)
    perimeter_result.draw(win)

    win.getMouse()


def circle():
    width = 400
    height = 400
    win = graphics.GraphWin("Circle", height, width)
    center = win.getMouse()
    center.draw(win)
    dist = win.getMouse()
    dist.draw(win)
    radius = math.sqrt(((center.getX() - dist.getX())**2) + (center.getY() - dist.getY())**2)
    circ = graphics.Circle(graphics.Point(center.getX(), center.getY()), radius)
    circ.draw(win)


def pi2():
    terms = int(input("How many terms in the series?: "))
    approx = 0
    for i in range(1, terms + 1):
        denom = 1 + (2 * (i -1))
        sign = ((i % 2) - 0.5) * 2 // 1
        approx = approx + ((4 / denom) * sign)
    acc = math.pi - approx
    print(approx)
    print(acc)


if __name__ == '__main__':
    pass
