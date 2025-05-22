# https://leetcode.com/discuss/post/6679050/amazon-online-assessment-by-anonymous_us-dyun/
# Data analysts at Amazon are analyzing a string, data. Each of its characters is worth 1 point.
#  Any substring in which all characters are adjacent to characters within one position in the English alphabet is also worth 1 point.
#  For example, "aa", "ab", and "ba" are each worth 1 point.

# To improve the score, at most one character can be replaced with any other character from the lowercase English alphabet.

# Given a string, data, find the maximum score that can be achieved.

# Example
# Given data = "abez"

# "abez" to "abaz"

# Each of the substrings is worth 1 point. Hence, the final answer is 7.
def max_score(data):
    n = len(data)
    
    if n == 1:
        return 1  # only 1 character

    # Step 1: Build prefix array
    prefix = [1] * n
    for i in range(1, n):
        if abs(ord(data[i]) - ord(data[i - 1])) <= 1:
            prefix[i] = prefix[i - 1] + 1

    # Step 2: Build suffix array
    suffix = [1] * n
    for i in range(n - 2, -1, -1):
        if abs(ord(data[i + 1]) - ord(data[i])) <= 1:
            suffix[i] = suffix[i + 1] + 1

    # Step 3: Try replacing each character and compute max valid length
    max_len = 1  # minimum valid substring length
    for i in range(n):
        left = prefix[i - 1] if i > 0 else 0
        right = suffix[i + 1] if i < n - 1 else 0

        if i > 0 and i < n - 1 and abs(ord(data[i - 1]) - ord(data[i + 1])) == 2:
            max_len = max(max_len, left + 1 + right)
        else:
            max_len = max(max_len, max(left, right) + 1)

    # Step 4: Compute total score
    return n + (max_len * (max_len - 1)) // 2

    

#example 
data = "abez"
print(max_score(data))  # Output: 7