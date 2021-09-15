import datetime
import getopt
import sys
from enum import Enum


class SortOrder(Enum):
    ASC = 1
    DESC = 2


def partition(array, low, high, ascending: bool = True):
    global swaps, comparisons
    i = (low - 1)
    pivot = array[high]

    for j in range(low, high):
        comparisons += 1
        if array[j] <= pivot and ascending or array[j] >= pivot and not ascending:
            i = i + 1
            swaps += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quickSort(array, low, high, ascending: bool = True):
    if len(array) == 1:
        return array
    if low < high:
        pi = partition(array, low, high, ascending)

        quickSort(array, low, pi - 1, ascending)
        quickSort(array, pi + 1, high, ascending)
    return array


def main(argv):
    _arr, _ascending = [], True
    opts, args = getopt.getopt(argv, "ha:o:", ["array=", "order="])
    for opt, arg in opts:
        if opt in ("-a", "--array"):
            _arr = [int(i) for i in arg.split(',') if i]
        if opt in ("-o", "--order"):
            if arg in ('asc', 'desc'):
                if arg == 'asc':
                    _ascending = True
                else:
                    _ascending = False
    return _arr, _ascending


comparisons = 0
swaps = 0
arr, ascending = main(sys.argv[1:])
n = len(arr)
start = datetime.datetime.now()
sorted_arr = quickSort(arr, 0, n - 1, ascending)
execution_time = datetime.datetime.now() - start
print("QuickSort:\n"
      f"Execution time: {execution_time.total_seconds() * 1000} ms\n"
      f"Comparisons: {comparisons}\n"
      f"Swaps: {swaps}\n"
      f"{sorted_arr}")
