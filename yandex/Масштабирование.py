height = int(input())
length = int(input())
all_ = []
for i in range(height):
    all_.append(input())
for i in range(1, height + 1, 2):
    for j in range(1, length + 1, 2):
        print(all_[i - 1][j - 1], end='')
    print()
