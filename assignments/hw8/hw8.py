"""
Name: Ashley Eidenberger
hw8.py

Problem: Create a series of programs that manipulate lists and make use of logical operators

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math
from graphics import Circle, GraphWin


def add_ten(nums):
    nums_new = []
    for i in nums:
        new_value = [i + 10]
        i = new_value
        nums_new = nums_new + i
    nums[0:] = nums_new


def square_each(nums):
    nums_new = []
    for i in nums:
        new_value = [i ** 2]
        i = new_value
        nums_new = nums_new + i
    nums[0:] = nums_new


def sum_list(nums):
    nums_sum = 0
    for i in nums:
        nums_sum = nums_sum + i
    return nums_sum


def to_numbers(nums):
    nums_new = []
    for i in nums:
        new_value = eval(i)
        i = [new_value]
        nums_new = nums_new + i
    nums[0:] = nums_new


def sum_of_squares(nums):
    sums_list = []
    for i in nums:
        nums_new = 0
        num_val = i
        num_val = num_val.split(",")
        for j in num_val:
            new_value = eval(j)
            new_value = new_value ** 2
            nums_new = nums_new + new_value
        sums_list = sums_list + [nums_new]
    nums[0:] = sums_list
    return nums


def starter(weight, wins):
    if (weight >= 150 and weight < 160) and wins >= 5:
        return True
    elif weight > 199 or wins > 20:
        return True
    else:
        return False


def leap_year(year):
    if (year % 4) == 0 and not (year % 100) == 0:
        return True
    elif (year % 400) == 0:
        return True
    return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center_2 = win.getMouse()
    circumference_point_2 = win.getMouse()
    radius_2 = math.sqrt(
        (center_2.getX() - circumference_point_2.getX()) ** 2 + (center_2.getY() - circumference_point_2.getY()) ** 2)
    circle_2 = Circle(center_2, radius_2)
    circle_2.setFill("light blue")
    circle_2.draw(win)

    win.getMouse()


def did_overlap(circle_one, circle_two):
    circle_one_center = circle_one.getCenter()
    circle_two_center = circle_two.getCenter()
    circle_one_rad = circle_one.getRadius()
    circle_two_rad = circle_two.getRadius()
    dist_x = ((circle_one_center.getX() - circle_two_center.getX()) ** 2)
    dist_y = ((circle_one_center.getY() - circle_two_center.getY()) ** 2)
    dist_tot = math.sqrt(dist_x + dist_y)
    radius_sum = circle_one_rad + circle_two_rad
    return dist_tot <= radius_sum


if __name__ == '__main__':
    pass
