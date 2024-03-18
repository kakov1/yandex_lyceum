dict_ = dict()


def add_friends(name_of_person, list_of_friends):
    if name_of_person in dict_.keys():
        dict_[name_of_person].extend(list_of_friends)
    else:
        dict_[name_of_person] = list_of_friends


def are_friends(name_of_person1, name_of_person2):
    if name_of_person1 in dict_.keys() and \
            name_of_person2 in dict_[name_of_person1]:
        return True
    elif name_of_person2 in dict_.keys() and \
            name_of_person1 in dict_[name_of_person2]:
        return True
    else:
        return False


def print_friends(name_of_person):
    if name_of_person in dict_.keys():
        print(*sorted(dict_[name_of_person]))
    else:
        for key, value in dict_.items():
            if name_of_person in value:
                value.append(name_of_person)
                print(*sorted(value))
