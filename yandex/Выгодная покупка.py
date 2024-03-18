import sys

data = list(map(str.strip, sys.stdin))
books = data[0]
sums = min({i[0]: sum(map(int, i[1:])) for i in data[1:]}, key=lambda x: x[1])
for i in data:

