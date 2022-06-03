import datetime
import getopt
import sys
from enum import Enum


class SortOrder(Enum):
    ASC = 1
    DESC = 2


def partition(array, left, right_and_pivot, ascending: bool = True):
    global swaps, comparisons
    pivot_val = array[right_and_pivot]

    for current in range(left, right_and_pivot):
        if array[current] <= pivot_val and ascending or array[current] >= pivot_val and not ascending:
            array[left], array[current] = array[current], array[left]
            left += 1
            swaps += 1
        comparisons += 1

    array[left], array[right_and_pivot] = array[right_and_pivot], array[left]
    return left


def quick_sort(array, left, right, ascending: bool = True):
    if len(array) == 1:
        return array
    if left < right:
        pivot = partition(array, left, right, ascending)

        quick_sort(array, left, pivot - 1, ascending)
        quick_sort(array, pivot + 1, right, ascending)
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
sorted_arr = quick_sort(arr, 0, n - 1, ascending)
execution_time = datetime.datetime.now() - start
print("QuickSort:\n"
      f"Execution time: {execution_time.total_seconds() * 1000} ms\n"
      f"Comparisons: {comparisons}\n"
      f"Swaps: {swaps}\n"
      f"{sorted_arr}")
