# https://leetcode.com/discuss/post/6679275/amazon-oa-questions-asked-by-anonymous_u-nx6w/
def getMinimumAlterations(server_health):
    s = server_health
    n = len(s)
    if n == 0:
        return 0
    
    # Count total '0's and '1's
    total0 = s.count('0')
    total1 = n - total0
    
    # Case 1: all '0's
    flips_all0 = total1
    
    # Case 2: all '1's
    flips_all1 = total0
    
    # Case 3: "00...011...1"
    # Precompute prefix counts of '1's and suffix counts of '0's
    prefix1 = [0] * (n + 1)
    suffix0 = [0] * (n + 1)
    
    for i in range(1, n + 1):
        prefix1[i] = prefix1[i - 1] + (1 if s[i - 1] == '1' else 0)
    
    for i in range(n - 1, -1, -1):
        suffix0[i] = suffix0[i + 1] + (1 if s[i] == '0' else 0)
    
    min_flips_case3 = float('inf')
    for i in range(0, n + 1):
        flips = prefix1[i] + suffix0[i]
        if flips < min_flips_case3:
            min_flips_case3 = flips

    prefix0 = [0] * (n + 1)
    suffix1 = [0] * (n + 1)
    
    for i in range(1, n + 1):
        prefix0[i] = prefix0[i - 1] + (1 if s[i - 1] == '0' else 0)
    
    for i in range(n - 1, -1, -1):
        suffix1[i] = suffix1[i + 1] + (1 if s[i] == '1' else 0)
    
    min_flips_case4 = float('inf')
    for i in range(0, n + 1):
        flips = prefix0[i] + suffix1[i]
        if flips < min_flips_case4:
            min_flips_case4 = flips
    
    # The answer is the minimum among all four cases
    return min(flips_all0, flips_all1, min_flips_case3, min_flips_case4)



print(getMinimumAlterations("1011010"))  # Output: 2