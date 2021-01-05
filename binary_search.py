def binary_search(array, number):
    high = len(array) - 1
    low = 0
    while high >= low:

        mid = (high + low) // 2
        if array[mid] == number:
            return number
        if array[mid] < number:
            low = mid + 1
        else:
            high = mid - 1

    return None


