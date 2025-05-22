class Solution:
    def optimizeIdentifiers(self, s: str) -> int:
        answer = 0
        left, right = 0, 0
        n = len(s)

        if s[0] == s[-1]:
            return n - 1
  
        for index, char in enumerate(s):
            if char == s[0]:
                left = index

            if char == s[-1]:
                right = index

            if right > left:
                answer = max(answer, n -  (right - left + 1))

        return answer

solution = Solution()
param1 = 'babdcaac'
print(f'input = {param1} -> ', solution.optimizeIdentifiers(param1))

param1 = 'hchc'
print(f'input = {param1} -> ', solution.optimizeIdentifiers(param1))

param1 = 'abc'
print(f'input = {param1} -> ', solution.optimizeIdentifiers(param1))

param1 = 'aba'
print(f'input = {param1} -> ', solution.optimizeIdentifiers(param1))
"""
Whenever the right pointer moves to a position greater than left, meaning a valid
substring is found where the first and last characters match, the algorithm calculates
the number of operations that can be performed.
This is done using the formula n - (right - left + 1), which gives the number of operations based 
on the substring from left to right. The idea is to consider the substring from left to right and calculate
how many characters can be removed without changing the type.
"""

# left: Tracks the last index of the character matching s[0] (first character).
# right: Tracks the last index of the character matching s[-1] (last character).