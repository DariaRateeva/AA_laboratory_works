import random

def partition(array, low, high):
    pivot_index = random.randint(low, high)
    array[pivot_index], array[high] = array[high], array[pivot_index]

    pivot = array[high]

    # pointer for greater element
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


