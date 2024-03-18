previous = ''


def print_without_duplicates(message):
    global previous
    if previous != message:
        print(message)
    previous = message
