class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Document the last occurance of each element
        last_occurance = {}
        for i, char in enumerate(s):
            last_occurance[char] = i
        
        start = 0
        end = 0
        result = []

        for i, char in enumerate(s):
            end = max(end, last_occurance[char])
            if end == i:
                result.append(end - start + 1)
                start = i + 1

        return result