from sys import stdin

print(any(map(lambda x: '0' in x, list(map(str.split, map(str.strip, stdin))))))
