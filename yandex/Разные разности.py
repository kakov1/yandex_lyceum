all_, ready = [int(input()) for i in range(int(input()))], []
for i in all_:
    for j in all_:
        ready.append(i - j)
ready = set(ready)
ready = list(ready)
ready.sort()
print(*ready, sep='\n')
