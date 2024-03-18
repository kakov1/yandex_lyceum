def find_mountain(heightsMap):
    x, y = 0, 0
    max_ = 0
    for i in range(len(heightsMap)):
        for j in range(len(heightsMap[i])):
            if heightsMap[i][j] > max_:
                x, y = i, j
                max_ = heightsMap[i][j]
    return x, y
