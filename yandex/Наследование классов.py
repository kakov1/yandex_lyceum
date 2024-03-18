n = int(input())
classes = []
for i in range(n):
    classes.append(input().split())
y, x = input().split()
dict_ = {}
for i in classes:
    if i[1] in dict_.keys() and i[0] in dict_.keys():
        dict_[i[0]] += dict_[i[1]]
    else:
        dict_[i[0]] = [i[1]]
check = False
while True:
    count = 0
    for i in range(len(dict_[x])):
        if dict_[x][i] in dict_.keys():
            count += 1
            dict_[x] += dict_[dict_[x][i]]
            if x in dict_[x]:
                check = True
                break
            del dict_[x][i]
    if count == 0 or check:
        break
if len(dict_[x]) != len(set(dict_[x])) or check:
    print('Impossible')
elif y not in dict_[x]:
    print('NO')
else:
    print('YES')
