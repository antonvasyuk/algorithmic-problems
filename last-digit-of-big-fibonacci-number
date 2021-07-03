def fib_digit(n):
    '''найти последнюю цифру n-го числа Фибоначчи (1 <= n <= 10 ** 7)'''
    a = [0, 1]
    for i in range(2, n + 1):
        a.append((a[i - 1] + a[i - 2]) % 10)
    return a[n]
