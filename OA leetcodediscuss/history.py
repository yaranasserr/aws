# https://leetcode.com/discuss/post/6671715/amazon-oa-by-anonymous_user-8zh6/
# Example:
# history = "abcdefdefabcghidefabcxyz"
# products = ["abc", "def", "ghi"]

# Output: 3

# Explanation:

# Substring "defabcghi" starting at index 3: 'abcdef-defabcghi-defabcxyz'
# Substring "abcghidef" starting at index 6: 'abcdefdef-abcghidef-abcxyz'
# Substring "ghidefabc" starting at index 9: 'abcdefdefabc-ghidefabc-xyz'
# sliding window 
from collections import defaultdict
class Solution :
    def countsubstrings(self,history,products) -> int:
        n = len(products)
        m = len(products[0])
        l = len(history)
        w = n*m # window
        if l < w:
            return 
        product_count = {}
        for product in products:
            if product in product_count:
                product_count[product] += 1
            else:
                product_count[product] = 1

        result = 0
        for i in range(l - w + 1):
            match = True 
            seen = defaultdict(int)
            for j in range(n):
                start = i + j * m
                chunk = history[start:start + m]
                seen[chunk] += 1
                if seen[chunk] > product_count.get(chunk, 0):
                    match = False
                    break
                if match and seen == product_count:
                    result += 1           

        return result 
        


       
    
# Example usage
history = "abcdefdefabcghidefabcxyz"
products = ["abc", "def", "ghi"]
solution = Solution()
result = solution.countsubstrings(history, products)
print(result)  

