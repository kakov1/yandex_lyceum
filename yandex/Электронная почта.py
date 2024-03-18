alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.@'
string = input()
card = input()
check = True
check_2 = True
answer = []
answer_check = True
for i in string:
    if i not in alphabet:
        print('Impossible')
        check = False
        break
count = -1
if check and not string.isalnum():
    if (string.count('@') == 1 and string.count('.') == 1) or string.count('@') == 1 or string.count('.') == 1:
        if '@' in string and '.' in string:
            string = string.split('@')
            string[1] = string[1].split('.')
            if len(string) == 2 and len(string[1]) == 2:
                print('Done')
            elif len(string) == 2 and len(string[1]) == 1:
                for i in range(len(card)):
                    if card[count] != '@' and card[count] != '.':
                        print(len(string[0]))
                    else:
                        print('Impossible')
                        break
                    count -= 1
        elif '@' in string:
            if '.' in card[card.rfind('@') + 1:] and '@' not in card[card.rfind('@') + 1:]:
                string = string.split('@')
                if len(string) == 1:
                    for i in range(len(card)):
                        answer.append(len(string[0]))
                        count -= 1
            else:
                print('Impossible')
        elif '.' in string:
            string.split('.')
            pass
    else:
        print('Impossible')
elif check and string.isalnum():
    pass
