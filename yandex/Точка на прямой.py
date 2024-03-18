def line(s, t):
    s = s.split('x')
    k = float(s[0])
    b = float(''.join(s[1][1:]))
    t = t.split(';')
    if s[1][0] == '+':
        if k * float(t[0]) + b == float(t[1]):
            print('True')
        else:
            print('False')
    else:
        if k * float(t[0]) - b == float(t[1]):
            print('True')
        else:
            print('False')
