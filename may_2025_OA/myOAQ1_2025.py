
# https://leetcode.com/discuss/post/6683555/amazon-sde1-oa-very-hard-by-anonymous_us-upta/
'''
Amazon's fulfillment centers handle packages of various weights, and they need to optimize their sorting process.

Given an array weight which denotes the weights of n packages, the goal is to create the lexicographically maximal
 resulting array sorted by non-increasing order of weight using the following operations:

Discard the first package from the current weight array

Add the first element to the resulting array, then remove it along with the next k (a fixed constant) elements from the current array

Note that Operation 2 can also be applied when fewer than k elements remain after the current element; In that case, the entire remaining array is removed.

The resulting array must have packages arranged in non-Increasing weight order.

Given an array weight of size n and an integer k, find the lexicographically maximal resulting array sorted by non-Increasing order of weight that can be obtained.

Note: An array x is lexicographically greater than an array y If:

x[i] >y[i], where i is the first position where x and y differ, or

/x/ > /y/ and y is a prefix of x (where /x/ denotes the size of array x)

'''

# def lexicographically_max_array(weight, k):
#     result = []
#     i = 0
#     n = len(weight)

#     while i < n:
#         # Determine the max element in the window i to i + k
#         # we must pick one of them
#         max_index = i
#         max_val = weight[i]
#         for j in range(i + 1, min(i + k + 1, n)):
#             if weight[j] > max_val:
#                 max_val = weight[j]
#                 max_index = j
        
#         # Add the best candidate to result
#         result.append(weight[max_index])

#         # Skip over selected element and next k elements
#         i = max_index + k + 1

#     return result
# def dfs(weight, k, result):
#     if not weight:
#         return result
    
#     best = dfs(weight[1:], k, result)  # Option 1: Discard first
    
#     # Option 2: Pick first, only if result is still non-increasing
#     if not result or weight[0] <= result[-1]:
#         new_result = result + [weight[0]]
#         remaining = weight[k+1:] if len(weight) > k else []
#         pick_result = dfs(remaining, k, new_result)
        
#         # Compare lexicographically
#         if pick_result > best:
#             best = pick_result
    
#     return best

# def lexicographically_max_array(weight, k):
#     return dfs(weight, k, [])
def lexicographically_max_array(weight, k):
    n = len(weight)
    result = []
    i = 0
    
    while i < n:
        max_idx = i
        for j in range(i + 1, min(i + k + 1, n)):
            if weight[j] > weight[max_idx]:
                max_idx = j
                
        if max_idx != i:
            i += 1
            continue
        
        result.append(weight[i])
        i += k + 1
    
    return result

# Test case 1
k = 2
weight = [10, 5, 9, 2, 5]
print(lexicographically_max_array(weight, k))  # Output: [10, 5]

# Test case 2
k = 0
weight = [3]
print(lexicographically_max_array(weight, k))  # Output: [3]
