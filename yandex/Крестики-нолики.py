def tic_tac_toe(field):
    winner = ''
    for i in range(3):
        field[i] = ''.join(field[i])
    for i in field:
        if i == 'xxx':
            winner = 'x win'
        elif i == '000':
            winner = '0 win'
    if len(winner) == 0:
        for i in range(3):
            count = 1
            for j in range(1, 3):
                if field[j][i] == field[j - 1][i] and field[j][i] != '-':
                    count += 1
                if count == 3:
                    winner = field[j][i] + ' win'
        if len(winner) == 0:
            if field[0][0] == field[1][1] == field[2][2] or\
                    field[2][0] == field[1][1] == field[0][2]:
                if field[1][1] == 'x':
                    winner = 'x win'
                elif field[1][1] == '0':
                    winner = '0 win'
    if len(winner) > 0:
        print(winner)
    else:
        print('draw')
