def transpose(matrix):
    matrix_copy = [[]]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            matrix_copy[-1].append(matrix[j][i])
        matrix_copy.append(list())
    del matrix_copy[-1]
    matrix.clear()
    matrix += matrix_copy
