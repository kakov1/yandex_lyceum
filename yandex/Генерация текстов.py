from swift import words
from random import choice

dict_ = dict()
for i in range(len(words)):
    if i != len(words) - 1:
        if words[i] in dict_.keys():
            dict_[words[i]].append(words[i + 1])
        else:
            dict_[words[i]] = [words[i + 1]]
current = choice([*dict_.keys()])
string = ''
check = [True, False, False, False, False, False, False, False, False, False]
first = True
while True:
    current_ = current
    if first or current.isalnum() or current == '-' or not string[-1].isalnum():
        if first:
            string += current.capitalize()
        else:
            string += ' ' + current
        current = choice(dict_[current])
        first = not first
    else:
        string += current
        current = choice(dict_[string[string.rfind(' ') + 1:string.rfind(current_)]])
        while current not in dict_[current_]:
            if current_ == '.':
                break
            current = choice(dict_[current_])
    if len(string) >= 80 and all(map(str.isalnum, dict_[current_])):
        print(string.strip())
        if string[-1] == '.' and choice(check):
            break
        string = ''
