from sys import stdin

data = list(map(lambda x: x.strip(), list(filter(lambda x: x != '\n', stdin))))
print(len(list(filter(lambda x: x[0] == '#', data))))
