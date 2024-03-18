all_ = []


def print_only_new(message):
    global all_
    if message not in all_:
        print(message)
        all_.append(message)
