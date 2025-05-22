# https://leetcode.com/discuss/post/4749861/amazon-oa-by-anonymous_user-1yoe/

def countDistinctPasswords(password: str) -> int:
    from collections import Counter

    n = len(password)
    total_pairs = n * (n - 1) // 2

    # Count characters
    freq = Counter(password)
    
    # Count number of same character pairs
    same_pairs = sum(f * (f - 1) // 2 for f in freq.values())
    
    # Distinct reversals = total pairs with different characters
    distinct_reversals = total_pairs - same_pairs
    
    # Add the original string
    return 1 + distinct_reversals

# Test case
print(countDistinctPasswords("abaa"))  # Output should be 4
print(countDistinctPasswords("abc"))   # Output should be 