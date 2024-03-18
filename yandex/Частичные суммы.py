def partial_sums(*args):
    if len(args) == 0:
        sums = [0]
    else:
        sums = [0, args[0]]
    for i in range(2, len(args) + 1):
        sums.append(sum(args[:i]))
    return sums
