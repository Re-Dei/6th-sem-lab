import unittest
from sum import sum
class TestSum(unittest.TestCase):
    def test_sum(self):
        input_data = [4, 3, 2, 1]
        result = sum(input_data)
        self.assertEqual(result, 10)

        input_data = []
        result = sum(input_data)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()