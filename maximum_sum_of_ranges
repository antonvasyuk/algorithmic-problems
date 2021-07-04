def max_sum(lst, ranges):
    '''найти максимальную сумму элементов списка lst на отрезках из списка ranges'''
    pref = [0] * (len(lst) + 1)
    for i in range(1, len(pref)):
        pref[i] = pref[i - 1] + lst[i - 1]
    best = -10 ** 9
    for x in ranges:
        best = max(best, pref[x[1] + 1] - pref[x[0]])
    return best
