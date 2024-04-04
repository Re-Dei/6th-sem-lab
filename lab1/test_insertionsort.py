import unittest
from insertionsort import insertionsort
class TestSum(unittest.TestCase):
    def test_insertionsort(self):
        input_data = [4, 3, 2, 1]
        result = insertionsort(input_data)
        self.assertEqual(result, [1, 2, 3, 4])

        input_data = []
        result = insertionsort(input_data)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()