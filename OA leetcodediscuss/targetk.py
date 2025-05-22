# https://leetcode.com/discuss/post/6674769/amazon-oa-by-anonymous_user-sxr7/
# Given an array of numbers and a value k. You need to find the maximum count of k the array can have. You can do 1 operation in which you can pick any subarray of the given array and add a number to all the elements in the subarray.

# Initial Array: [1, 2, 3, 4, 5]
# Target Value k: 5

# ans :- 2

# Initial Array: [5, 4, 3, 4, 5]
# Target Value k: 5

# ans :- 4
def max_count_k(arr, k):
    diff = [k - i for i in arr]
    n = len(diff)
    i = 0

    while i < n:
        if diff[i] <= 0:
            i += 1
            continue
 
        while i < n and diff[i] > 0:
            diff[i] -= 1
            i += 1

  
    return sum(1 for d in diff if d == 0)


# Example usage
arr1 = [1, 2, 3, 4, 5]
k1   = 5
result1 = max_count_k(arr1, k1)
print(result1)  # Output: 2             
arr2 = [5, 4, 3, 4, 5]
k2   = 5
result2 = max_count_k(arr2, k2)
print(result2)  # Output: 4
    




