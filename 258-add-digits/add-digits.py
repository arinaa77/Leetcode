class Solution:
    def addDigits(self, num: int) -> int:
        # If num has more than 1 digit, process the num
        while num >= 10:
            sum = 0
            while num:
                sum += num % 10
                num //= 10
            num = sum
        
        return num