# An online marketplace has onboarded n merchants, each operating within a designated geographical range. The operating zone of merchant i is defined by the interval spanning from zoneStart[i] to zoneEnd[i].

# A set of k merchants is termed cohesive (inclusive) if there exists at least one merchant whose operational territory overlaps with (or touches) all the other (k-1) merchants’ operational zones.

# The marketplace plans to relocate some merchants to new areas. Your goal is to determine the minimum number of merchants that need to be moved so that the remaining merchants form a cohesive subset.

# Function Description

# Complete the predefined function in the editor.

# minimumRetailers has the following parameters:

# int zoneStart[n]: the left ends of the operating regions
# int zoneEnd[n]: the right ends of the operating regions
# Returns

# int: the smallest number of merchants that need to be relocated

# Constraints

# 1 ≤ n ≤ 10^5
# 1 ≤ zoneStart[i] ≤ zoneEnd[i] ≤ 10^9 (1 <= i < n)
# All regions have regions with the same start and end points.
# Example 1:

# Input:  zoneStart = [1, 3, 4, 6, 9], zoneEnd = [2, 8, 5, 7, 10]
# Output: 2 
# Explanation:
# Example 2:

# Input:  zoneStart = [1, 2, 3, 4], zoneEnd = [2, 3, 5, 5]
# Output: 1 
# Explanation:

# Region 1 (1, 2) intersects only region 2. (move regions 3 and 4)

# Region 2 (2, 3) intersects regions 1 and 3. (move region 4)

# Region 3 (3, 5) intersects regions 2 and 4. (move region 1)

# Region 4 (4, 5) intersects region 3. (move regions 1 and 2)

# The minimum number of moves is 1, moving region 1 or 4
      
# Example 3:

# Input:  zoneStart = [1, 2, 4], zoneEnd = [7, 5, 6]
# Output: 0 
# Explanation:

# Will update once find reliable resources. As always.
def minimumRetailers(zoneStart, zoneEnd):
    n = len(zoneStart)
    maxOverlap = 0

    for i in range(n):
        groupCount = 1
        a1 = zoneStart[i]
        a2 = zoneEnd[i]

        for j in range(n):
            if i == j:
                continue

            b1 = zoneStart[j]
            b2 = zoneEnd[j]

            # Check overlap: not (a2 < b1 or b2 < a1)
            if not (a2 < b1 or b2 < a1):
                groupCount += 1

        maxOverlap = max(maxOverlap, groupCount)

    return n - maxOverlap


# Unit tests
import unittest

class TestMinimumRetailers(unittest.TestCase):
    def test_example1(self):
        zoneStart = [1, 3, 4, 6, 9]
        zoneEnd = [2, 8, 5, 7, 10]
        self.assertEqual(minimumRetailers(zoneStart, zoneEnd), 2)

    def test_example2(self):
        zoneStart = [1, 2, 3, 4]
        zoneEnd = [2, 3, 5, 5]
        self.assertEqual(minimumRetailers(zoneStart, zoneEnd), 1)

    def test_example3(self):
        zoneStart = [1, 2, 4]
        zoneEnd = [7, 5, 6]
        self.assertEqual(minimumRetailers(zoneStart, zoneEnd), 0)

  
if __name__ == "__main__":
    unittest.main()
      