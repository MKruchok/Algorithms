def partition(array, low, high):
    i = (low - 1)
    pivot = array[high]

    for j in range(low, high):

        if order:
            if array[j] <= pivot:

                i = i + 1
                array[i], array[j] = array[j], array[i]
        if not order:
            if array[j] >= pivot:

                i = i + 1
                array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quickSort(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
        pi = partition(array, low, high)

        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


arr = [10, 29, 63, 33, 85, 1, 8, 5]
n = len(arr)
order = False
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for k in range(n):
    print(arr[k])
