def group_equal(els):
    value = []
    element = [None, 0]
    for x in els:
        if x == element[0]:
            element[1] += 1
        else:
            if element[0] != None:
                value.extend([[element[0]] * element[1]])
            element = [x, 1]
    else:
        if element[0] != None:
            value.extend([[element[0]] * element[1]])
    return value
