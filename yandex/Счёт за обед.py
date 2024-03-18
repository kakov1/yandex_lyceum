def count_food(days):
    sum_ = 0
    for i in days:
        sum_ += daily_food[i - 1]
    return sum_
