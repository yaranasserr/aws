def maxpoints(memory):
    # sort in desc 
    memory.sort(reverse=True)
    res = [0] * len(memory)
    res[0] = memory[0]
    for i in range(1, len(memory)):
        res[i] = memory[i] + res[i - 1]
    
    return sum(res)
   


  




import unittest
class TestMaxPoints(unittest.TestCase):
    def test_case_1(self):
        memory = [3, 4, 5]
        expected = 26
        result = maxpoints(memory)
        self.assertEqual(result, expected)
    def test_case_2(self):
        memory = [1, 2, 3]
        expected = 14
        result = maxpoints(memory)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

"""
The cumulative values are [1, 1 + 2, 1 + 2 + 3], which gives 1 + 3 + 6 = 10.

The best arrangement is [3, 2, 1]:

Step 1: 3 (cumulative sum = 3)
res[0] = nums[0]
Step 2: 3 + 2 = 5 (cumulative sum = 8)
for i in range(1, n):
    res[i] = nums[i] + res[i - 1]


Step 3: 3 + 2 + 1 = 6 (cumulative sum = 14)

Total sum: 3 + 5 + 6 = 14 :)

"""