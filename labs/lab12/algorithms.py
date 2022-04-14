def read_data(file_name):
    in_file = open(file_name, 'r')
    line = in_file.readline()
    values = []
    line = line.split()

    while line:
        i = 0
        while i < len(line):
            val = line[i]
            val = eval(val)
            values = values + [val]
            i = i + 1
        line = in_file.readline()
        line = line.split()
    return values


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if values[i] == search_val:
            return True
        i = i + 1
    return False
