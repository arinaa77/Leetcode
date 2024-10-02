class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path, used, result):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                # Track if num is used by index
                if used[i]:
                    continue
                    
                used[i] = True
                path.append(nums[i])
                backtrack(nums, path, used, result)
                path.pop()
                used[i] = False

        result = []
        used = [False] * len(nums)
        backtrack(nums, [], used, result)
        return result