class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Time: O(len(str1) + len(str2))
        # Space: O(len(str1) + len(str2))
        if str1 + str2 != str2 + str1:
            return ''
        common_char = math.gcd(len(str1), len(str2))
        return str1[:common_char]

        '''
        def can_divide(string, substr):
            repeat = len(string) // len(substr)
            return repeat * substr == string
        
        gcd_string = math.gcd(len(str1), len(str2))
        substr = str1[:gcd_string]
        if can_divide(str1, substr) and can_divide(str2, substr):
            return substr
        else:
            return ''
        '''