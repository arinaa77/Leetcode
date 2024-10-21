class Solution:
    def reverseVowels(self, s: str) -> str:
        # Time: O(n)
        # Space: O(1)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        return ''.join(s)

        '''
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        vowel_list = []
        for char in s:
            if char in vowels:
                vowel_list.append(char)
        
        result = []
        i = len(vowel_list) - 1
        for char in s:
            if char in vowels:
                result.append(vowel_list[i])
                i -= 1
            else:
                result.append(char)
        
        return ''.join(result)
        '''