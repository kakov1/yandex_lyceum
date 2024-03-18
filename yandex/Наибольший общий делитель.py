import functools
import math
import sys

print(functools.reduce(lambda result, element: math.gcd(result, element),
                       map(int, map(str.strip, sys.stdin)), 0))
