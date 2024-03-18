letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


def string_to_coordinates(string):
    return letters.index(string[0]) + 1, int(string[1])


def coordinates_to_string(coordinates):
    return f'{letters[coordinates[0] - 1]}{coordinates[1]}'


def possible_turns(cell):
    cell = string_to_coordinates(cell)
    answer = []
    for i in range(8):
        new_ = ''
        if i == 0:
            new_ = (cell[0] + 2, cell[1] + 1)
        elif i == 1:
            new_ = (cell[0] + 2, cell[1] - 1)
        elif i == 2:
            new_ = (cell[0] - 2, cell[1] + 1)
        elif i == 3:
            new_ = (cell[0] + 1, cell[1] + 2)
        elif i == 4:
            new_ = (cell[0] + 1, cell[1] - 2)
        elif i == 5:
            new_ = (cell[0] - 1, cell[1] + 2)
        elif i == 6:
            new_ = (cell[0] - 1, cell[1] - 2)
        else:
            new_ = (cell[0] - 2, cell[1] - 1)
        if max(new_) <= 8 and min(new_) >= 1:
            answer.append(coordinates_to_string(new_))
    answer.sort()
    return answer
