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
    word_len = len(secret_word)
    hidden_word = secret_word
    for i in range(word_len):









def won(guessed):
    pass


def play_graphics(secret_word):
    pass


def play_command_line(secret_word):
    pass


if __name__ == '__main__':
    word = make_hidden_secret("american", ["a", "e"])
    print(word)
    # play_command_line(secret_word)
    # play_graphics(secret_word)
