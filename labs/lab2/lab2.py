"""
Ashley Eidenberger
lab2.py
Problem: Create a program that allows the user to calculate the root-mean-square, the harmonic mean
and the geometric mean.
Certificate of Authenticity: I certify that this assignment is entirely my own work
"""


def dynamic_mean_cal():
    value_amount = int(input("How many values will you enter?: "))
    root_mean = 0
    harmonic_mean = 0
    geometric_mean = 1
    for i in range(value_amount):
        input_value = int(input("Please input a value: "))
        root_mean = root_mean + (input_value ** 2)
        harmonic_mean = harmonic_mean + (1 / input_value)
        geometric_mean = geometric_mean * input_value

    root_mean = (root_mean / value_amount) ** (1/2)
    root_mean = round(root_mean, 3)

    harmonic_mean = value_amount / harmonic_mean
    harmonic_mean = round(harmonic_mean, 3)

    geometric_mean = geometric_mean ** (1/value_amount)
    geometric_mean = round(geometric_mean, 3)

    print("The Root-Mean-Square is: ", root_mean)
    print("The Harmonic Mean is: ", harmonic_mean)
    print("The Geometric Mean is: ", geometric_mean)


dynamic_mean_cal()
