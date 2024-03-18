all_ = []
for i in range(int(input())):
    current = input()
    current_views = {}
    if i == 0:
        current_views[current[:current.find(' ') + 1]] = current[current.rfind(': '):]
    else:

