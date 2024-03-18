all_, check, previous = {}, [], ['0', '0', '0']
for i in range(int(input())):
    info = input().split()
    if previous[2] != info[2]:
        previous = info
    if info[2] in all_.keys():
        if isinstance(all_[info[2]], str):
            all_[info[2]] = [all_[info[2]].split()]
        all_[info[2]] = all_[info[2]].append(info[:2])
        check.append(info[2])
    else:
        all_[info[2]] = ' '.join(info[:2])
dates = []
check_2 = []
all_guess = []
a = int(input())
for i in range(a):
    guess = input()
    kuk = False
    count = 0
    dates = []
    check_2 = []
    if guess in all_.keys():
        if guess in check:
            all_[guess].sort()
            for j in all_[guess]:
                dates.append(int(j[1]))
            dates.sort()
            for j in dates:
                for k in all_[guess]:
                    if str(j) in k and k not in check_2:
                        if len(check_2) + 1 == len(dates):
                            print(' '.join(k))
                        else:
                            print(' '.join(k), end=' ')
                            kuk = True
                        check_2.append(k)
        else:
            print(all_[guess])
    else:
        print()
