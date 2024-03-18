def swap(first, second):
    first_copy = tuple(first)
    first.clear()
    first += tuple(second)
    second.clear()
    second += first_copy
