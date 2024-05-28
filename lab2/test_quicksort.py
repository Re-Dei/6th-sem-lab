import unittest
from quicksort import quicksort
class TestSum(unittest.TestCase):
    def test_selectionsort(self):
        input_data = [4, 3, 2, 1]
        quicksort(input_data, 0, len(input_data) - 1)
        self.assertEqual(input_data, [1, 2, 3, 4])

        input_data = []
        quicksort(input_data, 0, len(input_data) - 1)
        self.assertEqual(input_data, [])

if __name__ == '__main__':
    unittest.main()