class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1_ind, word2_ind = -1, -1
        result = float('inf')
        
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                word1_ind = i
            elif wordsDict[i] == word2:
                word2_ind = i
            
            if word1_ind != -1 and word2_ind != -1:
                result = min(result, abs(word1_ind - word2_ind))
        
        return result