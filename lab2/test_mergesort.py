import unittest
from mergesort import mergesort
class TestSum(unittest.TestCase):
    def test_selectionsort(self):
        input_data = [4, 3, 2, 1]
        result = mergesort(input_data)
        self.assertEqual(result, [1, 2, 3, 4])

        input_data = []
        result = mergesort(input_data)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()