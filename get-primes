def get_primes(n):
    '''найти все простые числа до n включительно'''
    res = []
    if n > 1:
        res.append(2)
        for i in range(3, n + 1, 2):
            for j in range(3, int(i ** 0.5) + 1, 2):
                if i % j == 0:
                    break
            else:
                res.append(i)
    return res
