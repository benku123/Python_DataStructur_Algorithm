def selection_sort(array):
    for main_index in range(len(array)):
        min_number = main_index
        for inner in range(main_index + 1, len(array)):
            if array[min_number] > array[inner]:
                min_number = inner

        array[main_index], array[min_number] = array[min_number], array[main_index]

    return array


def selectionSort(array):
    """We create sorting algorithm by add element to a new list"""
    new_array = []

    for i in range(len(array)):
        new_array.append(min(array))
        array.remove(min(array))

    return new_array


print(selectionSort([0, 2, 1, 6, 8, 3]))
