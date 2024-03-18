nums, count = input().split(), 0
for i in nums:
    guess = []
    check = int(i)
    while check != 0:
        if check % 2:
            guess.append('1')
        else:
            guess.append('0')
        check //= 2
    guess.reverse()
    nums[count] = ''.join(guess)
    count += 1
list_ = []
dict_ = dict()
for i in nums:
    dict_ = dict()
    dict_['digits'] = len(i)
    dict_['units'] = i.count('1')
    dict_['zeros'] = i.count('0')
    list_.append(dict_)
print(list_)
