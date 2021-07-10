def find_the_nearest_element(sorted_lst_length, sorted_lst, lst):
    '''найти ближайший по модулю элемент для каждого элемента в списке'''
    for elem in lst:
        left = 0
        right = sorted_lst_length - 1
        while left < right:
            middle = (left + right) >> 1
            if sorted_lst[middle] < elem:
                left = middle + 1
            else:
                right = middle
        if left and sorted_lst[left] != elem and abs(sorted_lst[left - 1] - elem) <= abs(sorted_lst[left] - elem):
            print(sorted_lst[left - 1])
        else:
            print(sorted_lst[left])
