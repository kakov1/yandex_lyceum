n = str(1 / int(input())).split('.')[1]
max_count = 0
check = []
count = 0
if len(n) < 16:
    print(0)
    exit()
else:
    for i in n:
        if n.count(i) > max_count and i not in check:
            max_count = n.count(i)
            del check[:count]
            check.append(i)
        elif (n.count(i) == max_count or n.count(i) == max_count - 1) and i not in check:
            check.append(i)
        count += 1
    print(*check, sep='')
