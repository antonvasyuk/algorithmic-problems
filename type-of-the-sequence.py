def type_of_sequence(lst):
    ''' возвращает тип последовательности '''
    if not lst:
        return 'EMPTY'
    constant = True
    ascending = True
    weakly_ascending = True
    descending = True
    weakly_descending = True
    prev = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < prev:
            constant = False
            ascending = False
            weakly_ascending = False
        if lst[i] > prev:
            constant = False
            descending = False
            weakly_descending = False
        if lst[i] == prev:
            ascending = False
            descending = False
        prev = lst[i]
    if constant:
        return 'CONSTANT'
    if ascending:
        return 'ASCENDING'
    if weakly_ascending:
        return 'WEAKLY ASCENDING'
    if descending:
        return 'DESCENDING'
    if weakly_descending:
        return 'WEAKLY DESCENDING'
    return 'RANDOM'
