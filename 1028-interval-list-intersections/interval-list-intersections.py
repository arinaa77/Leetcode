class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # Time: O(m * n)
        # Space: O(k)
        if not len(firstList) or not len(secondList):
            return []

        intersection_list = []
        for f in firstList:
            for s in secondList:
                if f[1] >= s[0]:
                    start = max(s[0], f[0])
                    end = min(s[1], f[1])
                    if end >= start:
                        intersection_list.append([start, end])

        return intersection_list