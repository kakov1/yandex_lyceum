from math import sqrt, sin, cos, pi

t = 0
all_s = []
while True:
    if t > 2 * pi:
        break
    x = cos(t) ** 3
    y = sin(t) ** 3
    s = sqrt((x - 0.75) ** 2 + y ** 2)
    all_s.append(round(s, 4))
    t += 0.0001

print(min(all_s))
