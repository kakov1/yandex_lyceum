string = input()
check_2 = len(string)
check = False
if len(string) % 2:
    current = string[len(string) // 2]
    string = string[:len(string) // 2] + string[len(string) // 2 + 1:]
    near_count = 1
    check = True
else:
    current = string[len(string) // 2 - 1:len(string) // 2 + 1]
    string = string[:len(string) // 2 - 1] + string[len(string) // 2 + 1:]
    near_count = 1
count = len(string) // 2 - len(current)
check_1 = len(string) // 2
for i in range(len(string) // 2 + 1):
    if i == 0:
        if check_2 == 2 or check_2 == 1:
            print(current)
        elif check:
            print(' ' * count, current)
        else:
            print(' ' * (count + 1), current)
        count = len(string) // 2
    else:
        if check:
            if check_2 == 3:
                print(string[count - 1], string[count])
            elif i == 1:
                print(' ' * (count - len(current) - 1), string[count - 1], string[count])
            elif i == check_1:
                print(string[count - 1], ' ' * (near_count - 2), string[count])
            else:
                print(' ' * (count - len(current) - 1), string[count - 1], ' ' * (near_count - 2), string[count])
        else:
            if i == check_1:
                print(string[count - 1], ' ' * (near_count - 1), string[count])
            else:
                print(' ' * (count - len(current)), string[count - 1], ' ' * (near_count - 1), string[count])
        near_count += 2
        string = string[:count - 1] + string[count + 1:]
        count = len(string) // 2
