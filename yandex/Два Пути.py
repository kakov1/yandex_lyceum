s = int(input())
before = []
for i in range(s):
    before.append(int(input()))
brother_1 = tuple(before)
brother_2 = tuple(before)
brother_1 = list(brother_1)
brother_2 = list(brother_2)
for i in range(int(input())):
    who = int(input())
    if who == 1:
        brother_1[int(input())] += int(input())
    else:
        brother_2[int(input())] += int(input())
print(*brother_1)
print(*brother_2)
count = 0
for i in range(len(brother_1)):
    if brother_1[i] == brother_2[i]:
        count += 1
print(count)
