class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Time: O(nlog(sum(weights) - max(weights)))
        # Space: O(1)
        left, right = max(weights), sum(weights)

        # O(n)
        def can_ship_with(capacity):
            total_days = 1
            curr_weight = 0
            for w in weights:
                if curr_weight + w > capacity:
                    total_days += 1
                    curr_weight = 0
                curr_weight += w

            return total_days <= days
         # O(log(sum(weights) - max(weights)))
        while left < right:
            mid = left + (right - left) // 2
            if can_ship_with(mid):
                right = mid
            else:
                left = mid + 1
        
        return left