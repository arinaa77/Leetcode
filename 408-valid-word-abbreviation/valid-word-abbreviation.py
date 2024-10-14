class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # Time: O(m + n)
        # Space: O(1)
        
        if len(abbr) > len(word):
            return False
        
        word_pointer, abbr_pointer = 0, 0

        while word_pointer < len(word) and abbr_pointer < len(abbr):
            if abbr[abbr_pointer].isdigit():
                if abbr[abbr_pointer] == '0':
                    return False
                skip = 0
                while abbr_pointer < len(abbr) and abbr[abbr_pointer].isdigit():
                    skip = skip * 10 + int(abbr[abbr_pointer])
                    abbr_pointer += 1
                word_pointer += skip
            else:
                if word[word_pointer] != abbr[abbr_pointer]:
                    return False
                word_pointer += 1
                abbr_pointer += 1
            
        return word_pointer == len(word) and abbr_pointer == len(abbr)

                