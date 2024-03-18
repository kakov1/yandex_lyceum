import sys

data = list(map(str.split, sys.stdin.readlines()))
print('YES' if set([sum(map(int, i)) for i in data]) == set(
    map(sum, list(zip(*[i for i in [list(map(int, data[j])) for j in range(len(data))]])))) else 'NO')
