class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # Time: O(n)
        # Space: O(1)
        record = defaultdict(int)

        # O(n)
        for char in s:
            record[char] += 1
        for char in t:
            record[char] -= 1
        
        cnt = 0
        for value in record.values(): # O(1)
            if value > 0:
                cnt += value
        
        return cnt