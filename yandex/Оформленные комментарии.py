from sys import stdin

data = list(map(str.strip, stdin))
comments = list(filter(lambda x: x[0] == '#', data))
for i in comments:
    print(f'Line {data.index(i) + 1}: {i[i.index("#") + 1:].strip()}')
