# You are given a DNA sequence string genome, consisting of lowercase Latin letters.

# A substring of genome is considered special if it satisfies one of the following conditions:

# The length of the substring is exactly 2 and both characters are the same. Example: "aa", "bb"
# The length of the substring is greater than 2, the first and last characters are the same, and the substring in between (from index 1 to n-2) contains exactly one distinct character. Example: "xyyx" -> 'x' == 'x' and the middle "yy" has only one distinct character.
# Function Signature

# def countSpecialSubstrings(genome: str) -> int:

# Input

# • A single string genome of length n where:

# 1 ≤ n ≤ 3 * 10^5
# genome contains only lowercase letters ('a' to 'z')
# Output

# • Return the total count of special substrings in the given genome string.

# Example 1:

# Input:  genome = "aabbaa"
# Output: 4 
# Explanation:

# Special substrings: "aa", "bb", "abba", "abba"
# Total: 4
      
# Example 2:

# Input:  genome = "pq"
# Output: 0 
# Explanation:

# No special substrings are present.
      
# Example 3:

# Input:  genome = "xyyx"
# Output: 2 
# Explanation:

# Special substrings: "yy" (Type 1), "xyyx" (Type 2)
def countSpecialSubstrings(genome: str) -> int:
    n = len(genome)
    result = 0

    for i in range(n - 1):
        if genome[i] == genome[i + 1]:
            result += 1

    for l in range(n):
        for r in range(l + 2, min(l + 100, n)):
            if genome[l] == genome[r]:
                middle = genome[l + 1:r]
                if len(set(middle)) == 1:
                    result += 1

    return result





import unittest
class TestCountSpecialSubstrings(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(countSpecialSubstrings("aabbaa"), 4)
        self.assertEqual(countSpecialSubstrings("pq"), 0)
        self.assertEqual(countSpecialSubstrings("xyyx"), 2)
 

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
