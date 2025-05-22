# https://leetcode.com/discuss/post/6682902/amazon-oa-problem-2-by-anonymous_user-6wx2/
def max_k_after_one_addition(arr, k):
    n = len(arr)
    original_k = arr.count(k)
    max_k = original_k

    i = 0
    while i < n:
        if arr[i] == k:
            i += 1
            continue

        delta = k - arr[i]  # what we need to add to turn arr[i] into k
        j = i
        new_k_count = 0     # number of values in this window that can become k with +delta

        # expand the window while the delta is consistent
        while j < n and (arr[j] == k or k - arr[j] == delta):
            if arr[j] != k:
                new_k_count += 1
            j += 1

        # count how many original Ks are inside this window (they'd be overwritten)
        overwritten_k = 0
        for x in range(i, j):
            if arr[x] == k:
                overwritten_k += 1

        # total k's after applying the addition: old k's outside + new k's in window
        total_k = original_k - overwritten_k + new_k_count
        max_k = max(max_k, total_k)

        i = j  # move to next segment

    return max_k


arr = [4,4,6,4,4,4,6,4,4,4,4,6,4]
k = 6
print(max_k_after_one_addition(arr, k))  # Output: 10
