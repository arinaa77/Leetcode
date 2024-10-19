class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        # Time: O(nlogn)
        # Space: O(n)
        max_points = sum(reward2)

        diff = [(reward1[i] - reward2[i]) for i in range(len(reward1))]
        diff.sort(reverse=True)

        max_points += sum(diff[:k])
        return max_points