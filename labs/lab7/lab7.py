"""
Name: Ashley Eidenberger
lab7.py

Problem: Create a program that takes values from a file, outputs the values into average grades for each student and
displays a class average, all in an output file.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    infile_value = infile.readlines()
    class_average = 0
    student_weighted = 0
    for i in infile_value:
        student = i
        student_values = student.split(":")
        student_name = student_values[0]
        student_grades = student_values[1]
        student_grades = student_grades.strip("\n")
        student_grades = student_grades.lstrip()
        student_grades = student_grades.split(" ")
        student_grades_len = len(student_grades)
        tot_avg = 0
        weight = 0
        for j in range(0, student_grades_len, 2):
            val_1 = eval(student_grades[j])
            val_2 = eval(student_grades[j+1])
            weight = weight + val_1
            tot_val = val_1 * val_2
            tot_avg = tot_avg + tot_val
        if weight == 100:
            weighted = tot_avg / 100
            grade_w_name = student_name + str(": ") + str(weighted) + str("\n")
            outfile.write(grade_w_name)
            class_average = class_average + weighted
            student_weighted = student_weighted + 1
        elif weight > 100:
            overflow = str("The weights are more than 100")
            grade_w_name = student_name + str(": ") + overflow + str("\n")
            outfile.write(grade_w_name)
        else:
            underflow = str("The weights are less than 100")
            grade_w_name = student_name + str(": ") + underflow + str("\n")
            outfile.write(grade_w_name)
    class_average_final = class_average / student_weighted
    class_average_final = str("Class Average: ") + str(class_average_final)
    outfile.write(class_average_final)

    infile.close()
    outfile.close()


weighted_average("grades.txt", "avg.txt")
