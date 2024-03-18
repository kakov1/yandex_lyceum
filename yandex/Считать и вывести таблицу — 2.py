string = int(input())
column = int(input())
all_ = [input() for i in range(string * column)]
count = 0
for i in range(string):
    for j in range(column):
        print(all_[count + j], end='\t')
    print()
    count += column
print()
for i in range(column):
    count = 0
    for j in range(string):
        print(all_[i + count], end='\t')
        count += column
    print()
