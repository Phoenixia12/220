"""
Ashley Eidenberger
lab10.py
Problem: Create a program that displays a GUI, when a button is clicked on screen,
simulate a door opening and closing
Certificate of Authenticity: I certify that this assignment is entirely my own work
"""

import graphics
from button import Button
from door import Door


def main():
    win = graphics.GraphWin('Window', 400, 400)
    button = Button(graphics.Rectangle(graphics.Point(25, 25), graphics.Point(375, 75)), 'Button')
    door = Door(graphics.Rectangle(graphics.Point(25, 100), graphics.Point(375, 375)), 'closed', False)
    door.draw(win)
    button.draw(win)

    point = win.getMouse()
    while button.is_clicked(point):
        if button.is_clicked(point):
            door.open('white', 'open')
        point = win.getMouse()
        if button.is_clicked(point):
            door.close('red', 'closed')
        point = win.getMouse()

    win.close


main()
