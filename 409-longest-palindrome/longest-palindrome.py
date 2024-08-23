class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Time: O(n)
        # Space: O(1): size of dict is constant, only depends on number of letters
        records = defaultdict(int)
        for char in s:
            records[char] += 1
        
        result = 0
        has_odd_num = False

        for cnt in records.values():
            result += (cnt // 2) * 2
            if cnt % 2 != 0:
                has_odd_num = True
        
        if has_odd_num:
            result += 1

        return result