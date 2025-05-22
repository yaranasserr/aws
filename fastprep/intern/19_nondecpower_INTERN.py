from typing import List
def makePowerNonDescreasing(powa: List[int]) -> int:
    n = len(powa)
    if n == 1 :
      return 0 
    ans = 0 

    for i in range(1,n):
      if powa[i]<powa[i-1]:
        diff  = powa[i-1] - powa[i]
        j = i 
        while j < n and powa[j] <powa[i-1]:
          j+=1
        for k in range(i,j):
          powa[k]+= diff 
        ans += diff 
    return ans 
# test cases 
import unittest

class TestCountSpecialSubstrings(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(makePowerNonDescreasing([3, 4, 1, 6, 2]), 7)
        self.assertEqual(makePowerNonDescreasing([3,2, 1]), 2)
        self.assertEqual(makePowerNonDescreasing([3, 5, 2, 3]), 3)

if __name__ == "__main__":
    unittest.main()

        

       