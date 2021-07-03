def make_prefix_sum(A):
    '''вернуть массив префиксных сумм списка A'''
    prefix_sum = [0] * (len(A) + 1)
    for i in range(1, len(A) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]
    return prefix_sum
