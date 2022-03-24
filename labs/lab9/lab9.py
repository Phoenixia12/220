"""
Ashley Eidenberger
lab9.py
"""


def build_board():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    pos = board[position - 1]
    if str(pos).isnumeric():
        return True
    else:
        return False


def fill_spot(board, position, character):
    shape = character.lower()
    shape = shape.strip()
    board[position - 1] = shape


def winning_game(board):
    if board[0] == board[1] == board[2]:
        return True
    elif board[0] == board[3] == board[6]:
        return True
    elif board[0] == board[4] == board[8]:
        return True
    elif board[1] == board[4] == board[7]:
        return True
    elif board[2] == board[4] == board[6]:
        return True
    elif board[2] == board[5] == board[8]:
        return True
    elif board[3] == board[4] == board[5]:
        return True
    elif board[6] == board[7] == board[8]:
        return True
    else:
        return False


def game_over(board):
    if winning_game(board):
        return True
    for i in range(9):
        pos = board[i]
        if str(pos).isnumeric():
            return False
    return True


def get_winner(board):
    x = board.count('x')
    o = board.count('o')
    if not game_over(board):
        return None
    if x > o:
        return "X"
    elif x == o:
        return "O"



def play(board):
    print('Players will take turns placing their shape (x or o) on a square by entering the '
          'number where they want to play. x’s will always start, followed by o’s. If a player enters'
          ' the number of an unavailable square (the square has already been played), then nothing happens '
          'and the same player is prompted again to play (see sample games below). '
          'The game ends when one player gets three or their shapes in a row (horizontally, '
          'vertically, or diagonally) or every square is played. A tie occurs when every square i'
          's played without either player winning')
    want_to_play = "y"
    while want_to_play == "y":
        while not game_over(board):
            for i in range(1):
                position_x, shape_x = int(input("What position would you like to fill, player X?:")), "X"
                while not is_legal(board, position_x):
                    position_x, shape = int(input("What position would you like to fill, player X?:")), "X"
                fill_spot(board, position_x, shape_x)
                print_board(board)
            for i in range(1):
                position_o, shape_o = int(input("What position would you like to fill, player O?:")), "O"
                while not is_legal(board, position_o):
                    position_o, shape_o = int(input("What position would you like to fill, player O?:")), "O"
                fill_spot(board, position_o, shape_o)
                print_board(board)

        get_winner(board)
        want_to_play = input("Do you want to play again?")




def main():
    board = build_board()
    print_board(board)
    play(board)
if __name__ == '__main__':
    main()
