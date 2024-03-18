all_ = [(input(), int(input())) for i in range(int(input()))]
score = []
for i in range(len(all_)):
    score.append(all_[i][1])
score.sort(reverse=True)
if len(all_) % 2:
    final_score = score[:len(score) // 2 + 1]
else:
    final_score = score[:len(score) // 2]
if len(all_) % 2:
    other_score = score[len(score) // 2 + 1:]
else:
    other_score = score[len(score) // 2:]
final = []
other = []
for i in final_score:
    for j in all_:
        if i in j:
            final.append(j[0])
for i in other_score:
    for j in all_:
        if i in j:
            other.append(j[0])
final.sort()
other.sort()
print(*final, sep='\n')
print(*other, sep='\n')


