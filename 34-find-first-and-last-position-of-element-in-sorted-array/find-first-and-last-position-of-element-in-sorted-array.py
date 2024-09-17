class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left_bound(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] >= target:
                    right = mid - 1
            if left >= len(nums) or nums[left] != target:
                return -1
            return left

        def right_bound(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
            if right < 0 or nums[right] != target:
                return -1
            return right

        return [left_bound(nums, target), right_bound(nums, target)]
        '''
        def binarySearch(nums, target):
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        
        left_boarder = binarySearch(nums, target)
        right_boarder = binarySearch(nums, target + 1) - 1

        if left_boarder == len(nums) or nums[left_boarder]!= target:
            return [-1, -1]

        return [left_boarder, right_boarder]
        '''