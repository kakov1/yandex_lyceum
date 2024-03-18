import functools
import sys

print(sum(functools.reduce(
    lambda result, element: [result[0] + [int(element[0])], result[1]] if element in result[1]
    else [result[0], result[1] + [element]],
    map(lambda x: [x[:x.find(' ') + 1], x[x.find(' ') + 1:]],
        map(str.strip, sys.stdin)), [[0], []])[0]))
