def upper_bound(sorted_lst, n):
    left = -1
    right = len(sorted_lst)
    while right > left + 1:
        middle = (left + right) >> 1
        if sorted_lst[middle] > n:
            right = middle
        else:
            left = middle
    return right
