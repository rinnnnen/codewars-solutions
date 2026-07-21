def multiple_of_index(arr):
    list_div = []
    for index, num in enumerate(arr):
        if (index == 0 and num == 0) or (index != 0 and num % index == 0):
            list_div.append(num)
    return list_div
