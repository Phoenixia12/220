"""
Name: Ashley Eidenberger
hw9.py

Problem: Create a program that allows the user to play hangman

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""


from random import randint

def get_words(file_name):
    input_file = open(file_name, "r")
    initial_list = input_file.readlines()
    word_list = []
    for word in initial_list:
        word_mod = word.lower()
        word_mod = [word_mod.rstrip("\n")]
        word_list = word_list + word_mod
    return word_list

def get_random_word(words):
    tot_words = len(words)
    word_position = randint(0, tot_words)
    word = words[word_position]
    return word


def letter_in_secret_word(letter, secret_word):
    letter_val = secret_word.count(letter)
    return letter_val > 0


def already_guessed(letter, guesses):
    letter_in_guess = guesses.count(letter)
    return letter_in_guess > 0


def make_hidden_secret(secret_word, guesses):
    hidden_word = ""
    for letter in secret_word:
        if guesses.count(letter) > 0:
            hidden_word = hidden_word + letter + " "
        else:
            hidden_word = hidden_word + "_ "
    hidden_word = hidden_word.rstrip()
    return hidden_word


def won(guessed):
    if guessed.count("_") > 0:
        return True
    else:
        return False


def play_graphics(secret_word):
    pass


def play_command_line(secret_word):
    guesses = []
    tot_tries = 6
    hidden_word = make_hidden_secret(secret_word, guesses)
    while won(hidden_word):
        if tot_tries > 0:
            guess = input("Guess a letter:")
            if letter_in_secret_word(guess, secret_word):
                guesses = guesses + [guess]
                hidden_word = make_hidden_secret(secret_word, guesses)
            elif already_guessed(guess, guesses):
                guess = input("Guess a letter:")
            else:
                guesses = guesses + [guess]
                tot_tries = tot_tries - 1
            print("already guessed:", guesses)
            print("guesses remaining:", tot_tries)
            print(hidden_word)
    if not won(secret_word):
        print('winner')
        print('word is:', secret_word)
    else:
        print('you have run out of tries')
        print('the word was:', secret_word)

if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
