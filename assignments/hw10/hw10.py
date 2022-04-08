"""
Name: Ashley Eidenberger
hw10.py

Problem: Create a series of programs and classes without using for loops

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math
from graphics import GraphWin, Point
import sphere
from face import Face


def fibonacci(count):
    val_1 = 0
    val_2 = 1
    acc = 0
    int_val = count
    if int_val >= 1:
        while acc < count:
            if acc < 1:
                new_val = acc
            else:
                new_val = val_1 + val_2
                val_1 = val_2
                val_2 = new_val
            acc = acc + 1
        return new_val
    else:
        return None


def double_investment(principal, rate):
    years = 0
    invest_total = principal
    while invest_total < (principal * 2):
        invest_total = invest_total * (1.0 + rate)
        years = years + 1
    return years


def syracuse(value):
    val_list = [value]
    while value != 1:
        if value % 2 == 0:
            value = int(value / 2)
            val_list.append(value)
        else:
            value = (3 * value) + 1
            val_list.append(value)
    return val_list


def goldbach(num):
    if num % 2 == 0:
        prime_nums = [0, 0]



