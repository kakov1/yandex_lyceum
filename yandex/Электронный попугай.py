list_ = list()


def parrot(phrase):
    print(phrase) if phrase in list_ else list_.append(phrase)
