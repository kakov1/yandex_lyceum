import functools
import sys

print(functools.reduce(lambda result, element: result if element > result else element,
                       list(map(str.strip, sys.stdin))).strip())
