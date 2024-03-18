url = input()
url = url[url.index('?') + 1:]
url = url.split('&')
dict_ = dict()
for i in range(len(url)):
    dict_[url[i].split('=')[0]] = url[i].split('=')[1]
print(dict_[input()])
