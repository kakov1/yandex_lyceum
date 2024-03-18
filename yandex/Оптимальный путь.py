from sys import stdin


def way(data, guess):
    roads = []
    if guess[1] in data[guess[0]]:
        return
    return way(way(data[guess[0]][:-1]))


data = list(map(str.split, map(str.strip, stdin)))
guess = data[-1]
roads = dict()
for i in data[:-1]:
    if int(i[0]) in roads.keys():
        roads[int(i[0])].append((int(i[1]), int(i[2])))
    else:
        roads[int(i[0])] = [(int(i[1]), int(i[2]))]

print(roads)
