class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Time: O(nlogn + n^2)
        # Space: O(n)

        # Sort the list in descending order according to height
        # If height is the same, start with smallest k
        people.sort(key=lambda x: (-x[0], x[1]))

        que = []
        for p in people:
            # Insert position depends on ascending k
            que.insert(p[1], p)

        return que