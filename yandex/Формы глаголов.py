from sys import stdin
import pymorphy2

data = []
for i in stdin.read().split():
    current = pymorphy2.MorphAnalyzer().parse(i)
    for j in current:
        if j.tag.POS:
            data.append(j.normal_form)
    current.clear()
check = 'видеть, увидеть, глядеть, примечать, узреть'.split(', ')
count = 0
for i in data:
    if i in check:
        count += 1
print(count)
