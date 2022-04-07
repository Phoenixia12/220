"""
Name: Ashley Eidenberger
lab11.py

Problem: Create a program that prompts the user to try and guess which door is 'secret' once the user guesses a
door track their win or loss and ask them to play again, the user can quit at anytime by pressing the quit button

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import graphics
from random import randint
from lab10.door import Door
from lab10.button import Button

def main():
    game_board = graphics.GraphWin('Three Door Game', 900, 900)
    quit_game = Button(graphics.Rectangle(graphics.Point(650,50), graphics.Point(850, 100)), 'Quit')
    quit_game.draw(game_board)
    wins = Button(graphics.Rectangle(graphics.Point(25, 50), graphics.Point(75, 100)), '0')
    win = 0
    wins.draw(game_board)
    losses = Button(graphics.Rectangle(graphics.Point(75, 50), graphics.Point(125, 100)), '0')
    loss = 0
    losses.draw(game_board)
    point = graphics.Point(0, 0)

    while not quit_game.is_clicked(point):
        if not quit_game.is_clicked(point):
            instructions = graphics.Text(graphics.Point(425, 75), '')
            instructions.setText('I have a secret door')
            instructions.draw(game_board)

            door_1 = Door(graphics.Rectangle(graphics.Point(50, 150), graphics.Point(200, 550)), 'Door 1', False)
            door_1.door_color('grey')
            door_1.draw(game_board)
            door_2 = Door(graphics.Rectangle(graphics.Point(350, 150), graphics.Point(500, 550)), 'Door 2', False)
            door_2.door_color('grey')
            door_2.draw(game_board)
            door_3 = Door(graphics.Rectangle(graphics.Point(650, 150), graphics.Point(800, 550)), 'Door 3', False)
            door_3.door_color('grey')
            door_3.draw(game_board)

            play_again = graphics.Text(graphics.Point(425, 625), ' ')
            play_again.setText('Click to guess which is the secret door!')

            play_again.draw(game_board)
            val = randint(1, 3)
            if val == 1:
                door_1.set_secret(True)
            if val == 2:
                door_2.set_secret(True)
            if val == 3:
                door_3.set_secret(True)
            point = game_board.getMouse()
            if door_1.is_clicked(point):
                if door_1.is_secret():
                    door_1.door_color('green')
                    win = win + 1
                    wins.set_label(str(win))
                    instructions.setText('you win!')
                    play_again.setText('click anywhere to play again')
                else:
                    door_1.door_color('red')
                    if door_2.is_secret():
                        door_2.door_color('green')
                        loss = loss + 1
                        losses.set_label(str(loss))
                        instructions.setText('you lose')
                        play_again.setText('click anywhere to play again')
                    else:
                        door_3.door_color('green')
                        loss = loss + 1
                        losses.set_label(str(loss))
                        instructions.setText('you lose')
                        play_again.setText('click anywhere to play again')

            if door_2.is_clicked(point):
                if door_2.is_secret():
                    door_2.door_color('green')
                    win = win + 1
                    wins.set_label(str(win))
                    instructions.setText('you win!')
                    play_again.setText('click anywhere to play again')
                else:
                    door_2.door_color('red')
                    if door_1.is_secret():
                        door_1.door_color('green')
                        loss = loss + 1
                        losses.set_label(str(loss))
                        instructions.setText('you lose')
                        play_again.setText('click anywhere to play again')
                    else:
                        door_3.door_color('green')
                        loss = loss + 1
                        losses.set_label(str(loss))
                        instructions.setText('you lose')
                        play_again.setText('click anywhere to play again')

            if door_3.is_clicked(point):
                if door_3.is_secret():
                    door_3.door_color('green')
                    win = win + 1
                    wins.set_label(str(win))
                    instructions.setText('you win!')
                    play_again.setText('click anywhere to play again')
                else:
                    door_3.door_color('red')
                    if door_1.is_secret():
                        door_1.door_color('green')
                        loss = loss + 1
                        losses.set_label(str(loss))
                        instructions.setText('you lose')
                        play_again.setText('click anywhere to play again')
                    else:
                        door_2.door_color('green')
                        loss = loss + 1
                        losses.set_label(str(loss))
                        instructions.setText('you lose')
                        play_again.setText('click anywhere to play again')
        point = game_board.getMouse()
        instructions.undraw()
        play_again.undraw()








main()