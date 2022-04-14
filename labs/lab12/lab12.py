"""
Name: Ashley Eidenberger
lab12.py

Problem: Create a series of programs that make use of while loops

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from random import randint


def find_and_remove_first(val_list, value):
    i = 0
    while val_list[i] != value:
        i = i + 1
    val_list.pop(i)
    val_list.insert(i, 'Zoey')
    print(val_list)


def good_input():
    user_input = eval(input('Please input a number between one and ten:'))
    while user_input > 10 or user_input <= 0:
        if user_input > 10:
            user_input = eval(input('Value is too high, please input a new value'))
        elif user_input <= 0:
            user_input = eval(input('Value is too low, please input a new value'))
    return user_input


def num_digits():
    user_input = eval(input('Please provide a value'))
    count = 0
    if user_input <= 0:
        return None
    else:
        while user_input > 0:
            user_input = user_input // 10
            count += 1
        return count


def hi_lo_game():
    value = randint(1, 100)
    print(value)
    chances = 7
    count = 0
    while chances >= 0:
        user_value = eval(input('Guess a number between one and one hundred:'))
        if user_value == value:
            print('Congrats you guessed the number and it only took you {} guesses!'.format(count))
            chances = chances - 8

        elif chances == 0:
            print('You lose, the number was {}!'.format(value))
            chances -= 1
        else:
            chances -= 1
            count += 1
            if user_value > value:
                print('Your guess was too high, try again!')
            else:
                print('Your guess was to low, try again!')
