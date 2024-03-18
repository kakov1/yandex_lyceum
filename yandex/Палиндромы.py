def palindrome(s):
    s_ = ''
    for i in range(len(s)):
        if s[i] != ' ':
            s_ += s[i]
    s_1 = list(s.lower())
    s_1.reverse()
    s_1 = ''.join(s_1)
    s_1.lower()
    s_1_ = ''
    for i in range(len(s_1)):
        if s_1[i] != ' ':
            s_1_ += s_1[i]
    if s_.lower() == s_1_:
        return 'Палиндром'
    else:
        return 'Не палиндром'
