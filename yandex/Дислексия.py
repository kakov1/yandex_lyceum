import itertools

dictionary = set(input().lower().split())
letter = input().lower().split()
print(*[i if (len(set(map(''.join, itertools.permutations(i))).intersection(
    dictionary)) == 1 and i in dictionary) or len(
    set(map(''.join, itertools.permutations(i))).intersection(dictionary)) < 1
             and i not in dictionary
             else '#' * len(i) for i in letter])
