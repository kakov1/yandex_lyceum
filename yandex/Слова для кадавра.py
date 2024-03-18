template = input()
vowels = 'аоуэюяыеиё'
all_ = []
guess = ''
while True:
    guess = input()
    if guess == '':
        break
    else:
        all_.append(guess)
print_ = []
count = 0
template_copy = template
for i in all_:
    check = 0
    count = 0
    template = template_copy
    if (len(i) < len(template) and '*' not in template) or '*' in template and (len(i) - 1 == len(template)):
        continue
    for j in template:
        if count + 1 == len(i) and count + 1 != len(template):
            break
        if j == '1':
            if i[count] not in vowels:
                check += 1
        elif j == '0':
            if i[count] in vowels:
                check += 1
        elif j == '*':
            template = list(template[count + 1:])
            template.reverse()
            template = ''.join(template)
            new = list(i[count + 1:])
            new.reverse()
            new = ''.join(new)
            count_ = 0
            check_ = 0
            check__ = True
            for k in template:
                if k == '1':
                    if len(new) == count_:
                        check__ = not check__
                        break
                    if new[count_] not in vowels:
                        check_ += 1
                elif k == '0':
                    if len(new) == count_:
                        check__ = not check__
                        break
                    if new[count_] in vowels:
                        check_ += 1
                    else:
                        break
                elif k == '?':
                    check_ += 1
                count_ += 1
            if len(template) == check_ or len(new) == check_ and check__:
                check += len(new) + 1
                break
            break
        elif j == '?':
            check += 1
        count += 1
    if check == len(i):
        print_.append(i)
if len(print_) != 0:
    for i in print_:
        print(i)
else:
    print('Есть нечего, значить!')
