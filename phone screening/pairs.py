def find_pairs_with_sum_hashing(arr, x):
    seen = {}  # Dictionary to store the count of elements
    result = []

    for num in arr:
        complement = x - num
        # Check if the complement exists in seen
        if complement in seen and seen[complement] > 0:
            result.append((num, complement))
            seen[complement] -= 1  # Decrease count for the complement
        else:
            # Add the current number to seen
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

    return result

# Example usage
arr = [2, 2, 4, 4]
x = 6
print(find_pairs_with_sum_hashing(arr, x))  # Output: [(2, 4), (2, 4)]
