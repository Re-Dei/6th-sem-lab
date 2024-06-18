import unittest

def knapsack_brute_force(weights, values, capacity):
    n = len(weights)
    max_value = 0
    max_set = []
    for i in range(2**n):
        set = []
        total_weight = 0
        total_value = 0
        for j in range(n):
            if (i >> j) & 1:
                set.append(j)
                total_weight += weights[j]
                total_value += values[j]
        if total_weight <= capacity and total_value > max_value:
            max_value = total_value
            max_set = set
    return max_set, max_value
  
class TestSum(unittest.TestCase):
    def test_knapsack_brute_force(self):
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 50
        result = knapsack_brute_force(weights, values, capacity)
        self.assertEqual(result, ([1, 2], 220))

        weights = [10, 20, 30, 40, 50]
        values = [60, 100, 120, 200, 250]
        capacity = 100
        result = knapsack_brute_force(weights, values, capacity)
        self.assertEqual(result, ([0, 3, 4], 510))

        weights = [10, 20, 30, 40, 50]
        values = [60, 100, 120, 200, 250]
        capacity = 10
        result = knapsack_brute_force(weights, values, capacity)
        self.assertEqual(result, ([0], 60))

        weights = [10, 20, 30, 40, 50]
        values = [60, 100, 120, 200, 250]
        capacity = 0
        result = knapsack_brute_force(weights, values, capacity)
        self.assertEqual(result, ([], 0))
      
      
if __name__ == '__main__':
    unittest.main()