class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # Use a list of strings to keep track of each digit
        str_num = list(str(n))

        # Adjust each digit in reverse order
        for i in range(len(str_num) - 1, 0, -1):
            # If one digit is greater than the digit after it
            # Subtract the digit by one and change the following digits to 9
            if str_num[i - 1] > str_num[i]:
                str_num[i - 1] = str(int(str_num[i - 1]) - 1)
                for j in range(i, len(str_num)):
                    str_num[j] = '9'
        
        return int(''.join(str_num))