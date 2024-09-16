class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, start, path, result):
            result.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(nums, i + 1, path, result)
                path.pop()

        result = []
        backtrack(nums, 0, [], result)
        return result