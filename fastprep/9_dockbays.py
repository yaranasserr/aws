import heapq
from typing import List

class Solution:
    def getMinimumDockBays(self, truckCargoSize: List[int], maxTurnaroundTime: int) -> int:
        l, r = 1, len(truckCargoSize)
        minD = r
        while l <= r:
            d = l + (r - l) // 2
            time = 0
            pq = [time] * d
            heapq.heapify(pq)
            for size in truckCargoSize:
                cur = heapq.heappop(pq) + size
                time = max(time, cur)
                heapq.heappush(pq, cur)

            if time > maxTurnaroundTime:
                l = d + 1
            else:
                r = d - 1
                minD = min(minD, d)
        return minD

# test cases
import unittest

class TestMinimumDockBays(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(Solution().getMinimumDockBays([3, 4, 3, 2, 3], 8), 3)
        self.assertEqual(Solution().getMinimumDockBays([2, 3, 1], 7), 1)

if __name__ == '__main__':
    unittest.main()
