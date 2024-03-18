class Table:
    def __init__(self, rows, cols):
        self.table = [[0 for __ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def get_value(self, row, col):
        return self.table[row][col] if 0 <= row < self.rows and 0 <= col < self.cols else None

    def set_value(self, row, col, value):
        self.table[row][col] = value

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols

    def delete_row(self, row):
        del self.table[row]
        self.rows = len(self.table)

    def delete_col(self, cols):
        for i in range(self.rows):
            del self.table[i][cols]
        self.cols = len(self.table[0])

    def add_row(self, row):
        if self.rows != 0:
            self.table.insert(row, [0 for _ in range(self.cols)])
        else:
            if self.cols != 0:
                self.table = [[0] for _ in range(self.cols)]
            else:
                self.table = [[0]]
        self.rows = len(self.table)

    def add_col(self, col):
        if self.cols != 0:
            for i in range(self.rows):
                self.table[i].insert(col, 0)
        else:
            if self.rows != 0:
                self.table = [[0] for _ in range(self.rows)]
            else:
                self.table = [[0]]
        self.cols = len(self.table[0])
        