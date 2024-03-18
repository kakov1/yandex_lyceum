access = [input().split('/') for _ in range(int(input()))]
ask = [input().split('/') for _ in range(int(input()))]
check = True
for j in range(len(ask)):
    if len(access[j]) > len(ask[j]):
        for i in range(len(ask[j])):
            if access[i] != ask[i]:
                print('NO')
                check = False
        if check:
            print('YES')
    else:
        for i in range(len(access[j])):
            if access[i] != ask[i]:
                print('NO')
                check = False
        if check:
            print('YES')
