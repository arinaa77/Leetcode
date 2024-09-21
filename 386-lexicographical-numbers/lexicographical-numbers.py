class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # Time: O(n)
        # Space: O(n)
        
        def traverse(root, n):
            nonlocal result
            if root > n:
                return
            result.append(root)
            for child in range(root * 10, root * 10 + 10):
                if child > n:
                    break
                traverse(child, n)
            
        result = []
        for i in range(1, 10):
            traverse(i, n)
        return result