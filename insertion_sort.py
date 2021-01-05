def insertion_sort(array):
    index = 1
    while index != len(array):
        switched_index = index - 1
        index_comparison = index
        while array[switched_index] > array[index_comparison] and switched_index >= 0:
            array[switched_index], array[index_comparison] = array[index_comparison], array[switched_index]
            index_comparison -= 1
            switched_index -= 1
        index += 1
    return array
