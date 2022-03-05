"""
Name: Ashley Eidenberger
hw7.py

Problem: Create a series of programs that manipulate files, and are able to read files and write to files

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    words = infile.readlines()
    line_list = []

    for i in words:
        line = i
        line_words = line.split()
        line_list = line_list + line_words
    line_list_len = len(line_list)
    for i in range(line_list_len):
        word = line_list[i]
        number = str(i + 1)
        number_word = number + " " + word
        print(number_word, file=outfile)


def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")

    employees = infile.readlines()
    for i in employees:
        employee = i
        employee = employee.split()
        name = employee[0] + " " + employee[1]
        hourly_wage = float(employee[2]) * float(employee[3])
        bonus = float(employee[3]) * 1.65
        tot_pay = hourly_wage + bonus
        print("{0} {1:.2f}".format(name, tot_pay), file=outfile)
    infile.close()
    outfile.close()


def calc_check_sum(isbn):
    isbn_new = isbn.replace("-", "")
    isbn_len = len(isbn_new)
    isbn_sum = 0
    for i in range(isbn_len, 0, -1):
        val = int(isbn_new[10 - i]) * i
        isbn_sum = isbn_sum + val
    return isbn_sum


def send_message(file_name, friend_name):
    infile = open(file_name, "r")
    name_file = friend_name + ".txt"
    outfile = open(name_file, "w")
    infile_content = infile.readlines()
    for line in infile_content:
        line_content = line
        line_content = line_content.strip("\n")
        print(line_content, file=outfile)
    infile.close()
    outfile.close()


def send_safe_message(file_name, friend_name, key):
    infile = open(file_name, "r")
    name_file = friend_name + ".txt"
    key_1 = key

    outfile = open(name_file, "w")
    infile_content = infile.readlines()
    for line in infile_content:
        line_content = line
        line_content = line_content.strip("\n")
        line_content = encode(line_content, key_1)
        print(line_content, file=outfile)
    infile.close()
    outfile.close()


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    infile = open(file_name, "r")
    name_file = friend_name + ".txt"
    outfile = open(name_file, "w")
    infile_content = infile.readlines()
    key = open(pad_file_name, "r")
    key_content = key.readline
    for line in infile_content:
        line_content = line
        line_content = line_content.strip("\n")
        encode_better(line_content, key_content)
        print(line_content, file=outfile)
    infile.close()
    key.close()
    outfile.close()


if __name__ == '__main__':
    send_safe_message("pad.txt", "Zoey", 4)
