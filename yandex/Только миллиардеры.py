all_ = [i.split(',') for i in input().split(';')]
print(*[','.join([j for j in i if int(j) >= 10 ** 9]) for i in all_], sep='\n')
