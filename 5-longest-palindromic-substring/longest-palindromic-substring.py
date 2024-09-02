class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Time: O(n^2)
        # Space: O(n)
        
        def palindrome(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]
        
        result = ''
        for i in range(len(s)):
            s1 = palindrome(s, i, i)
            s2 = palindrome(s, i, i + 1)
            result = s1 if len(s1) > len(result) else result
            result = s2 if len(s2) > len(result) else result

        return result