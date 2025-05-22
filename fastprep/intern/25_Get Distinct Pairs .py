import unittest


def getDistinctPairs(stocksProfit, target):
    seen = set()
    pairs = set()

    for n in stocksProfit:
        diff = target - n
        if diff in seen:
            pairs.add(tuple(sorted((n, diff))))
        seen.add(n)

    return len(pairs)


class TestFindMaximumNum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(getDistinctPairs([5, 7, 9, 13, 11, 6, 6, 3, 3], 12), 3)
  
if __name__ == "__main__":
    unittest.main()