# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            res.append(root.val)
            traverse(root.right)
        
        res = []
        traverse(root)
        return res
        '''
        
        stack = []
        result = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            result.append(root.val)

            root = root.right

        return result