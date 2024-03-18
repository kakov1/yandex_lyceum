import functools
import sys

print(*[i[0][:-3] + ' - ' + str(int(i[0][:-3]) + 100) + ': ' + ', '.join(i[1:]) if i[
    0] != '00000' else '0' + ' - ' + '100' + ': ' + ', '.join(
    i[1:]) for i in map(sorted, functools.reduce(
        lambda result, element: result + [element] if all([element[1] not in i for i in result]) else result[:-1] + [
            [*result[-1], element[0]]], (map(lambda x: [x[0], x[2][0:len(x[2]) - 5] + '0' *
                                                        (len(x[2]) - len(x[2]) + 5)],
                                         sorted(map(str.split, sys.stdin.read().split('\n')),
                                                key=lambda x: int(x[2])))), []))], sep='\n')
