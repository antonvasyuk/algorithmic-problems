def max_subarray_without_repeats(arr):
    '''найти максимальную длину подмассива без повторяющихся элементов'''
    i = 0
    j = 0
    best = 0
    s = set()
    while i < len(arr) and j < len(arr):
        if arr[i] not in s:
            s.add(arr[i])
            best = max(best, len(s))
            i += 1
        else:
            while arr[i] in s:
                s.remove(arr[j])
                j += 1
    return best
