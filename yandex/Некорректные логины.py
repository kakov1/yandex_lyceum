started = input().split(',')
check = ['ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890_']
check.append(''.join(check).lower())
check = ''.join(check)
check = list(check)
wrong = []
for i in started:
    for j in i:
        if j not in check:
            wrong.append(i)
            break
wrong.sort()
void = 0
for i in wrong:
    if len(i) > void:
        void = len(i)
for i in wrong:
    if len(i) == void:
        print(i)
    else:
        print(' ' * (void - len(i) - 1), i)
