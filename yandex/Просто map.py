def simple_map(transformation, values):
    values = tuple(values)
    values = list(values)
    for i in range(len(values)):
        values[i] = transformation(values[i])
    return values
