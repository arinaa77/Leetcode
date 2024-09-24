class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        record = defaultdict(int)
        for num in nums:
            record[num] += 1
        
        result = 0
        for key, value in record.items():
            if value > 1:
                result = key
        return result
        '''

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1

            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left