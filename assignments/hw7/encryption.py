def encode(message, key):
    message_output = ''
    message_char_length = len(message)
    for i in range(message_char_length):
        num = message[i]
        num = ord(message[i]) + key
        character = chr(num)
        message_output = message_output + character
    return message_output


def encode_better(message, key):
    key_val = key
    key_length = len(key_val)
    message_length = len(message)
    coded_message = ""

    for i in range(message_length):
        character_num = ord(message[i])
        key_num = ord(key_val[i % key_length])
        character_num = character_num - 65
        key_num = key_num - 65
        shift_val = (character_num + key_num) % 58
        coded_val = shift_val + 65
        coded_val = chr(coded_val)
        coded_message = coded_message + coded_val

    return coded_message
