a = input()
b = [0 for i in range(3 * 10000)]
count = 0
count_ = 0
for i in a:
    if i == '[':
        count_ += 2
    elif count_ != 0 and i == ']':
        count_ -= 1
    elif count_ != 0 and i != ']':
        if b[count] == 0:
            count += 1
        else:
            if i == '>':
                while b[count] != 0:
                    count += 1
            elif i == '<':
                while b[count] != 0:
                    count -= 1
            elif i == '+':
                b[count] = 0
            elif i == '-':
                b[count] = 0
            else:
                print(b[count])
        count_ -= 1
    elif i == '>':
        count += 1
    elif i == '<':
        count -= 1
    elif i == '+':
        if b[count] == 255:
            b[count] = 0
        else:
            b[count] += 1
    elif i == '-':
        if b[count] == 0:
            b[count] = 255
        else:
            b[count] -= 1
    else:
        print(b[count])
