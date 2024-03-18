def find_farthest_orbit(list_of_orbits):
    max_ = 0
    answer = 0
    for i in list_of_orbits:
        if i[0] * i[1] * 3.14159 > max_ and i[0] != i[1]:
            answer = i
            max_ = i[0] * i[1] * 3.14159
    return answer
