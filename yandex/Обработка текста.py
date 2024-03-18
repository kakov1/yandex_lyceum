import functools
import sys

print(functools.reduce(lambda result, element: result + str(element[0]) +
      ' - ' + element[1] + '\n' if element[1] not in result else result + '',
            sorted(filter(lambda x: x[1][0].isupper(), enumerate(
                  ''.join([i for i in sys.stdin.read() if i not in '.;,:&^%$#@!*()']).split())),
            key=lambda x: x[1]), ''))
