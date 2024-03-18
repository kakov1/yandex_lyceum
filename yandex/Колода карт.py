from itertools import product
from sys import stdin

a = ['пик', 'бубен', 'червей', 'треф']
b = [*[f'{i}' for i in range(2, 11)], 'валет', 'дама', 'король', 'туз']
print(*product(b, filter(lambda x: x  input(), a)))
