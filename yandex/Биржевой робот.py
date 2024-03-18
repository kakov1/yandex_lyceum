all_ = []
cost = -1
while True:
    cost = int(input())
    if cost == 0:
        break
    all_.append(cost)
count = 0
buy = 0
for i in all_:
    if count != 0:
        if i > all_[count - 1]:
            buy = i
            break
    count += 1
count_ = 0
sell = 0
for i in all_[count:]:
    if count_ != 0:
        if i < all_[count:][count_ - 1]:
            sell = i
            break
    count_ += 1
print(buy, sell, sell - buy)
