# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # Time: O(n)
        # Space: O(h)
        def get_sum(root):
            nonlocal total_sum
            if not root:
                return 0
            total_sum += root.val
            get_sum(root.left)
            get_sum(root.right)

        def get_max_product(root):
            nonlocal max_product
            if not root:
                return 0
            subtree_sum = root.val + get_max_product(root.left) + get_max_product(root.right)
            max_product = max(max_product, subtree_sum * (total_sum - subtree_sum))
            return subtree_sum

        total_sum = 0
        max_product = 0
        get_sum(root)
        get_max_product(root)
        return max_product % (10 ** 9 + 7)          