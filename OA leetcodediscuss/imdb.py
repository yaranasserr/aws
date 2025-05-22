# https://leetcode.com/discuss/post/6668538/amazon-oa-for-sde-ii-by-anonymous_user-koos/
from collections import defaultdict
def max_increasing_pairs(ratings):
    freq = defaultdict(int)
    for num in ratings:
        freq[num] += 1
    max_freq = max(freq.values())
    return len(ratings) - max_freq
# Example usage
ratings1=[2, 1, 1, 2]
ratings2=[2, 3, 1, 5, 4]
print(max_increasing_pairs(ratings1))  # Output: 2
print(max_increasing_pairs(ratings2))  # Output: 4