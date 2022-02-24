"""
Name: Ashley Eidenberger
lab6.py

Problem: Create a program with a GUI that allows the user to encode a message.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import graphics


def vigenere():

    win = graphics.GraphWin("Message Encoder", 400, 400)
    button = graphics.Rectangle(graphics.Point(100, 250), graphics.Point(300, 300))
    prompt = graphics.Text(button.getCenter(), "Click to Proceed")
    message_prompt = graphics.Text(graphics.Point(75, 50), "Enter message:")
    message_entry = graphics.Entry(graphics.Point(250, 50), 25)
    key_prompt = graphics.Text(graphics.Point(75, 75), "Enter key:")
    key_entry = graphics.Entry(graphics.Point(250, 75), 25)

    message_prompt.draw(win)
    button.draw(win)
    prompt.draw(win)
    message_entry.draw(win)
    key_prompt.draw(win)
    key_entry.draw(win)
    win.getMouse()

    message = message_entry.getText()
    key = key_entry.getText()
    key = key.upper()
    key = key.replace(" ", "")
    message = message.upper()
    message = message.replace(" ", "")
    message_length = len(message)
    coded_message = ""

    for i in range(message_length):
        character_num = ord(message[i])
        char_num_val = character_num - 65
        key_num = ord(key[i % 3])
        key_num_val = key_num - 65
        key_shift = (char_num_val + key_num_val) % 26
        new_char_value = character_num + key_shift
        new_char = chr(new_char_value)
        coded_message = coded_message + new_char

    button.undraw()
    prompt.undraw()

    new_message = graphics.Text(graphics.Point(75, 100), "Encoded Message:")
    coded_message_text = graphics.Text(graphics.Point(200, 100), "")
    coded_message_text.setText(coded_message)
    new_message.draw(win)
    coded_message_text.draw(win)
    closing_text = graphics.Text(button.getCenter(), "Click to close")
    closing_text.draw(win)
    win.getMouse()


vigenere()
