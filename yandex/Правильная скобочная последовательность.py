def bracket_check(test_string):
    new = ''
    for i in test_string:
        if i == '(' or i == ')':
            new += i
    if len(new) % 2:
        print('NO')
    else:
        test_string = new
        for i in range(len(test_string) // 2):
            if test_string[0] == '(':
                count = 0
                test_string = test_string[1:]
                for j in test_string:
                    if j == ')':
                        test_string = test_string[:count] + test_string[count + 1:]
                        break
                    count += 1
            else:
                break
        if len(test_string) == 0:
            print('YES')
        else:
            print('NO')
