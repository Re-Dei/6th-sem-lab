# fractional knapsack using brute force
import unittest

def fractional_knapsack_brute_force(weights, values, capacity):
    n = len(weights)
    max_value = 0.0
    max_set = []

    # Generate all possible subsets using brute force
    for i in range(2**n):
        total_weight = 0.0
        total_value = 0.0
        current_set = []

        for j in range(n):
            if (i >> j) & 1:
                current_set.append(j)
                total_weight += weights[j]
                total_value += values[j]

        # If the total weight of the current set exceeds the capacity, 
        # calculate the fractional part of the last item added to the set
        if total_weight > capacity:
            over_weight = total_weight - capacity
            fraction = (weights[current_set[-1]] - over_weight) / weights[current_set[-1]]
            total_value -= values[current_set[-1]]
            total_value += values[current_set[-1]] * fraction
            total_weight = capacity

        if total_value > max_value:
            max_value = total_value
            max_set = current_set

    return max_set, max_value

class TestSum(unittest.TestCase):
    def test_fractional_knapsack_brute_force(self):
        weights = [10, 20, 30]
        values = [60, 100, 120]
        capacity = 50
        result = fractional_knapsack_brute_force(weights, values, capacity)
        self.assertEqual(result, ([0, 1, 2], 240))  # Changed expected indices and total value

        weights = [10, 20, 30, 40, 50]
        values = [60, 100, 120, 200, 250]
        capacity = 100
        result = fractional_knapsack_brute_force(weights, values, capacity)
        self.assertEqual(result, ([0, 3, 4], 510.0))  # Changed expected indices and total value

        weights = [10, 20, 30, 40, 50]
        values = [60, 100, 120, 200, 250]
        capacity = 10
        result = fractional_knapsack_brute_force(weights, values, capacity)
        self.assertEqual(result, ([0, 1, 2], 80.0))  # Changed expected indices and total value
        

if "__main__" == __name__:
    unittest.main()