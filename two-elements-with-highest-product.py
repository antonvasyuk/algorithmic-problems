def two_elements_with_highest_product(lst):
    ''' возвращает два элемента с максимальным произведением '''
    if len(lst) < 2:
        return
    highest = max(lst[0], lst[1])
    lowest = min(lst[0], lst[1])
    highest_product_of_2 = lst[0] * lst[1]
    highest_product_of_2_element1 = lst[0]
    highest_product_of_2_element2 = lst[1]
    for i in range(2, len(lst)):
        if lst[i] * highest > highest_product_of_2:
            highest_product_of_2 = lst[i] * highest
            highest_product_of_2_element1 = highest
            highest_product_of_2_element2 = lst[i]
        if lst[i] * lowest > highest_product_of_2:
            highest_product_of_2 = lst[i] * lowest
            highest_product_of_2_element1 = lowest
            highest_product_of_2_element2 = lst[i]
        if lst[i] > highest:
            highest = lst[i]
        if lst[i] < lowest:
            lowest = lst[i]
    highest_product_of_2_element1 = min(highest_product_of_2_element1, highest_product_of_2_element2)
    highest_product_of_2_element2 = max(highest_product_of_2_element1, highest_product_of_2_element2)
    return highest_product_of_2_element1, highest_product_of_2_element2
