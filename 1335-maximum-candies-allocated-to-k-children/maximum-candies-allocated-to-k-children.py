class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Time: O(nlog(max(candies)))
        # Space: O(1)
        def can_distribute(mid):
            total_children = 0
            for c in candies:
                total_children += c // mid
            return total_children >= k

        left, right = 1, max(candies)

        result = 0
        while left <= right:
            mid = left + (right - left) // 2

            if can_distribute(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
