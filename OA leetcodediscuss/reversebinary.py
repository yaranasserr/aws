def min_operations_to_reverse(image):
    reversed_image = image[::-1]
    n = len(image)
    max_matched = 0
    i = 0  # pointer for original string
    j = 0  # pointer for reversed string
    
    while i < n and j < n:
        if image[i] == reversed_image[j]:
            j += 1
            max_matched = j
        i += 1
    
    return n - max_matched

# Example usage
image = "0100110"
print(min_operations_to_reverse(image))  # Output should be 3