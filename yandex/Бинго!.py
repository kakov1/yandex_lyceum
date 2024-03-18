from random import sample, shuffle


def make_bingo():
    nums = list(range(1, 76))
    shuffle(nums)
    card = list()
    for i in range(5):
        if i == 2:
            cur = sample(nums, k=2)
            card.append([*cur, 0])
            for j in cur:
                del nums[nums.index(j)]
            cur = sample(nums, k=2)
            card[-1].extend(cur)
            card[-1] = tuple(card[-1])
        else:
            cur = sample(nums, k=5)
            card.append(tuple(cur))
        for j in cur:
            del nums[nums.index(j)]
    return tuple(card)
