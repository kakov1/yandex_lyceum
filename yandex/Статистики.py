def print_statistics(arr):
    if not len(arr):
        print('0', '0', '0', '0', '0', sep='\n')
    else:
        print(len(arr))
        print(sum(arr) / len(arr))
        print(min(arr))
        print(max(arr))
        if len(arr) % 2:
            print(sorted(arr)[len(arr) // 2])
        else:
            print((sorted(arr)[len(arr) // 2] + sorted(arr)[len(arr) // 2 - 1]) / 2)
