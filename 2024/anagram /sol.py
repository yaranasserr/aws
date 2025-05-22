def is_special_anagram(dna1, dna2):
    def get_frequency(word):
        freq = {}
        for char in word:
            freq[char] = freq.get(char, 0) + 1
        return freq

    # Calculate frequencies of both strings
    freq1 = get_frequency(dna1)
    freq2 = get_frequency(dna2)

    # Find common keys, keys exclusive to each string
    common_keys = set(freq1.keys()).intersection(freq2.keys())
    diff_keys1 = set(freq1.keys()).difference(freq2.keys())
    diff_keys2 = set(freq2.keys()).difference(freq1.keys())

    # If there are more than one unique keys in either string, it's not special
    if len(diff_keys1) > 1 or len(diff_keys2) > 1:
        return False

    # Remove mismatched keys from frequency dictionaries
    for key in diff_keys1:
        del freq1[key]
    for key in diff_keys2:
        del freq2[key]

    # Check the remaining frequencies
    for key in common_keys:
        if abs(freq1[key] - freq2[key]) > 1:
            return False

    return True


# Example usage
def process_pairs(pairs):
    results = []
    for dna1, dna2 in pairs:
        results.append(is_special_anagram(dna1, dna2))
    return results


# Sample Input
n = 2
pairs = [("abcee", "acdeedb"), ("sljffsaje", "sljsje")]

# Output
print(process_pairs(pairs))  # Expected Output: [True, False]
# from collections import Counter

# def getSequence(dna_pairs):
#     result = []
    
#     for dna1, dna2 in dna_pairs:
#         count1 = Counter(dna1)
#         count2 = Counter(dna2)
        
#         surplus1 = {}
#         surplus2 = {}
        
#         # Calculate surplus for DNA1
#         for char in count1:
#             if count1[char] > count2.get(char, 0):
#                 surplus1[char] = count1[char] - count2.get(char, 0)
        
#         # Calculate surplus for DNA2
#         for char in count2:
#             if count2[char] > count1.get(char, 0):
#                 surplus2[char] = count2[char] - count1.get(char, 0)
        
#         # Check surplus constraints
#         if len(surplus1) <= 1 and len(surplus2) <= 1:
#             result.append(True)
#         else:
#             result.append(False)
    
#     return result

# # Example usage
# dna_pairs = [
#     ("abcee", "acdeedb"),
#     ("sljffsaje", "sljsje")
# ]

# print(getSequence(dna_pairs))  # Output: [True, False]
""""if count1[char] > count2.get(char, 0):

For each character char in count1, this condition checks whether its count in count1 (count1[char]) is greater than its count in count2.
count2.get(char, 0) retrieves the count of char in count2. If char is not present in count2, get returns the default value of 0.
This comparison identifies characters in dna1 that appear more frequently than in dna2.
surplus1[char] = count1[char] - count2.get(char, 0)

If the character char appears more times in dna1 than in dna2, this line calculates the surplus count of that character and stores it in the surplus1 dictionary.
surplus1 keeps track of all characters from dna1 that have extra occurrences compared to dna2.
"""