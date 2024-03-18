string = input()
a = [' * ', '* *', '***', '* *', '* *']
b = ['** ', '* *', '** ', '* *', '** ']
c = [' * ', '* *', '*  ', '* *', ' * ']
count = 0
for i in range(5):
    for j in string:
        if j == 'A':
            print(a[count], end='  ')
        elif j == 'B':
            print(b[count], end='  ')
        else:
            print(c[count], end='  ')
    count += 1
    print()
