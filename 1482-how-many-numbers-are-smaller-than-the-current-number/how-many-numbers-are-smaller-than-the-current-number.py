class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        '''
        # Time: O(n^2)
        if not nums:
            return []

        result = []
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    cnt += 1
            result.append(cnt)
        
        return result
        '''
        # Time: O(nlogn)
        sorted_nums = sorted(nums)
        nums_dict = {}

        for i, num in enumerate(sorted_nums):
            if num not in nums_dict:
                nums_dict[num] = i
        
        result = [nums_dict[num] for num in nums]
        return result
                