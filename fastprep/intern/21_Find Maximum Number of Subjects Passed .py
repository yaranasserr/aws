from typing import List

def findMaximumNum(answered: List[int], needed: List[int], q: int) -> int:
    extra_needed = [max(0, need - ans) for ans, need in zip(answered, needed)]
    extra_needed.sort()
    
    passed = 0
    for extra in extra_needed:
        if q >= extra:
            q -= extra
            passed += 1
        else:
            break
    return passed

# test cases
import unittest

class TestFindMaximumNum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(findMaximumNum([24, 27, 0], [51, 52, 100], 100), 2)
        self.assertEqual(findMaximumNum([24, 27, 0], [51, 52, 100], 200), 3)
        self.assertEqual(findMaximumNum([2, 4], [4, 5], 1), 1)

if __name__ == "__main__":
    unittest.main()
