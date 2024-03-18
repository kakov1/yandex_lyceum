c = 1
a = []
b = []
for i in range(int(input())):
    a = []
    while c:
        c = input().strip().split()
        if c == ['*']:
            break
        else:
            a.extend(c)
    b.append(a)
b.reverse()
for i in b:
    if b.index(i) + 1 == len(b):
        print('-'.join(i))
    else:
        print('-'. join(i), end=', ')
