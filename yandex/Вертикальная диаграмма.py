start = input().split()
count = 0
for i in range(int(max(map(int, start))) + 2):
    if i == 0:
        print('*' * (len(start) + 2))
    elif i == 1:
        void = len(start) - 2
        if void < 0:
            print('*', '*')
        else:
            print('*', ' ' * void, '*')
        count = int(max(map(int, start)))
    elif i == int(max(map(int, start))) + 1:
        print('*' * (2 + len(start)))
    else:
        print('*', end='')
        for j in start:
            if int(j) >= count:
                print('*', end='')
            else:
                print(' ', end='')
        print('*')
        count -= 1
