from datetime import date as dt
from math import sin, pi

birth = dt(*map(int, input().split('.')[::-1]))
date = dt(*map(int, input().split('.')[::-1]))
t = (date - birth).days
print(*map(lambda x: round(x, 2),
      [sin((2 * pi * t) / 23) * 100, sin((2 * pi * t) / 28) * 100, sin((2 * pi * t) / 33) * 100]), sep='\n')
