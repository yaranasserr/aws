import unittest
from collections import Counter

def computeEncodedProductName(nameString):
    """
    Rearranges the characters of a palindromic string to form the lexicographically smallest possible palindrome.

    Parameters:
    nameString (str): The input palindromic string.

    Returns:
    str: The lexicographically smallest palindromic rearrangement of the input string.
    """
    freq = Counter(nameString)
    
    # Sort characters in alphabetical order
    sorted_chars = sorted(freq.keys())
    
    first_half = []
    middle = ''
    
    for char in sorted_chars:
        count = freq[char]
        half = count // 2
        first_half.append(char * half)
        freq[char] -= half * 2  # Remaining is either 0 or 1
    
    # Find the smallest character with odd count for the middle
    for char in sorted_chars:
        if freq[char] == 1:
            middle = char
            break
    
    # Build the first half string
    first_half_str = ''.join(first_half)
    
    # Build the second half string by reversing the first half
    second_half_str = first_half_str[::-1]
    
    # Combine to get the final palindrome
    encoded_name = first_half_str + middle + second_half_str



    return encoded_name


    # char_count={}
    # first_half = []
    # middle=''

    # for char in nameString:
    #     if char in char_count:
    #         char_count[char]+=1 
    #     else:
    #         char_count[char] = 1

    # sorted_char=sorted(char_count.keys())
    # for char in sorted_char:
    #     count=char_count[char]
    #     half = count //2 
    #     first_half.append(char*half)
    #     char_count[char] -= half*2 

    # for char in sorted_char:
    #     if char_count[char]==1:
    #         middle = char 
    #         break 

    # first_half_str = ''.join(first_half)

    # second_half_str =first_half[::-1]


    # encoded= first_half_str+middle +second_half_str
    # return encoded 







class TestComputeEncodedProductName(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(computeEncodedProductName("babab"), "abbba")

    def test_case_2(self):
        self.assertEqual(computeEncodedProductName("yxxy"), "xyyx")

if __name__ == "__main__":
    unittest.main()
