from sys import stdin
from random import choice

data = list(map(str.strip, stdin))
data_ = tuple(data)
for i in data_:
    friend = choice(data)
    while friend == i:
        friend = choice(data)
    print(i, ' - ', friend)
    del data[data.index(friend)]
