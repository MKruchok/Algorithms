from quick_sort import quickSort
import unittest


class TestQuickSort(unittest.TestCase):
    def test_input_array(self):
        arr = [10, 29, 63, 33, 85, 1, 8, 5]
        n = len(arr)
        self.assertEqual(quickSort(arr, 0, n-1), sorted(arr))

    def test_asc_asc(self):
        asc_arr = [i for i in range(100)]
        n = len(asc_arr)
        quickSort(asc_arr, 0, n-1)
        self.assertEqual(quickSort(asc_arr, 0, n-1), sorted(asc_arr))

    def test_asc_desc(self):
        asc_arr = [i for i in range(100)]
        n = len(asc_arr)
        quickSort(asc_arr, 0, n-1, False)
        self.assertEqual(quickSort(asc_arr, 0, n-1, False), sorted(asc_arr, reverse=True))

    def test_desc_desc(self):
        asc_arr = [i for i in range(100, 0, -1)]
        n = len(asc_arr)
        quickSort(asc_arr, 0, n-1, False)
        self.assertEqual(quickSort(asc_arr, 0, n-1, False), sorted(asc_arr, reverse=True))

    def test_desc_asc(self):
        asc_arr = [i for i in range(100, 0, -1)]
        n = len(asc_arr)
        quickSort(asc_arr, 0, n-1)
        self.assertEqual(quickSort(asc_arr, 0, n-1), sorted(asc_arr))


if __name__ == '__main__':
    unittest.main()
