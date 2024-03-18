def matrix(*args):
    matrix_ = []
    if len(args) == 0:
        return '0'
    elif len(args) == 1:
        for i in range(args[0]):
            string = []
            for j in range(args[0]):
                string.append('0')
            matrix_.append(string)
    elif len(args) == 2:
        for i in range(args[0]):
            string = []
            for j in range(args[1]):
                string.append('0')
            matrix_.append(string)
    else:
        for i in range(args[0]):
            string = []
            for j in range(args[1]):
                string.append(f'{args[2]}')
            matrix_.append(string)
    return matrix_
