import unittest
from selectionsort import selectionsort
class TestSum(unittest.TestCase):
    def test_selectionsort(self):
        input_data = [4, 3, 2, 1]
        result = selectionsort(input_data)
        self.assertEqual(result, [1, 2, 3, 4])

        input_data = []
        result = selectionsort(input_data)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()