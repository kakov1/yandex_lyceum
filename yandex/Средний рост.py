from sys import stdin

data = list(map(int, map(str.strip, stdin)))
print(sum(data) / len(data) if len(data) != 0 else -1)
