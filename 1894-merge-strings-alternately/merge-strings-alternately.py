class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Time: O(n)
        # Space: O(1)
        shorter = min(len(word1), len(word2))
        result = ''
        i = 0

        while i < shorter:
            result += word1[i]
            result += word2[i]
            i += 1
        
        longer = word1 if len(word1) > len(word2) else word2
        result += longer[i:]
        
        return result