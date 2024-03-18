birth = {}
for i in range(int(input())):
    info = input().split()
    if info[2] in birth.keys():
        birth[info[2]] = birth[info[2]] + ' ' + info[0]
    else:
        birth[info[2]] = info[0]
for i in range(int(input())):
    guess = input()
    if guess in birth.keys():
        print(*sorted(birth[guess].split()))
    else:
        print()
