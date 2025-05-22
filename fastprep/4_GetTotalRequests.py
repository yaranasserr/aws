# Developers at Amazon have their applications deployed on n servers. Initially, the ith server has an id server[i] and can handle server[i] requests at a time.

# For maintenance purposes, some servers are replaced periodically. On a jth day, all the servers with id equal to replaced[j] are replaced with servers with id newId[j] that can serve newId[j] requests. The total number of requests served on a jth day is the sum of the ids of the servers that the application is running on.

# Given server, replaced, and newId, find the total number of requests served by the servers each day.

# Note: The indices i and j are assumed to follow 1-based indexing.

# Function Description

# Complete the function getTotalRequests in the editor.

# getTotalRequests takes the following arguments:

# 1. int server[n]: the initial server ids
# 2. int replaced[n]: the ids of the servers to replace
# 3. int newId[n]: the new ids of the replaced servers
# Returns

# int[]: an array of integers representing the total number of requests served each day

# Example 1:

# Input:  server = [20, 10], replaced = [10, 20], newId = [20, 1]
# Output: [40, 2] 
# Explanation:

      
      

#         Day 1: The servers are [20, 10]. Server with id 10 is replaced by a server with id 20. New servers are [20, 20]. Total requests = 20 + 20 = 40.
      


      

#         Day 2: The servers are [20, 20]. Server with id 20 is replaced by a server with id 1. New servers are [1, 1]. Total requests = 1 + 1 = 2.
      


      

#         Hence the answer is [40, 2].
      


# Example 2:

# Input:  server = [3, 3], replaced = [3, 1], newId = [1, 5]
# Output: [2, 10] 
# Explanation:

# After the first day, the servers are [1, 1].

# After the second day, the servers are [5, 5] :)
# Example 3:

# Input:  server = [2, 5, 2], replaced = [2, 5, 3], newId = [3, 1, 5]
# Output: [11, 7, 11] 
# Explanation:

# After the first day, the servers are [3, 5, 3].)

# After the second day, the servers are [3, 1, 3] :)

# After the third day,the servers are [5, 1, 5] :)

import unittest
from typing import List

class Solution:
    def getTotalRequests(self, server: List[int], replaced: List[int], new_id: List[int]) -> List[int]:
        results = []
        n = len(replaced)
        count_map = {}
        for id in server:
            if id in count_map:
                count_map[id] += 1
            else:
                count_map[id] = 1
        for day in range(n):
            to_replace = replaced[day]
            new_replacement = new_id[day]
            if to_replace in count_map:
                count = count_map[to_replace]
                del count_map[to_replace]
                if new_replacement in count_map:
                    count_map[new_replacement] += count
                else:
                    count_map[new_replacement] = count 
            total_requests = 0
            for id, count in count_map.items():
                total_requests += id * count
            results.append(total_requests)
        return results


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        server = [20, 10]
        replaced = [10, 20]
        new_id = [20, 1]
        expected = [40, 2]
        self.assertEqual(self.solution.getTotalRequests(server, replaced, new_id), expected)

    def test_example2(self):
        server = [3, 3]
        replaced = [3, 1]
        new_id = [1, 5]
        expected = [2, 10]
        self.assertEqual(self.solution.getTotalRequests(server, replaced, new_id), expected)

    def test_example3(self):
        server = [2, 5, 2]
        replaced = [2, 5, 3]
        new_id = [3, 1, 5]
        expected = [11, 7, 11]
        self.assertEqual(self.solution.getTotalRequests(server, replaced, new_id), expected)


if __name__ == "__main__":
    unittest.main()
