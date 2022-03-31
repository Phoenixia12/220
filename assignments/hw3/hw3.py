"""
Name: Ashley Eidenberger
h32.py

Problem: Series of programs which solve math problems via loops

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math

def average():
    grades = int(input("How many grades would you like to enter?: "))
    grade_sum = 0
    for _ in range(grades):
        grade_input = int(input("Enter grade:"))
        grade_sum = grade_sum + grade_input
    grade_avg = grade_sum / grades
    print("The average is: ", grade_avg)




def tip_jar():
    tip_total = 0.0
    for _ in range(5):
        tip = float(input("How much would you like to tip?: "))
        tip_total = tip_total + tip
    print("Total tips is: ", tip_total)




def newton():
    root = int(input("What number do you want to square root?: "))
    approx = root

    approx_range = int(input("How many times should we improve the approximation?: "))
    for _ in range(approx_range):
        approx = (approx + (root / approx)) / 2
    print("The square root is approximately: ", approx)



def sequence():
    term = int(input("How many terms would you like?: "))
    initial_val = 1
    difference = 2
    for i in range(1, term+1):
        i = i / 2
        i = math.ceil(i)
        sequence_val = initial_val + (i - 1) * difference
        print(sequence_val, end='\t')






def pi():
    terms = int(input("How many terms in the series?: "))
    pi_half = 1.0
    for i in range(1, terms + 1):
        side_1 = (2 * i) / (2 * i - 1)
        side_2 = (2 * i) / (2 * i + 1)
        total = side_1 * side_2
        pi_half = pi_half * total
    pi_final = pi_half * 2
    print(pi_final)

pi()

if __name__ == '__main__':
    pass
