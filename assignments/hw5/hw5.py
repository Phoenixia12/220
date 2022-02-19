"""
Name: Ashley Eidenberger
hw5.py

Problem: Create a series of programs that manipulate strings

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""


def name_reverse():
    namestr = input("Enter a first and last name: ")
    namelist = namestr.split()
    print(namelist[1] + ", " + namelist[0])


def company_name():
    domain = input("Enter a domain name: ")
    domainlis = domain.split(".")
    company = domainlis[1]
    print(company)


def initials():
    students = int(input("How many students are in the class?: "))
    for _ in range(1, students + 1):
        student = input("What is the student's name?: ")
        studentlis = student.split()
        fname = studentlis[0]
        lname = studentlis[1]
        initial = fname[0] + lname[0]
        print(initial)


def names():
    namelist = input("Enter a list of names, seperated by commas: ")
    initial_list = namelist.split(",")
    #print(initial_list)
    number_of_names = len(initial_list)
    #print(number_of_names)
    final_initials_list = []
    for i in range(number_of_names):
        name = str(initial_list[i])

        name = name.split()
        #print(name)

        fname = name[0]
        #print(fname)
        lname = name[1]
        #print(lname)
        initial = [fname[0] + lname[0]]
        #print(initial)
        final_initials_list = final_initials_list + initial
    print(final_initials_list)


def thirds():
    sentences = eval(input("How many sentences would you like to enter?: "))
    third = []
    third_total = []
    for i in range(sentences):
        sentence = input("Input a sentence: ")
        sentence_length = len(sentence)
        #print(sentence_length)
        for j in range(sentence_length // 3):
            #print(j)
            character = [sentence[j * 3]]
            third = third + character



        third_total = third_total.append(third)
        third = []
    print(third_total)


thirds()



def word_average():
    sentence = input("Enter a sentence: ")
    words = sentence.split(" ")
    sentence_length = len(words)
    total_letters = 0
    for i in range(sentence_length):
        word = [words[i]]
        letter = str(word) + ""
        letters = len(letter) - 4
        total_letters = total_letters + letters
    average = total_letters / sentence_length
    print(average)


def pig_latin():
    sentence = input("Enter a sentence: ")
    latin = ""
    words = sentence.split(" ")
    words_length = len(words)
    print(words)
    print(words_length)
    for i in range(words_length):
        word = str(words[i])
        print(word)
        latin = latin + (word[1:] + word[0] + "ay") + " "
    latin = latin.lower()
    latin = latin.rstrip()
    print(latin)



if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
