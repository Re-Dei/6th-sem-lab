def knapsack_memoization(weights, values, capacity):
    n = len(weights)
    memo = [[-1 for j in range(capacity + 1)] for i in range(n)]
    def knapsack_recursive(i, capacity):
        if i == n:
            return 0
        if memo[i][capacity] != -1:
            return memo[i][capacity]
        if weights[i] > capacity:
            memo[i][capacity] = knapsack_recursive(i + 1, capacity)
        else:
            memo[i][capacity] = max(knapsack_recursive(i + 1, capacity), values[i] + knapsack_recursive(i + 1, capacity - weights[i]))
        return memo[i][capacity]
    return knapsack_recursive(0, capacity)
  
import unittest

class TestSum(unittest.TestCase):
    def test_knapsack_memoization(self):
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 50
        result = knapsack_memoization(weights, values, capacity)
        self.assertEqual(result, 220)

        weights = [10, 20, 30, 40, 50]
        values = [60, 100, 120, 200, 250]
        capacity = 100
        result = knapsack_memoization(weights, values, capacity)
        self.assertEqual(result, 510)

        weights = [10, 20, 30, 40, 50]
        values = [60, 100, 120, 200, 250]
        capacity = 10
        result = knapsack_memoization(weights, values, capacity)
        self.assertEqual(result, 60)

        weights = [10, 20, 30, 40, 50]
        values = [60, 100, 120, 200, 250]
        capacity = 0
        result = knapsack_memoization(weights, values, capacity)
        self.assertEqual(result, 0)
        
if __name__ == '__main__':
    unittest.main()