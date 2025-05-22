from typing import List
"""
You are given a potentially large list of words.

Some of these are compounds, where all parts are also in the list.

Identify all combinations where one word can be composed of two or more
words of the same list and print or return them.

Example:
Input: [rockstar, rock, star, rocks, tar, stars, rockstars, super, highway, high, way, superhighway]

Output:
rockstar -> rock + star
rockstar -> rocks + star
rockstars -> rock + stars
superhighway -> super + highway
superhighway -> super + high + way

Or if returning, the output would be a list of lists, e.g.
[
[rock, star],
[rocks, tar],
[rock, stars],
[high, way],
[super, highway],
"""

def find_compound_words(words: List[str]) -> List[List[str]]:
    word_set = set(words)  # Use a set for O(1) lookups
    result = []
    
    def backtrack(s, i, cur):
        if i == len(s):
            result.append(cur[:])  # Store the decomposition as a list
            return
        
        for j in range(i, len(s)):
            w = s[i:j+1]
            if w in word_set:
                cur.append(w)
                backtrack(s, j+1, cur)
                cur.pop()
    
    for word in words:
        word_set.remove(word)  # Remove word temporarily to avoid self-match
        cur = []
        backtrack(word, 0, cur)
        word_set.add(word)  # Restore word
    
    return result

# Example usage
words = ["rockstar", "rock", "star", "rocks", "tar", "stars", "rockstars", "super", "highway", "high", "way", "superhighway"]
output = find_compound_words(words)

# Printing the output
for combination in output:
    print(" + ".join(combination))
