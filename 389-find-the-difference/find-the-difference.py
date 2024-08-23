class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Time: O(n)
        # Space: O(1)

        records = defaultdict(int)

        for char in s:
            records[char] += 1
        
        for char in t:
            records[char] -= 1
            if records[char] < 0:
                return char
            
        for char in records():
            if records[char] != 0:
                return char

        # Time: O(n^2)
        # Space: O(1)
        for char in t:
            if char not in s:
                return char