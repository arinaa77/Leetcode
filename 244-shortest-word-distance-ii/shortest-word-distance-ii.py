class WordDistance:

    def __init__(self, wordsDict: List[str]):
        # Time: O(n)
        # Space: O(n)
        self.record = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.record[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        # Time: O(p + q)
        indices1 = self.record[word1]
        indices2 = self.record[word2]

        i, j = 0, 0
        result = float('inf')
        while i < len(indices1) and j < len(indices2):
            result = min(result, abs(indices1[i] - indices2[j]))
            if indices1[i] < indices2[j]:
                i += 1
            else:
                j += 1
        
        return result
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)