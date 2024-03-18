from sys import stdin
import pymorphy2

data = [i[:-1].lower() if i.isalpha() and not i[-1].isalpha()
        else i.lower() if i.isalpha() else  for i in stdin.read().split()]
print(data)