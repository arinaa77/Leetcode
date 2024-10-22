class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # Time: O(n * m)
        # Space: O(1)
        result = 0
        
        for word in words:
            match = True
            if len(pref) > len(word):
                continue
            for i in range(len(pref)):
                if word[i] != pref[i]:
                    match = False
                    break
            if match:
                result += 1

        return result

        '''
        # Time: O(n * m)
        # Space: O(1)
        # 1
        result = 0
        for word in words:
            if word.startswith(pref):
                result += 1

        return result

        # 2
        result = 0
        for word in words:
            if word[:len(pref)] == pref:
                result += 1

        return result
        '''