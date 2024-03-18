class SeaMap:
    def __init__(self):
        self.field = [['.' for _ in range(10)] for __ in range(10)]

    def shoot(self, row, col, result):
        if result == 'miss':
            self.field[row][col] = '*'
        if result == 'hit':
            self.field[row][col] = 'x'
        if result == 'sink':
            self.field[row][col] = 'x'
            for i in range(10):
                for j in range(10):

                    self.field[i][j] = '*'

    def cell(self, row, col):
        return self.field[row][col]


sm = SeaMap()
sm.shoot(0, 0, 'sink')
sm.shoot(0, 9, 'sink')
sm.shoot(9, 0, 'sink')
sm.shoot(9, 9, 'sink')
for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()
