# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Time: O(n)
        # Space: O(n)
        def traverse(root, result, depth):
            if not root:
                return
            
            if len(result) == depth:
                result.append([])
            result[depth].append(root.val)
            
            traverse(root.left, result, depth + 1)
            traverse(root.right, result, depth + 1)

        result = []
        traverse(root, result, 0)
        return result