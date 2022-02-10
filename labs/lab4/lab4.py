"""
Name: Ashley Eidenberger
lab4.py

Problem: Create a program that displays a heart and wishes the user a happy Valentine's day, afterwards it shoots
an arrow through the heart and prompts the user to click on the screen to close the program.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import *
import time


def greeting_card():
    win = GraphWin("Happy Valentine's Day", 400, 400)
    heart_1 = Circle(Point(175, 150), 35)
    heart_2 = Circle(Point(225, 150), 35)
    heart_3 = Polygon(Point(140, 150), Point(260, 150), Point(200, 240))
    heart_1.setFill("pink")
    heart_1.setOutline("pink")
    heart_2.setFill("pink")
    heart_2.setOutline("pink")
    heart_3.setFill("pink")
    heart_3.setOutline("pink")
    heart_1.draw(win)
    heart_2.draw(win)
    heart_3.draw(win)

    message = Text(Point(200, 275), "Happy Valentines Day!")
    message.setTextColor("red")
    message.draw(win)

    arrow_head = Point(401, 150)
    arrow_tail = Point(551, 150)
    arrow_end_head = Point(550, 150)
    arrow_end_tail = Point(551, 150)
    arrow = Line(arrow_head, arrow_tail)
    arrow_end = Line(arrow_end_head, arrow_end_tail)
    arrow.setArrow("first")
    arrow_end.setArrow("first")
    arrow.draw(win)
    arrow_end.draw(win)
    arrow.setOutline("gold")
    arrow_end.setOutline("gold")
    arrow.setWidth(5)
    arrow_end.setWidth(5)
    for i in range(125):
        time.sleep(.1)
        arrow.move(-5, 0)
        arrow_end.move(-5, 0)
    goodbye_message = Text(Point(200, 100), "Click to close <3")
    goodbye_message.setTextColor("red")
    goodbye_message.draw(win)
    win.getMouse()
    win.close()


greeting_card()
