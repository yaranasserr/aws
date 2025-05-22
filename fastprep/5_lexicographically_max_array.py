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
