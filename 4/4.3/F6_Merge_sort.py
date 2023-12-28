def merge_sort(array):

    if len(array) == 1:
        return array

    array = list(array)
    length = len(array) // 2
    sort_array = []
    index1, index2 = 0, 0

    first_half, second_half = merge_sort(array[:length]), merge_sort(array[length:])

    while index1 < len(first_half) and index2 < len(second_half):
        if first_half[index1] < second_half[index2]:
            sort_array.append(first_half[index1])
            index1 += 1
        else:
            sort_array.append(second_half[index2])
            index2 += 1

    for i in range(index1, len(first_half)):
        sort_array.append(first_half[i])

    for i in range(index2, len(second_half)):
        sort_array.append(second_half[i])

    return sort_array


result = merge_sort([3, 1, 5, 3])
print(result)