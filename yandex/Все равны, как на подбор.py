def same_by(characteristic, objects):
    true_count = 1
    false_count = 1
    for i in range(1, len(objects)):
        previous = characteristic(objects[0])
        if characteristic(objects[i]) == previous:
            true_count += 1
        else:
            false_count += 1
    return True if true_count == len(objects) or false_count == len(objects) \
                   or not len(objects) else False
