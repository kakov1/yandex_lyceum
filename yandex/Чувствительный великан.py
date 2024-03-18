a = input().split()
b = input().split('/' + '\\')
c = input().split('***')
for i in a:
    print(i + ':')
    count = 0
    one = []
    print_ = []
    for j in b:
        if j.lower() <= i.lower() and j.lower()[-1] in i.lower():
            print_.append(j)
    for j in print_:
        if j == print_[-1]:
            print(j.capitalize())
        else:
            print(j.capitalize(), end=' ! ')
    if len(print_) == 0:
        print()
    print_ = []
    check = []
    for j in c:
        count = 0
        if len(set(list(j.lower())).intersection(set(i.lower()))) <= 2 and len(j) < len(i):
            print_.append(j)
    for j in print_:
        if j == print_[-1]:
            print(j)
        else:
            print(j, end=f' {i.lower()[0]} ')
    if len(print_) == 0:
        print()
