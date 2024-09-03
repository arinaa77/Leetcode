class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums_str = ''
        for char in s:
            pos = ord(char) - ord('a') + 1
            nums_str += str(pos)
        
        for _ in range(k):
            total = 0
            for digit in nums_str:
                total += int(digit)
            nums_str = str(total)
        
        return int(nums_str)
