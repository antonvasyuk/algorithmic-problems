def range_with_maximum_sum(lst):
    '''найти подмассив с максимальной суммой'''
    if not lst:
        return 0, -1, -1
    best = lst[0]
    begin = 0
    end = 0
    range_sum = 0
    last_negative = -1
    for i in range(len(lst)):
        range_sum += lst[i]
        if range_sum > best:
            best = range_sum
            begin = last_negative + 1
            end = i
        if range_sum < 0:
            range_sum = 0
            last_negative = i
    return best, begin, end
