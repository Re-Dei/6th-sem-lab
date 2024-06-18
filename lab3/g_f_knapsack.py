import unittest


def knapsack_greedy(weights, values, capacity):
    n = len(weights)
    value_per_weight = [values[i] / weights[i] for i in range(n)]
    sorted_indices = sorted(range(n), key=lambda x: value_per_weight[x], reverse=True)
    total_weight = 0
    total_value = 0
    set = []
    for i in sorted_indices:
        if total_weight + weights[i] <= capacity:
            set.append(i)
            total_weight += weights[i]
            total_value += values[i]
    return set, total_value


class TestSum(unittest.TestCase):
    def test_knapsack_greedy(self):
        weights = [10, 20, 30]

        values = [60, 100, 120]
        capacity = 50
        result = knapsack_greedy(weights, values, capacity)
        self.assertEqual(result, ([0, 1], 160))

        weights = [10, 20, 30, 40, 50]
        values = [60, 100, 120, 200, 250]
        capacity = 100
        result = knapsack_greedy(weights, values, capacity)
        self.assertEqual(result, ([0, 1, 3, 2], 480))

        weights = [10, 20, 30, 40, 50]
        values = [60, 100, 120, 200, 250]
        capacity = 10
        result = knapsack_greedy(weights, values, capacity)
        self.assertEqual(result, ([0], 60))

        weights = [10, 20, 30, 40, 50]
        values = [60, 100, 120, 200, 250]
        capacity = 0
        result = knapsack_greedy(weights, values, capacity)
        self.assertEqual(result, ([], 0))


if __name__ == "__main__":
    unittest.main()
