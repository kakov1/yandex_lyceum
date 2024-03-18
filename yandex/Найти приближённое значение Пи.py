from random import random

points = []
points_quarter = []
for i in range(150000):
    x = random()
    y = random()
    if (x ** 2 + y ** 2) ** 0.5 <= 1:
        points_quarter.append((x, y))
    points.append((x, y))
print((4 * len(points_quarter)) / len(points))
