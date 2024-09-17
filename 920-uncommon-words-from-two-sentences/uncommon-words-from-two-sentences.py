class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        list1 = s1.split()
        list2 = s2.split()
        result = []

        word_cnt = Counter(list1 + list2)

        for word, cnt in word_cnt.items():
            if cnt == 1:
                result.append(word)
        
        return result
