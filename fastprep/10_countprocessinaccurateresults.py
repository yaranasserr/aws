import unittest
from bisect import bisect_left, insort

def countInaccurateProcesses(processOrder, executionOrder):
    n = len(processOrder)
    index_map = {process: i for i, process in enumerate(processOrder)}
    execution_indices = [index_map[p] for p in executionOrder]

    remaining = []
    for i in range(n):
        insort(remaining, i)

    inaccurate_count = 0
    for task_index in execution_indices:
        if remaining[0] != task_index:
            inaccurate_count += 1
        del remaining[bisect_left(remaining, task_index)]

    return inaccurate_count


class TestCountSpecialSubstrings(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(countInaccurateProcesses([2, 3, 5, 1, 4], [5, 2, 3, 4, 1]), 2)
        self.assertEqual(countInaccurateProcesses([4, 2, 3, 5, 1, 6], [2, 3, 5, 1, 6, 4]), 5)
        self.assertEqual(countInaccurateProcesses([3, 2, 1], [3, 2, 1]), 0)

if __name__ == "__main__":
    unittest.main()


