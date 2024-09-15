class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        path = []
        used = [False] * len(nums)

        self.backtrack(nums, path, used)
        return self.result
    
    def backtrack(self, nums, path, used):
        # Base case
        if len(path) == len(nums):
            self.result.append(path.copy())
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            # Make the choice
            path.append(nums[i])
            used[i] = True
            # Recursively go deeper into the decision tree
            self.backtrack(nums, path, used)
            # Undo the choice (backtrack)
            path.pop()
            used[i] = False