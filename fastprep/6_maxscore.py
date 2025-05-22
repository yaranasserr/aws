class Solution:
    def count_valid_substrings(self, s: str) -> int:
        count = 0
        current = 1
        for i in range(1, len(s)):
            if abs(ord(s[i]) - ord(s[i - 1])) <= 1:
                current += 1
                count += current - 1
            else:
                current = 1
        return count

    def findMaximumScore(self, data: str) -> int:
        n = len(data)
        if n == 0:
            return 0

        base_score = n
        original_substrings = self.count_valid_substrings(data)
        max_substrings = original_substrings

        for i in range(n):
            original_char = data[i]
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c == original_char:
                    continue
                modified = data[:i] + c + data[i + 1:]
                new_substrings = self.count_valid_substrings(modified)
                if new_substrings > max_substrings:
                    max_substrings = new_substrings

        return base_score + max_substrings
import unittest

class TestSolutionSamples(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sample_case_abcb(self):
        data = "abcb"
        expected = 10
        self.assertEqual(self.solution.findMaximumScore(data), expected)

    def test_sample_case_aabacfgh(self):
        data = "aabacfgh"
        expected = 21
        self.assertEqual(self.solution.findMaximumScore(data), expected)

    def test_sample_case_abez(self):
        data = "abez"
        expected = 7
        self.assertEqual(self.solution.findMaximumScore(data), expected)

if __name__ == "__main__":
    unittest.main()
