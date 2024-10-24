# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(n)
    # Space: O(n)
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        column_table = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()
            if node:
                column_table[column].append(node.val)

                if node.left:
                    queue.append((node.left, column - 1))
                if node.right:
                    queue.append((node.right, column + 1))
        
        low = min(column_table.keys())
        high = max(column_table.keys())

        result = []
        for i in range(low, high + 1):
            result.append(column_table[i])
        return result