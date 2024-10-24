class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Time: O(len(allowed) + len(words))
        # Space: O(n)
        records = set()
        result = 0

        for char in allowed:
            records.add(char)
        
        for word in words:
            is_in_allowed = True
            for char in word:
                if char not in records:
                    is_in_allowed = False
                    break
            if is_in_allowed:
                result += 1
        
        return result
