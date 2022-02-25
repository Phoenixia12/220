"""
Name: Ashley Eidenberger
hw6.py

Problem: Create a series of programs which return values or encode a message

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import math


def cash_converter():
    cash = float(input("Enter an integer: "))
    amount = str(cash) + '0'
    amount = amount[:5]
    print("That is ${0:>4}".format(amount))


def encode():
    message = input("Enter a message:")
    key = eval(input("Enter a key"))
    message_output = ''
    message_char_length = len(message)
    for i in range(message_char_length):
        num = message[i]
        print(num)
        num = ord(message[i]) + key
        print(num)
        character = chr(num)
        print(character)
        message_output = message_output + character
    print(message_output)


def sphere_area(radius):
    area_value = 4 * math.pi * math.pow(radius, 2)
    return area_value


def sphere_volume(radius):
    vol_value = (4 / 3) * math.pi * math.pow(radius, 3)
    return vol_value


def sum_n(number):
    total_sum = 0
    for i in range(1, number + 1):
        total_sum = total_sum + i
    return total_sum


def sum_n_cubes(number):
    total_sum = 0
    for i in range(1, number + 1):
        total_sum = total_sum + math.pow(i, 3)
    return total_sum


def encode_better():
    message = input("Enter a message: ")
    key = input("Enter a key: ")
    key_length = len(key)
    message_length = len(message)
    coded_message = ""

    for i in range(message_length):
        character_num = ord(message[i])
        key_num = ord(key[i % key_length])
        character_num = character_num - 65
        print(character_num)
        key_num = key_num - 65
        print(key_num)
        shift_val = (character_num + key_num) % 58
        print(shift_val)
        coded_val = shift_val + 65
        print(coded_val)
        coded_val = chr(coded_val)
        print(coded_val)
        coded_message = coded_message + coded_val

    print(coded_message)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
