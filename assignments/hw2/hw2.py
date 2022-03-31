"""
Name: Ashley Eidenberger
hw2.py
Problem: Create a series of functions that solve various math problems.
Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
import math


def sum_of_threes():
    """
    loop, multiply each value by 3
    convert value given by user using integer division
    """
    upper_bound = int(input("Please specify an upper bound: "))
    upper_value = upper_bound // 3
    three_total = 0
    for i in range(1, upper_value + 1):
        three_total = (i * 3) + three_total
    print("The sum of threes is: ", three_total)


def multiplication_table():
    for i in range(1, 11):
        for h in range(1, 11):
            print(i * h, end="\t")


def triangle_area():
    length_a = int(input("Enter a side length: "))
    length_b = int(input("Enter a side length: "))
    length_c = int(input("Enter a side length: "))
    length_total = (length_a + length_b + length_c) / 2
    side_a = length_total - length_a
    side_b = length_total - length_b
    side_c = length_total - length_c

    area = math.sqrt(length_total * side_a * side_b * side_c)
    print("The area is: ", area)


def sum_squares():
    low_bound = int(input("Enter the lower range: "))
    high_bound = int(input("Enter the upper range: "))
    square_total = 0
    for i in range(low_bound, high_bound + 1):
        square_total = square_total + (i * i)
    print("Your sum of squares is: ", square_total)


def power():
    base_value = int(input("Enter a base: "))
    exponent_value = int(input("Enter an exponent: "))
    total_value = 1
    for _ in range(exponent_value):
        total_value = total_value * base_value
    print(base_value, "^", exponent_value, "=", total_value)


if __name__ == '__main__':
    multiplication_table()
