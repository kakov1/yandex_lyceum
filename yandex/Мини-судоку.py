from sys import stdin


def make_assumptions(sudoku):
    for i, row in enumerate(sudoku):
        for j, value in enumerate(row):
            if not value:
                values = set(row) \
                         | set([sudoku[k][j] for k in range(4)]) \
                         | set([sudoku[m][n] for m in range((i // 2) * 2, (i // 2) * 2 + 2)
                                for n in range((j // 2) * 2, (j // 2) * 2 + 2)])
                yield i, j, list(set(range(1, 5)) - values)


def solve_sudoku(sudoku):
    if all([k for row in sudoku for k in row]):
        return sudoku
    assumptions = list(make_assumptions(sudoku))

    x, y, values = min(assumptions, key=lambda x: len(x[2]))

    for v in values:
        new_sudoku = sudoku
        new_sudoku[x][y] = v
        s = solve_sudoku(new_sudoku)
        if s:
            return s
    return None


for i in solve_sudoku([[int(j) for j in i] for i in list(map(str.strip, stdin))]):
    print(*i, sep='')
