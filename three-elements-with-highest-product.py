def three_elements_with_highest_product(lst):
    '''this function finds three elements with highest product'''
    if len(lst) < 3:
        return
    highest = max(lst[0], lst[1])
    lowest = min(lst[0], lst[1])
    highest_product_of_2 = lst[0] * lst[1]
    highest_product_of_2_element1 = lst[0]
    highest_product_of_2_element2 = lst[1]
    lowest_product_of_2  = lst[0] * lst[1]
    lowest_product_of_2_element1 = lst[0]
    lowest_product_of_2_element2 = lst[1]
    highest_product_of_3 = lst[0] * lst[1] * lst[2]
    highest_product_of_3_element1 = lst[0]
    highest_product_of_3_element2 = lst[1]
    highest_product_of_3_element3 = lst[2]
    for i in range(2, len(lst)):
        if lst[i] * highest_product_of_2 > highest_product_of_3:
            highest_product_of_3 = lst[i] * highest_product_of_2
            highest_product_of_3_element1 = highest_product_of_2_element1
            highest_product_of_3_element2 = highest_product_of_2_element2
            highest_product_of_3_element3 = lst[i]
        if lst[i] * lowest_product_of_2 > highest_product_of_3:
            highest_product_of_3 = lst[i] * lowest_product_of_2
            highest_product_of_3_element1 = lowest_product_of_2_element1
            highest_product_of_3_element2 = lowest_product_of_2_element2
            highest_product_of_3_element3 = lst[i]
        if lst[i] * highest > highest_product_of_2:
            highest_product_of_2 = lst[i] * highest
            highest_product_of_2_element1 = highest
            highest_product_of_2_element2 = lst[i]
        if lst[i] * lowest > highest_product_of_2:
            highest_product_of_2 = lst[i] * lowest
            highest_product_of_2_element1 = lowest
            highest_product_of_2_element2 = lst[i]
        if lst[i] * highest < lowest_product_of_2:
            lowest_product_of_2 = lst[i] * highest
            lowest_product_of_2_element1 = highest
            lowest_product_of_2_element2 = lst[i]
        if lst[i] * lowest < lowest_product_of_2:
            lowest_product_of_2 = lst[i] * lowest
            lowest_product_of_2_element1 = lowest
            lowest_product_of_2_element2 = lst[i]
        if lst[i] > highest:
            highest = lst[i]
        if lst[i] < lowest:
            lowest = lst[i]
    return highest_product_of_3_element1, highest_product_of_3_element2, highest_product_of_3_element3
